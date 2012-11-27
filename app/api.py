from helper import *
from db import Entity
from tornado import web
from tornado import auth
from tornado import httpclient
from tornado import escape
import json
import urllib
import urlparse
import string
import hashlib
import random
import time
import magic

class Search (myRequestHandler):
    """
    API search for entities based on keywords,entity type and
    dataproperty.
    
    
    search?[full_info=$full_info][&search=$search][&entity_definition_keyname=$entity_definition_keyname]
    
    [&dataproperty=$dataproperty][&limit=$limit][&full_definition=$full_definition][&public=$public]
    
    
    $full_info = [(true)|(false)]
    $search = (string)
    $entity_definition_keyname = (string)
    $dataproperty = (string)
    $limit = (int)
    $full_definition = [(true)|(false)]
    $public = [(true)|(false)]
    
    Parameters:
    
        full_info - if 'true', returns all available visible data regarding the queried entities,
                    otherwise ('false') returns minimalistic descriptive data:
                        * entity_id
                        * displayname
                        * displayinfo
                        * displaypicture
                        * displaytable
           
                   DEFAULT = false
                    
                        
        search  -   filters returned entities by returning only those entities which property has 
                    one of the 'search' phrases as 'value_string' attribute
                    
                    e.g. ?search=name%20title%20author%20creator
               
                    
        entity_definition_keyname - returns entities which are of specified type
        
                    e.g. ?entity_definition_keyname=book
                    
        
        dataproperty - 
        
        
        limit - maximum number of entities returned
        
                    e.g. ?limit=5
                    
                    DEFAULT = unlimited
                    
                    
        full_definition - if 'true', returns empty fields, otherwise 'false'
        
                    e.g. ?full_definition=true
                    
                    DEFAULT = false
                    
            
        public - if 'true', returns only public entities with public properties
        
                    e.g. ?public=true
    
                    DEFAULT = false
    
    
    Returns:
    
        No results:
        
            HTTP status code 404
            
        full_info = true:
        
            [{'id':val1,'displayname':val2,'displayinfo':val3,'displaypicture':val4,'displaytable':val5},
             ...,
            {'id':valx,'displayname':valy,'displayinfo':valz,'displaypicture':valv,'displaytable':valw}]
            
        otherwise:
        
            [{visible_entity1_fields},...,{visible_entityN_fields}]
            
            
    """
    def get(self):
        full_info = True if self.get_argument('full_info',default=None,strip=True) == 'true' else False
        keywords = self.get_argument('search',default=None,strip=True)
        entity_definition = self.get_argument('entity_definition_keyname',default=None,strip=True)
        dataproperty = self.get_argument('dataproperty',default=None,strip=True)
        limit = self.get_argument('limit',default=None,strip=True)
        full_definition = True if self.get_argument('full_definition',default=None,strip=True) == 'true' else False
        public = True if self.get_argument('public',default=None,strip=True) == 'true' else False
              
        entity = db.Entity(user_locale=self.get_user_locale())
        
        result = entity.get(ids_only=False, search=keywords,
                            entity_definition_keyname=entity_definition, dataproperty=dataproperty, limit=limit,
                            full_definition=full_definition, only_public=public)
       
        if not result:
            return self.missing()
       
        datetime_to_ISO8601(result)
              
        if not full_info:
            entities = []
            for entity in result:
                entity_obj = {}
                entity_obj['id'] = entity['id']
                entity_obj['displayname'] = entity['displayname']
                entity_obj['displayinfo'] = entity['displayinfo']
                entity_obj['displaypicture'] = entity['displaypicture']
                entity_obj['displaytable'] = entity['displaytable']
                entities.append(entity_obj)
            self.write(json.dumps(entities))

        else:
            self.write(json.dumps(result))

       
class View (myRequestHandler):
    """
    Returns entity by entity_id.
    
    view?entity_id=$entity_id[&public=$public][&full_definition=$full_definition]
    
    $entity_id = (int)
    $public = [(true)|(false)]
    $full_definition = [(true)|(false)]
    
    Parameters:
    
        entity_id (REQUIRED) - ID of the queried entity
        
        public - if 'true', searches among entities which are public and have public property
        
                DEFAULT = false
        
        full_definition - if 'true', includes properties that have empty values
        
                DEFAULT = false
    
    """    
    def get(self):        
        entity_id = self.get_argument('entity_id',default=None,strip=True)
       
        if not entity_id:
            raise web.HTTPError(400,'Entity ID required.')
       
        only_public = True if self.get_argument('public',default=None,strip=True) == '1' else False
        full_definition = True if self.get_argument('full_definition',default=None,strip=True) == 'true' else False
        
        entity = db.Entity(user_locale=self.get_user_locale())
       
        result = entity.get(entity_id=entity_id, limit=1, full_definition=full_definition, only_public=only_public)
       
        if not result:
            return self.missing()
       
        datetime_to_ISO8601(result)
       
        self.write(json.dumps(result))
        
