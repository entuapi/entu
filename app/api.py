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
        
        entity = db.Entity(user_locale=self.get_user_locale())
        
        result = entity.get(ids_only=ids_only,entity_id=entity_id,search=keywords,
                            entity_definition_keyname=entity_definition,dataproperty=dataproperty,limit=limit,
                            full_definition=full_definition,only_public=public)
        
        if result == None:
            self.write('')
        elif size(result) > 5:
            self.write(json.dumps(result))
        else:
            entity_ids = []
            for entity in result:
                entity_ids.append(entity['id'])
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
        entity = db.Entity(user_locale=self.get_user_locale())
        
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
        
        entity_definition = self.get_argument('entity_type',None)
        
        if entity_definition == None:
            raise web.HTTPError(400,'Entity type required.')
        
        parent = self.get_argument('parent', None)
        
        entity = db.Entity(user_locale=self.get_user_locale())
        entity_id = entity.create(entity_definition_keyname=entity_definition,parent_entity_id=parent)
        
        
        
    def post(self):
        raise web.HTTPError(405,'Currently using GET method.')
        
class Edit (myRequestHandler):
    """
    API edit entity function.
    
    """
    def get(self):
        print "Hello edit!";
        #TODO rest
   
    def post(self):
        raise web.HTTPError(405,'Currently using GET method.')
        
        
handlers = [
    ('/add', Add),
    ('/view', View),
    ('/search', Search),
    ('/edit', Edit),
]