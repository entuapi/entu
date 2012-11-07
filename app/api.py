from helper import *
from db import Entity
from tornado import web
from tornado import auth
from tornado import httpclient
import json
import urllib
import urlparse
import string
import hashlib


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
      
    def post(self):
      raise web.HTTPError(405, 'Currently using GET method.')

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
      is_counter = self.get_argument('counter', default='false', strip=True)
      is_public = self.get_argument('is_public', default='false', strip=True)
      uploaded_file = self.request.files.get('file', [])[0] if self.request.files.get('file', None) else None
      
      entity = db.Entity(user_locale=self.get_user_locale())
      if entity_id:
          property_id = entity.set_property(entity_id=entity_id, property_definition_keyname=property_definition_keyname, value=value, property_id=property_id, uploaded_file=uploaded_file)    
          self.write({
                      'property_id':property_id
          })
      else:
          raise web.HTTPError(400, 'Entity ID required')
      
          
    def post(self):
      raise web.HTTPError(405, 'Currently using GET method.')

class Auth (myRequestHandler,auth.OAuth2Mixin):
    """
    API authentication function.
    """
    
    @web.asynchronous
    def get(self,provider):

        key = self.settings['facebook_api_key']
        secret = self.settings['facebook_secret']
        self_url = self.request.protocol + '://' + self.request.host + '/auth/' + provider
        
        # initial step to gain code
        if not self.get_argument('code', None):
            return self.redirect(
                                 'https://www.facebook.com/dialog/oauth?client_id=%(id)s&redirect_uri=%(redirect)s&scope=%(scope)s&state=%(state)s'
                                 % {
                'id':       key,
                'redirect': self_url,
                'scope':    email,
            })
        
        # erroneous response from code gaining process
        if self.get_argument('error',None):
            raise web.HTTPError(401,'User declined authorization')
        
        # fetch access token using the gained code
        httpclient.AsyncHTTPClient().fetch(
            'https://graph.facebook.com/oauth/access_token',
            method = 'POST',
            headers = {'Content-Type': 'application/x-www-form-urlencoded'},        
            body = urllib.urlencode({
                'client_id' : key,
                'client_secret' : secret,
                'redirect_uri' : self_url,
                'code' : self.get_argument('code',None),
                'grant_type' : 'authorization_code'
            }),
            callback = self._got_token,
        )

    @web.asynchronous
    def _got_token(self,response):
        access_token = urlparse.parse_qs(response.body)['acces_token']
                
        httpclient.AsyncHTTPClient().fetch(
            'https://graph.facebook.com/me?access_token=%(token)s'
                %  {'token': access_token },
            callback = self._got_user
        )
        
    @web.asynchronous
    def _got_user(self,response):
        user = json.loads(response.body)
        LoginUser(self,{
            'provider' : 'facebook',
            'id' : user.setdefault('id'),
            'email' : user.setdefault('email'),
            'name' : user.setdefault('name'),
            'picture' : 'http://graph.facebook.com/%s/picture?type=large' % user.setdefault('id', ''),
        })
        
        
def Login(handler, user):
    """
    Starts session. Creates new user.

    """
    session_key = ''.join(random.choice(string.ascii_letters + string.digits) for x in range(32)) + hashlib.md5(str(time.time())).hexdigest()
    user_key = hashlib.md5(handler.request.remote_ip + handler.request.headers.get('User-Agent', None)).hexdigest()

    db.User().create(
        provider    = user['provider'],
        id          = user['id'],
        email       = user['email'],
        name        = user['name'],
        picture     = user['picture'],
        language    = handler.settings['default_language'],
        session     = session_key+user_key
    )

    handler.set_secure_cookie('session', str(session_key))
    
 
class Logout(myRequestHandler):
    def get(self):
        self.clear_cookie('session')
    
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
    ('/auth', Auth),
]