class GetEntityProperties(myRequestHandler):
    
    """    
    Returns all the properties as templates that an entity with a specified definition_keyname can possess.
    
    get_entity_properties?entity_definition_keyname=$entity_definition_keyname
    
    $entity_definition_keyname = (string)
    
    Parameters:
    
        entity_definition_keyname (REQUIRED) - entity type under scrutiny
        
        e.g. ?entity_definition_keyname=library
        
        
    Returns:
    
        entity_definition_keyname missing:
        
            HTTP status 400
            
        otherwise:
        
            [{property1_fields},...,{propertyN_fields}]
    
    """
    
    def get(self):        
        entity_definition_keyname = self.get_argument('entity_definition_keyname',default=None,strip=True)
        
        if not entity_definition_keyname:
            raise web.HTTPError(400,'entity_definition_keyname required.')
        
        entity = db.Entity(user_locale=self.get_user_locale())
        
        self.write(json.dumps(entity.get_definition(entity_definition_keyname)))


class GetAllowedChilds(myRequestHandler):
    """
    Returns allowed child-entity definitions, when entity_id is provided
    
    get_allowed_childs?entity_id=$entity_id
    
    $entity_id = (int)
    
    Parameters:
    
        entity_id (REQUIRED) - entity type
        
        e.g. ?entity_id=35
        
    Returns:
    
        [{"keyname":$keyname,"label":$label,"label_plural":$label_plural,"description":$description,"menugroup":$menugroup},...]
        
        $keyname = (string)
        
            entity_definition_keyname that can be used to create a new entity
            
        $label = (string)
        
            title for displaying
            
        $label_plural = (string)
    
            title in plural for displaying
            
        $description = (string)
        
            optional description of the entity type
            
        $menugroup = (string)
        
            suggests a name for the menu title
    
    """    
    def get(self):
        entity_id = self.get_argument('entity_id',default=None,strip=True)
        
        if not entity_id:
            raise web.HTTPError(400,'entity_id required')
        
        entity = db.Entity(user_locale=self.get_user_locale())
        
        self.write(json.dumps(entity.get_allowed_childs(entity_id)))
        
     
class SaveEntity(myRequestHandler):
    """
    API save entity function.
    Needs entity ID and optionally parent ID.
    Return Entity ID.
    
    save_entity?entity_definition_keyname=$entity_definition_keyname[&parent_entity_id=$parent_entity_id][&public=$public]
    
    
    $entity_definition_keyname = (string)
    $parent_entity_id = (int)
    $public = [(true)|(false)]
    
    Parameters:
    
        entity_definition_keyname (REQUIRED) - type of the created entity
        
                e.g. ?entity_definition_keyname=book
                
                
        parent_entity_id - propagates rights from the parent and sets a parent-child relationship
        
                e.g. ?parent_entity_definition=514
                
        
        public - allows entity to be seen without authentication
        
                e.g. ?public=true
                
    Returns:
    
        entity_definition_keyname missing:
        
            HTTP status 400
            
        otherwise:
        
            {'entity_id':ID}
    
    """
    def get(self):       
        parent_entity_id = self.get_argument('parent_entity_id', default=None, strip=True)
        entity_definition_keyname = self.get_argument('entity_definition_keyname', default=None, strip=True)
        public = True if self.get_argument('public', default=None, strip=True) == 'true' else False
      
        if entity_definition_keyname != None:
            entity = db.Entity(user_locale=self.get_user_locale())
            entity_id = entity.create(entity_definition_keyname=entity_definition_keyname, parent_entity_id=parent_entity_id)
            if public:
                entity.set_public(entity_id,is_public=public)            
            self.write({
                        'entity_id':entity_id
            })
        else:
            raise web.HTTPError(400, 'To create a new Entity entity_definition_keyname is required.')

