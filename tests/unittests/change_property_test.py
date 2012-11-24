import unittest
import urllib
import sys
from sqlalchemy import *

"""
Test for controlling validity of property changing.
NB! BE SURE YOU GIVE ID OF PROPERTY YOU WANT TO CHANGE!

How to use:
python change_property_test.py ['entity_id'] ['property_id'] ['property_definition_keyname'] ['value']

! Where
['entity_id'], ['property_id'] and ['property_definition_keyname'] are mandatory
['value'] is optional

EXAMPLE:
python change_property_test.py 3 6 library-name UT
"""

#Arguments
entityId=None
propertyId=None
propertyDefinition=None
value=None

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
       
    def test_changeExistingProperty(self):
       query_args = getArgs()
       query_args['property_id'] = propertyId
       query_args['value'] = value
       encoded_args = urllib.urlencode(query_args)
       expected_response = '{"property_id": "%s"}' % str(propertyId)           
   
       actual_response = urllib.urlopen("%s?%s" % (self.url, encoded_args)).read()
       self.assertEqual(expected_response, actual_response)
       
if __name__ == "__main__":
   entityId = getValue(1)
   propertyId = getValue(2)
   propertyDefinition = getValue(3)
   value = getValue(4)    
   if not entityId:
       print 'Error: No entity id given!'
   elif not propertyId:
       print 'Error: No property id given!'
   elif not propertyDefinition:
       print 'Error: No property definition keyname given!'
   else:
           unittest.main(argv=[sys.argv[0]])