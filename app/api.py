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
    
    """
    def get(self):
        print "Hello open!";
                
        # TODO rest
class Add (myRequestHandler):
    """
    API add entity function.
    
    """
    def get(self):
        self.write("Hello add!\n");
        
        entity = db.Entity(user_locale=self.get_user_locale())
        
        self.write("natuke tehtud\n")
        
        entity_id = entity.create(entity_definition_keyname=self.get_argument('id'))
        
        self.write("olen tubli\n")
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