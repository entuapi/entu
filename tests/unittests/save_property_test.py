import unittest
import urllib
import sys
from sqlalchemy import *

"""
Test for controlling validity of property creating.

How to use:
python save_and_change_property_test.py ['entity_id'] ['property_definition_keyname'] ['value']

! Where
['entity_id'] and ['property_definition_keyname'] are mandatory
['value'] is optional

EXAMPLE:
python save_property_test.py 3 library-name Ester
"""

#Arguments
entityId = None
propertyDefinition = None
value = None

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

def getArgs():
       query_args = {}
       query_args['entity_id'] = entityId
       query_args['property_definition_keyname'] = propertyDefinition
       return query_args

def getValue(argIndex):
       if argIndex < len(sys.argv):
           return sys.argv[argIndex]
       else:
           return None  

class TestSaveProperty(unittest.TestCase):
    def setUp(self):
       self.url = 'http://ec2-54-247-135-135.eu-west-1.compute.amazonaws.com:3307/save_property'
       self.lastId = getLastId()
       
    def test_changeExistingProperty(self):
       query_args = getArgs()
       if value:
           query_args['value'] = value
       encoded_args = urllib.urlencode(query_args)
       expected_response = '{"property_id": %s}' % str(self.lastId + 1)           
   
       actual_response = urllib.urlopen("%s?%s" % (self.url, encoded_args)).read()
       self.assertEqual(expected_response, actual_response)
       
if __name__ == "__main__":
   entityId = getValue(1)
   propertyDefinition = getValue(2)
   value = getValue(3)    
   if not entityId:
       print 'Error: No entity id given!'
   elif not propertyDefinition:
       print 'Error: No property definition keyname given!'
   else:
           unittest.main(argv=[sys.argv[0]])
