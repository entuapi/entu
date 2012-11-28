import unittest
import urllib
import sys
import json
from sqlalchemy import *

"""

Test for controlling validity of creating many new properties at a time by giving them in list in JSON format.

--HELP
How to use:
1) Firstly, create text file. This text file will be used to read 
    values that you want to give, so please use
    default structure of content, otherwise test fails.
    In order to give values for one property entry 
    put this line into your text file (to the first line) (to add more properties just copy same text 
    into next lines of your file):
    
    entity_id:,property_definition_keyname:,value:,file:
    entity_id:,property_definition_keyname:,value:,file:
    ...
    entity_id:,property_definition_keyname:,value:,file:
    
    Now simply put your values to the appropriate places. If you do not want to
    give any value, you can just remove it. Do not use quotes for values with String type.
    CONTROL THAT THERE ARE NO EXTRA SPACES USED!
    Example: 
    entity_id:3,property_definition_keyname:library-name,value:Ester
    entity_id:5,property_definition_keyname:institution-name,value:UT
    ...
    entity_id:2,property_definition_keyname:person-user,value:example@entu.com
    
2) Then run:
    python add_properties_in_list_test.py ['text_file.txt']
    Example:
    python add_properties_in_list_test.py propertiesToAdd.txt

--NEED TO KNOW
['entity_id'], ['property_definition_keyname'] and ['session_key'] are mandatory
['value'] and ['file'] are optional

/***/

$session_key = 'dummysession' as default for tests

/***/

$entity_id = (int)
$property_definition_keyname = (string)
$session_key = (string)
$value = *
$file = (string)

"""

# Arguments
txtFile = None

def getPropertiesInJSON():
    file = open(txtFile, 'r')
    entries = map(lambda entry: entry.rstrip('\n').split(','), file.readlines())
    query_args = []
    for entry in entries:
        arg = {}
        for value in entry:
            attribute = value.split(':')
            arg[attribute[0]] = attribute[1]
        query_args.append(arg)
    return query_args, len(query_args)

def getValue(argIndex):
    if argIndex < len(sys.argv):
       return sys.argv[argIndex]
    else:
       return None 
   
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

def getProperties():
    properties, sum = getPropertiesInJSON()
    return json.dumps(properties), sum
  
def getExpectedResponse(lastId, sum):
    response = "["
    for i in range(1, sum + 1):
        if i == sum:
            response += str(lastId + i)
        else:    
            response += str(lastId + i) + ", "
    response += "]"  
    return response

class TestSaveProperty(unittest.TestCase):
    def setUp(self):
        self.url = 'http://ec2-54-247-135-135.eu-west-1.compute.amazonaws.com:3307/api/save_properties'
        self.lastId = getLastId()
        properties, self.sum = getProperties()
        self.query_args = {}
        self.query_args['properties'] = properties
        
    def test_changeExistingProperties(self):
        self.query_args['session_key'] = 'dummysession'
        encoded_args = urllib.urlencode(self.query_args)
        expected_response = getExpectedResponse(self.lastId, self.sum)
        actual_response = urllib.urlopen("%s?%s" % (self.url, encoded_args)).read()
        self.assertEqual(expected_response, actual_response)
        
if __name__ == "__main__":
    txtFile = getValue(1)    
    if not txtFile:
        print 'Error: No text file given!'
    else:
        unittest.main(argv=[sys.argv[0]])
