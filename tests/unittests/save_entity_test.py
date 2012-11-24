import unittest
import urllib
import sys
from sqlalchemy import *

"""
Test for controlling validity of entity saving.
How to use:
python save_entity_test.py ['entity_definition_keyname'] ['parent_id']

! Where ['entity_definition_keyname'] is mandatory and ['parent_id'] is optional
"""
definition=None
prentId=None

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
        query_args = {}
        query_args['entity_definition_keyname'] = definition
        query_args['parent_id'] = parentId
        return query_args

def getValue(argIndex):
        if argIndex < len(sys.argv):
            return sys.argv[argIndex]
        else:
            return None
        
class TestSaveEntity(unittest.TestCase):
    def setUp(self):
        self.url = 'http://ec2-54-247-135-135.eu-west-1.compute.amazonaws.com:3307/save_entity'       
        self.encoded_args = urllib.urlencode(getArgs())
        lastId = getLastId()
        self.expected_response = '{"entity_id": %s}' % (lastId + 1)                
    def test_saveEntity(self):
        actual_response = urllib.urlopen("%s?%s" % (self.url, self.encoded_args)).read()
        self.assertEqual(self.expected_response, actual_response)

if __name__ == "__main__":
        definition=getValue(1)
	parentId=getValue(2)
	if not definition:
		print 'Error: No entity definition keyname given!'
	else:
		unittest.main(argv=[sys.argv[0]])