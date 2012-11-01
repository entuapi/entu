from helper import *
from db import Entity
from tornado import web
import json

class Search (myRequestHandler):
    """
    API search for entities based on keywords,entity type and
    dataproperty.
    
    """
    def get(self):
       
        ids_only = False
        full_info = self.get_argument('full_info',None)
        entity_id = None
        keywords = self.get_argument('keywords', None)
        entity_definition = self.get_argument('entity_type', None)
        dataproperty = self.get_argument('dataproperty', None)
        limit = self.get_argument('limit', None)
        full_definition = False
        public = True if self.get_argument('public', '0') == '1' else False
              
        entity = db.Entity(user_locale=self.get_user_locale())
        
        result = entity.get(ids_only=ids_only, entity_id=entity_id, search=keywords,
                            entity_definition_keyname=entity_definition, dataproperty=dataproperty, limit=limit,
                            full_definition=full_definition, only_public=public)
       
        if not result:
            return self.missing()
       
        datetime_to_ISO8601(result)
              
        if not full_info:
            entity_ids = []
            for entity in result:
                entity_obj = {}
                entity_obj['id'] = entity['id']
                entity_obj['displayname'] = entity['displayname']
                entity_obj['displayinfo'] = entity['displayinfo']
                entity_obj['displaypicture'] = entity['displaypicture']
                entity_obj['displaytable'] = entity['displaytable']
                entity_ids.append(entity_obj)
            self.write(json.dumps(entity_ids))

        else:
            self.write(json.dumps(result))


    def post(self):
        raise web.HTTPError(405, 'POST method not supported.')

       
       
class View (myRequestHandler):
    """
    Returns entity by entity_id.
    """    
    def get(self):
        entity = db.Entity(user_locale=self.get_user_locale())
        
        entity_id = self.get_argument('id',None)
       
        if not entity_id:
            raise web.HTTPError(400,'Entity ID required.')
       
        only_public = True if self.get_argument('public', '0') == '1' else False
       
        result = entity.get(entity_id=self.get_argument('id'), limit=1, full_definition=True, only_public=False)
       
        if not result:
            return self.missing()
       
        datetime_to_ISO8601(result)
       
        self.write(json.dumps(result))
       
    def post(self):
        raise web.HTTPError(405, 'POST method not supported.')
     
     
class Save(myRequestHandler):
    """
    API add and edit entity combinated functions
    """
    def get(self):
       entity_id = self.get_argument('entity_id', default=None, strip=True)
       entity = db.Entity(user_locale=self.get_user_locale())
       
       """
       If there is no entity_id given, then create new Entity
       """
       if not entity_id:
           parent_entity_id = self.get_argument('parent_entity_id', default=None, strip=True)
           entity_definition_keyname = self.get_argument('entity_definition_keyname', default=None, strip=True)
       
           if entity_definition_keyname != None:
               entity_id = entity.create(entity_definition_keyname=entity_definition_keyname, parent_entity_id=parent_entity_id)
               self.write({
                   'entity_id':entity_id
               })
           else:
               raise web.HTTPError(400, 'Entity ID required. To create new Entity, entity_definition_keyname is required.')
       
       """
       Save property value. Creates new one if property_id = None. Returns property ID.
       """
       property_definition_keyname = self.get_argument('property_definition_keyname', default=None, strip=True)
       property_id = self.get_argument('value_id', default=None, strip=True)
       value = self.get_argument('value', default=None, strip=True)
       is_counter = self.get_argument('counter', default='false', strip=True)
       is_public = self.get_argument('is_public', default='false', strip=True)
       uploaded_file = self.request.files.get('file', [])[0] if self.request.files.get('file', None) else None
       
       property_id = entity.set_property(entity_id=entity_id, property_definition_keyname=property_definition_keyname, value=value, property_id=property_id, uploaded_file=uploaded_file)    
       
       if property_id:
           self.write({
                   'property_id':property_id
               })
       
       
    def post(self):
       raise web.HTTPError(405, 'Currently using GET method.')
  
class Add (myRequestHandler):
    """
    API add entity function.
    Needs entity ID and optionally parent ID.
    """
    def get(self):
       
       parent_entity_id = self.get_argument('parent_entity_id', default=None, strip=True)
       entity_definition_keyname = self.get_argument('entity_definition_keyname', default=None, strip=True)
       
       if entity_definition_keyname == None:
           raise web.HTTPError(400, 'Entity type required.')
       
       entity = db.Entity(user_locale=self.get_user_locale())
       
       entity_id = entity.create(entity_definition_keyname=entity_definition_keyname, parent_entity_id=parent_entity_id)
       
       self.write({
           'entity_id':entity_id
       })
       
       
    def post(self):
       raise web.HTTPError(405, 'Currently using GET method.')
       
class Edit (myRequestHandler):
    """
    API edit entity function.
   
    """
    def get(self):
       entity_id = self.get_argument('entity_id', default=None, strip=True)
       
       property_definition_keyname = self.get_argument('property_definition_keyname', default=None, strip=True)
       property_id = self.get_argument('value_id', default=None, strip=True)
       value = self.get_argument('value', default=None, strip=True)
       is_counter = self.get_argument('counter', default='false', strip=True)
       is_public = self.get_argument('is_public', default='false', strip=True)
       uploaded_file = self.request.files.get('file', [])[0] if self.request.files.get('file', None) else None
       
       if not entity_id:
           raise web.HTTPError(400, 'Entity ID required.')
       
       entity = db.Entity(user_locale=self.get_user_locale())
       
       if is_counter.lower() == 'true':
           value = entity.set_counter(entity_id=entity_id)
       elif is_public.lower() == 'true':
           value = True if value.lower() == 'true' else False
           value = entity.set_public(entity_id=entity_id, is_public=value)
       else:
           property_id = entity.set_property(entity_id=entity_id, property_definition_keyname=property_definition_keyname, value=value, property_id=property_id, uploaded_file=uploaded_file)

  
    def post(self):
       raise web.HTTPError(405, 'Currently using GET method.')

class Auth (myRequestHandler):
    """
    API authentication function.
    """
   
    def get(self):
       print 'Auth get'
       
       provider = self.get_argument('provider', None)
      

    def post(self):
       raise web.HTTPError(401, 'Unauthorized')

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
    ('/add', Add),
    ('/view', View),
    ('/search', Search),
    ('/edit', Edit),
    ('/auth', Auth),
    ('/save', Save),
]
