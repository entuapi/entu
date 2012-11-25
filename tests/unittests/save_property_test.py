import unittest
import urllib
import sys
from sqlalchemy import *

"""
Test for controlling validity of property creating.

--HELP
How to use:
1) Firstly, create text file. This text file will be used to read 
    values that you want to give, so please use
    default structure of content, otherwise test fails.
    Put this line into your text file (to the first line):
    
    entity_id:,property_definition_keyname:,value:,public:,file:
    
    Now simply put your values to the appropriate places. If you do not want to
    give any value, you can just remove it. Do not use quotes for values with String type.
    CONTROL THAT THERE ARE NO EXTRA SPACES USED!
    Example: 
    entity_id:3,property_definition_keyname:library-name,value:Ester
    
2) Then run:
    python save_property_test.py ['text_file.txt']
    Example:
    python save_property_test.py propertyToSave.txt

--NEED TO KNOW
['entity_id'] and ['property_definition_keyname'] are mandatory
['value'], ['public'] and ['file'] are optional

$entity_id = (int)
$property_definition_keyname = (string)
$value = *
$public = [(true)|(false)]
$file = (string)

"""



# Arguments
textFile = None

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

def getArgs():
    file = open(txtFile, 'r')
    entries = map(lambda entry: entry.rstrip('\n').split(','), file.readlines())
    query_args = {}
    for value in entries[0]:
        attribute = value.split(':')
        try:
            query_args[attribute[0]] = int(attribute[1])
        except ValueError:
            query_args[attribute[0]] = attribute[1]
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
       encoded_args = urllib.urlencode(query_args)
       expected_response = '{"property_id": %s}' % str(self.lastId + 1)           
       actual_response = urllib.urlopen("%s?%s" % (self.url, encoded_args)).read()
       self.assertEqual(expected_response, actual_response)
       
if __name__ == "__main__":
    txtFile = getValue(1)    
    if not txtFile:
        print 'Error: No text file given!'
    else:
        unittest.main(argv=[sys.argv[0]])
