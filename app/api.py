from helper import *
from db import Entity

class Search ():
    """
    API search for entities function.
    
    """
    def get(self):
        print "Hello search!";
        # TODO rest
class Open ():
    """
    API open entity function.
    Needs entity ID.
    TODO MAYBE needs public/non-public???
    """
    def get(self):
        entity = db.Entity(user_locale=self.get_user_locale())
        
        self.write(entity.get(entity_id=self.get_argument('id'), limit=1, full_definition=True, only_public=False))
        self.write("Open: Done.\n")
class Add (myRequestHandler):
    """
    API add entity function.
    Needs entity ID and parent ID.
    """
    def get(self):
        self.write("Add: 1\n");
        
        entity = db.Entity(user_locale=self.get_user_locale())
        
        self.write("Add: 2\n")
        
        entity_id = entity.create(entity_definition_keyname=self.get_argument('id'), parent_entity_id=('parent_id'))
        
        self.write("Add: 3. Done.\n")
class Edit ():
    """
    API edit entity function.
    
    """
    def get(self):
        print "Hello edit!";
        #TODO rest
        
        
handlers = [
    ('/add', Add),
]