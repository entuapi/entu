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


class Search (myRequestHandler):
    """
    API search for entities based on keywords,entity type and
    dataproperty.
    
    """
    def get(self):
       
        ids_only = False
        full_info = self.get_argument('full_info',None)
        entity_id = None
        keywords = self.get_argument('search', None)
        entity_definition = self.get_argument('entity_definition_keyname', None)
        dataproperty = self.get_argument('dataproperty', None)
        limit = self.get_argument('limit', None)
        full_definition = True if self.get_argument('full_definition','false') == 'true' else False
        public = True if self.get_argument('public', 'false') == 'true' else False
              
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

       
class View (myRequestHandler):
    """
    Returns entity by entity_id.
    """    
    def get(self):
        entity = db.Entity(user_locale=self.get_user_locale())
        
        entity_id = self.get_argument('entity_id',None)
       
        if not entity_id:
            raise web.HTTPError(400,'Entity ID required.')
       
        only_public = True if self.get_argument('public', '0') == '1' else False
        full_definition = True if self.get_argument('full_definition','false') == 'true' else False
       
        result = entity.get(entity_id=self.get_argument('id'), limit=1, full_definition=full_definition, only_public=only_public)
       
        if not result:
            return self.missing()
       
        datetime_to_ISO8601(result)
       
        self.write(json.dumps(result))
        
class GetEntityProperties(myRequestHandler):
    
    def get(self):
        entity = db.Entity(user_locale=self.get_user_locale())
        
        entity_definition_keyname = self.get_argument('entity_definition_keyname',None)
        
        if not entity_definition_keyname:
            raise web.HTTPError(400,'Entity ID required.')
        
        self.write(json.dumps(entity.get_definition(entity_definition_keyname)))
     
     
class SaveEntity(myRequestHandler):
    """
    API save entity function.
    Needs entity ID and optionally parent ID.
    Return Entity ID.
    """
    def get(self):
       entity = db.Entity(user_locale=self.get_user_locale())
       parent_entity_id = self.get_argument('parent_entity_id', default=None, strip=True)
       entity_definition_keyname = self.get_argument('entity_definition_keyname', default=None, strip=True)
      
       if entity_definition_keyname != None:
           entity_id = entity.create(entity_definition_keyname=entity_definition_keyname, parent_entity_id=parent_entity_id)
           self.write({
               'entity_id':entity_id
           })
       else:
           raise web.HTTPError(400, 'To create new Entity entity_definition_keyname is required.')

class SaveProperty(myRequestHandler):  
    """
    Add or edit property value.
    Creates new one if property_id = None, otherwise changes existing.
    Returns property ID.
    """
    def get(self):
      entity_id = self.get_argument('entity_id', default=None, strip=True)
      property_definition_keyname = self.get_argument('property_definition_keyname', default=None, strip=True)
      property_id = self.get_argument('value_id', default=None, strip=True)
      value = self.get_argument('value', default=None, strip=True)
      public = True if self.get_argument('public', default='false', strip=True) == 'true' else False
      uploaded_file = self.request.files.get('file', [])[0] if self.request.files.get('file', None) else None
      
      entity = db.Entity(user_locale=self.get_user_locale())
      if entity_id:
          property_id = entity.set_property(entity_id=entity_id, property_definition_keyname=property_definition_keyname, value=value, property_id=property_id, uploaded_file=uploaded_file)    
          self.write({
                      'property_id':property_id
          })
      else:
          raise web.HTTPError(400, 'Entity ID required')
  
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
]
