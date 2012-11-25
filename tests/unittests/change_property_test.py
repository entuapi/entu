import unittest
import urllib
import sys
from sqlalchemy import *

"""

Test for controlling validity of property changing.
NB! BE SURE YOU GIVE ID OF PROPERTY YOU WANT TO CHANGE!

--HELP
How to use:
1) Firstly, create text file. This text file will be used to read 
    values that you want to give, so please use
    default structure of content, otherwise test fails.
    Put this line into your text file (to the first line):
    
    entity_id:,property_definition_keyname:,property_id:,value:,public:,file:
    
    Now simply put your values to the appropriate places. If you do not want to
    give any value, you can just remove it. Do not use quotes for values with String type.
    Example: 
    entity_id:3,property_definition_keyname:library-name,property_id:15
    
2) Then run:
    python change_property_test.py ['text_file.txt']
    Example:
    python change_property_test.py propertyToChange.txt

--NEED TO KNOW
['entity_id'], ['property_id'] and ['property_definition_keyname'] are mandatory
['value'], ['public'] and ['file'] are optional

$entity_id = (int)
$property_definition_keyname = (string)
$property_id = (int)
$value = *
$public = [(true)|(false)]
$file = (string)

"""

# Arguments
txtFile = None

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
       
    def test_changeExistingProperty(self):
       query_args = getArgs()
       encoded_args = urllib.urlencode(query_args)
       expected_response = '{"property_id": "%s"}' % query_args['property_id']           
   
       actual_response = urllib.urlopen("%s?%s" % (self.url, encoded_args)).read()
       self.assertEqual(expected_response, actual_response)
       
if __name__ == "__main__":
    txtFile = getValue(1)    
    if not txtFile:
        print 'Error: No text file given!'
    else:
        unittest.main(argv=[sys.argv[0]])
