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
        #Return current maximum property id
        return max(ids)

#Just random values, that are present in current database
def getArgs():
    query_args = {}
    query_args['entity_id'] = 3L
    query_args['property_definition_keyname'] = 'library-name'
    return query_args
  

class TestSaveProperty(unittest.TestCase):
    def setUp(self):
        self.url = 'http://ec2-54-247-135-135.eu-west-1.compute.amazonaws.com:3307/save_property'
        self.lastId = getLastId()
        
    def test_saveNewProperty(self):
        #Get arguments that are needed for creating new property
        query_args = getArgs()
        query_args['value'] = 'Ester'
        encoded_args = urllib.urlencode(query_args)
        expected_response = '{"property_id": %s}' % str(self.lastId+1)    
        actual_response = urllib.urlopen("%s?%s" % (self.url, encoded_args)).read()
        self.assertEqual(expected_response, actual_response)
        
    def test_changeExistingProperty(self):
        #Get arguments that are needed for changing property which was just created 
        query_args = getArgs()
        query_args['property_id'] = self.lastId+1
        query_args['value'] = 'UT'
        encoded_args = urllib.urlencode(query_args)
        expected_response = '{"property_id": "%s"}' % str(self.lastId+1)           
    
        actual_response = urllib.urlopen("%s?%s" % (self.url, encoded_args)).read()
        self.assertEqual(expected_response, actual_response)
        
if __name__ == "__main__":
    unittest.main()