class SaveProperty(myRequestHandler):  
    """
    Add or edit property value.
    Creates new one if property_id = None, otherwise changes existing.
    Returns property ID.
    
    #1  save_property?entity_id=$entity_id&property_definition_keyname=$property_Definition_keyname
    
        [&property_id=$property_id][&value=$value]
    
          
    #2 save_property?properties=$properties
    
        $properties = [
                        {
                          'entity_id':$entity_id#1,
                          'property_definition_keyname':$property_definition_keyname#1
                          [,'property_id':$property_id#1]
                          [,'value':$value#1]
                          [,'file':$file#1]
                        }
                        ,...,
                        {
                          'entity_id':$entity_id#N,
                          'property_definition_keyname':$property_definition_keyname#N
                          [,'property_id':$property_id#N]
                          [,'value':$value#N]
                          [,'file':$file#N]
                        }
                      ]
    
    $entity_id = (int)
    $property_definition_keyname = (string)
    $property_id = (int)
    $value = *
    $file = (string)
    
    Parameters:
    
        entity_id (REQUIRED) - ID of the entity that the given property belongs to
        
        
        property_definition_keyname (REQUIRED) - type of property
    
            e.g. ?property_definition_keyname=textbook-picture
            
            
        property_id - ID of an existing property to be changed
        
        
        value - value for the given property
        
        
        file (ONLY IN JSON) - name of the uploaded file
        
        
    Uploading file:
    
        In order to upload file, property_definition_keyname must map to property_definition which datatype is 'file'.
        
        Also, if non-json format is used (aka not using 'properties' parameter), file should be uploaded under 'file' name.
        If json format is used, each property's 'file' field must map to uploaded file's name.
        
        Uploaded file's name can be set, using, for example, simple html form:
        
            <form action="http://address.to.entu.api/save_property" method="post" enctype="multipart/form-data">
                <label for="file">Filename:</label>
                <input type="file" name="UPLOADED_FILE_NAME" id="file" />
                <br />
                <input type="submit" name="submit" value="Submit" />
            </form>
        
    """
    def get(self):
        entity_id = self.get_argument('entity_id', default=None, strip=True)
        property_definition_keyname = self.get_argument('property_definition_keyname', default=None, strip=True)
      
        # if data is passed as json
        if not entity_id and not property_definition_keyname:
            properties = self.get_argument('properties',default=None,strip=True)
            if not properties:
                raise web.HTTPError(400, 'Invalid data passed')
            
            properties = json.loads(properties)
            
            if not isinstance(properties,list):
                properties = [properties]
            
            entity = db.Entity(user_locale=self.get_user_locale())
            property_id_list = []
              
            for property in properties:
                entity_id = property.setdefault('entity_id',None)
                property_definition_keyname = property.setdefault('property_definition_keyname',None)
                property_id = property.setdefault('property_id',None)
                value = property.setdefault('value',None)
                uploaded_file_name = property.setdefault('file',None)
                uploaded_file = self.request.files.get(uploaded_file_name,None) if uploaded_file_name != None else None
                
                if entity_id and property_definition_keyname:
                    property_id_list.append(entity.set_property(entity_id=entity_id, property_definition_keyname=property_definition_keyname, value=value, property_id=property_id, uploaded_file=uploaded_file))
                else:
                    raise web.HTTPError(400, 'entity_id and property_definition_keyname required')
            
            self.write(json.dumps(property_id_list))
            self.finish()
            
        else:      
            property_id = self.get_argument('property_id', default=None, strip=True)
            value = self.get_argument('value', default=None, strip=True)
            uploaded_file = self.request.files.get('file', [])[0] if self.request.files.get('file', None) else None
          
            entity = db.Entity(user_locale=self.get_user_locale())
            if entity_id:
                property_id = entity.set_property(entity_id=entity_id, property_definition_keyname=property_definition_keyname, value=value, property_id=property_id, uploaded_file=uploaded_file)    
                self.write({
                            'property_id':property_id
                })
            else:
                raise web.HTTPError(400, 'Entity ID required')


class GetFile(myRequestHandler):
    @web.authenticated
    def get(self):
        """
        Returns file using file_id.
        
        get_file?file_id=$file_id
        
        $file_id = (int)
        
        
        Parameters:
        
            file_id (REQUIRED) - ID of the desired file
         
            
        Returns:
        
            file
        
        """
        
        file_id = self.get_argument('file_id',default=None,strip=True)
            
        if not file:
            return self.missing()    
            
        file = db.Entity(user_locale=self.get_user_locale(), user_id=self.current_user.id).get_file(file_id)
        
        if not file:
            return self.missing()

        ms = magic.open(magic.MAGIC_MIME)
        ms.load()
        mime = ms.buffer(file.file)
        ms.close()

        self.add_header('Content-Type', mime)
        self.add_header('Content-Disposition', 'attachment; filename="%s"' % file.filename)
        self.write(file.file)
        

class GetSession(myRequestHandler):
    """
    
    Creates new session for authenticated user.
    
    Returns:
    
        {'session_key':$session_key}
    
    """
    @web.authenticated
    def get(self):
        pass
  
def datetime_to_ISO8601(entity_list):
    """
        Transforms each entity's ordinal field into string format specified by ISO 8601
    """
    if type(entity_list) is not list:
        entity_list = [entity_list]        
    for entity in entity_list:
           datetime_obj = entity['ordinal']
           entity['ordinal'] = "%d%d%dT%d%d%d"%(datetime_obj.year,datetime_obj.month,datetime_obj.day,
                                                datetime_obj.hour,datetime_obj.minute,datetime_obj.second)
       
handlers = [
    ('/save_entity', SaveEntity),
    ('/view', View),
    ('/search', Search),
    ('/save_property', SaveProperty),
    ('/get_entity_properties', GetEntityProperties),
    ('/get_allowed_childs',GetAllowedChilds),
    ('/get_file',GetFile),
    ('/get_session',GetSession)
]
