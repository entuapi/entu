import unittest
import urllib
import sys
from sqlalchemy import *

"""
Test for controlling validity of entity saving.
How to use:
python save_entity_test.py ['entity_definition_keyname'] ['parent_id']

! Where ['entity_definition_keyname'] is mandatory and ['parent_id'] is optional

--HELP
How to use:
1) Firstly, create text file. This text file will be used to read 
    values that you want to give, so please use
    default structure of content, otherwise test fails.
    Put this line into your text file (to the first line):
    
    entity_definition_keyname:,session_key:,parent_entity_id:,public:
    
    Now simply put your values to the appropriate places. If you do not want to
    give any value, you can just remove it. Do not use quotes for values with String type.
    CONTROL THAT THERE ARE NO EXTRA SPACES USED!
    Example: 
    entity_definition_keyname:library,session_key:XxX123YyY456,parent_entity_id:3,public:true
    
2) Then run:
    python save_entity_test.py ['text_file.txt']
    Example:
    python save_entity_test.py entityToSave.txt

--NEED TO KNOW
['entity_definition_keyname'] and ['session_key'] are mandatory
['parent_entity_id'] and ['public'] are optional


$entity_definition_keyname = (string)
$session_key = (string)
$parent_entity_id = (int)
$public = true/false (default true)
"""

# Arguments
textFile = None

def getLastId():
        db = create_engine('mysql://root:1234@localhost/entudb', echo=False)
        metadata = MetaData(db)
        entity = Table('entity', metadata, autoload=True)
        s = entity.select(entity.c.id > 0)
        ids = []
        rs = s.execute()
        for row in rs:
            ids.append(row.id)
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
        
class TestSaveEntity(unittest.TestCase):
    def setUp(self):
        self.url = 'http://ec2-54-247-135-135.eu-west-1.compute.amazonaws.com:3307/api/save_entity'       
        self.query_args = getArgs()
        self.expected_response = '{"entity_id": %s}' % (getLastId() + 1) 
    def test_saveEntity(self):
        encoded_args = urllib.urlencode(self.query_args)            
        actual_response = urllib.urlopen("%s?%s" % (self.url, encoded_args)).read()
        self.assertEqual(self.expected_response, actual_response)
    
    def test_saveEntityWithNoDefinition(self):
        self.query_args['entity_definition_keyname'] = None
        encoded_args = urllib.urlencode(self.query_args)
        actual_response = urllib.urlopen("%s?%s" % (self.url, encoded_args)).read()
        self.assertNotEqual(self.expected_response, actual_response)
        
if __name__ == "__main__":
    txtFile = getValue(1)    
    if not txtFile:
        print 'Error: No text file given!'
    else:
        unittest.main(argv=[sys.argv[0]])
