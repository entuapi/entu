import unittest
import urllib
from sqlalchemy import *

def getLastId():
        db = create_engine('mysql://root:1234@localhost/entudb', echo=False)
        metadata = MetaData(db)
        property = Table('property', metadata, autoload=True)
        s = property.select(property.c.id > 0)
        ids = []
        rs = s.execute()
        for row in rs:
            ids.append(row.id)
        # Return current maximum property id
        return max(ids)

def getProperties(self):
    properties = '[{"entity_id":3,"property_definition_keyname":"library-name","value":"UT"},{"entity_id":3,"property_definition_keyname":"library-name","value":"Ester"}]'
    return properties
  

class TestSaveProperty(unittest.TestCase):
    def setUp(self):
        self.url = 'http://ec2-54-247-135-135.eu-west-1.compute.amazonaws.com:3307/save_property'
        self.lastId = getLastId()
        
    def test_changeExistingProperties(self):
        # Get arguments that are needed for changing existing property
        properties = getProperties(self)
        query_args = {}
        query_args['properties'] = properties
        encoded_args = urllib.urlencode(query_args)
        expected_response = "[%s, %s]" % (str(self.lastId + 1), str(self.lastId + 2))          
    
        actual_response = urllib.urlopen("%s?%s" % (self.url, encoded_args)).read()
        self.assertEqual(expected_response, actual_response)
        
if __name__ == "__main__":
    unittest.main()
