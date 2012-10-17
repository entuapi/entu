from helper import *
from db import Entity
from tornado import web
import json

class Search (myRequestHandler):
    """
    API search for entities based on keywords,entity definition, 
    dataproperty [and entity properties - not implemented].
    
    Returns entity ids if there are more than 5 query results or otherwise 
    respective amount of full entities in json format.
    
    """
    def get(self):
        
        ids_only = False
        entity_id=None
        keywords = self.get_argument('keywords',None)
        entity_definition = self.get_argument('entity_type', None)
        dataproperty = self.get_argument('dataproperty',None)
        limit = self.get_argument('limit',None)
        full_definition = False
        public = True if self.get_argument('public','0') == '1' else False
        
        entity = db.Entity(user_locale=self.get_user_locale(),user_id = self.current_user.id)
        
        result = entity.get(ids_only=ids_only,entity_id=entity_id,search=keywords,
                            entity_definition_keyname=entity_definition,dataproperty=dataproperty,limit=limit,
                            full_definition=full_definition,only_public=public)
        
        if not result:
            return self.missing()
        elif size(result) <= 5:
            self.write(json.dumps(result))
        else:
            entity_ids = []
            for entity in result:
                entity_obj = {}
                entity_obj['id'] = entity['id']
                entity_obj['title'] = entity['displayname']
                entity_obj['info'] = entity['displayinfo']
                entity_obj['image'] = entity['displaypicture']
                entity_ids.append(entity_obj)
            self.write(json.dumps(entity_ids))
            
    def post(self):
        raise web.HTTPError(405,'POST method not supported.')
 
        
        
class View (myRequestHandler):
    """
    API open entity function.
    Needs entity ID.
    TODO MAYBE needs public/non-public???
    """
    def get(self):
        entity = db.Entity(user_locale=self.get_user_locale(),user_id = self.current_user.id)
        
        self.write(entity.get(entity_id=self.get_argument('id'), limit=1, full_definition=True, only_public=False))
        self.write("Open: Done.\n")
        
    def post(self):
        raise web.HTTPError(405,'POST method not supported.')
        
class Add (myRequestHandler):
    """
    API add entity function.
    Needs entity ID and optionally parent ID.
    """
    def get(self):
        
        parent_entity_id            = self.get_argument('parent_entity_id', default=None, strip=True)
        entity_definition_keyname   = self.get_argument('entity_definition_keyname', default=None, strip=True)
        
        if entity_definition == None:
            raise web.HTTPError(400,'Entity type required.')
        
        entity = db.Entity(user_locale=self.get_user_locale(),user_id = self.current_user.id)
        
        entity_id = entity.create(entity_definition_keyname=entity_definition_keyname, parent_entity_id=parent_entity_id)
        
        self.write({
            'entity_id':entity_id
        })
        
        
    def post(self):
        raise web.HTTPError(405,'Currently using GET method.')
        
class Edit (myRequestHandler):
    """
    API edit entity function.
    
    """
    def get(self):
        entity_id = self.get_argument('entity_id', default=None, strip=True)
        
        property_definition_keyname = self.get_argument('property_definition_keyname', default=None, strip=True)
        property_id                 = self.get_argument('value_id', default=None, strip=True)
        value                       = self.get_argument('value', default=None, strip=True)
        is_counter                  = self.get_argument('counter', default='false', strip=True)
        is_public                   = self.get_argument('is_public', default='false', strip=True)
        uploaded_file               = self.request.files.get('file', [])[0] if self.request.files.get('file', None) else None
        
        if not entity_id:
            raise web.HTTPError(400,'Entity ID required.')
        
        entity = db.Entity(user_locale=self.get_user_locale(), user_id=self.current_user.id)
        
        if is_counter.lower() == 'true':
            value = entity.set_counter(entity_id=entity_id)
        elif is_public.lower() == 'true':
            value = True if value.lower() == 'true' else False
            value = entity.set_public(entity_id=entity_id, is_public=value)
        else:
            property_id = entity.set_property(entity_id=entity_id, property_definition_keyname=property_definition_keyname, value=value, property_id=property_id, uploaded_file=uploaded_file)

   
    def post(self):
        raise web.HTTPError(405,'Currently using GET method.')

        
handlers = [
    ('/add', Add),
    ('/view', View),
    ('/search', Search),
    ('/edit', Edit),
]