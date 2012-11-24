REQUIREMENTS FOR RUNNING TESTS
These tests use SQLAlchemy toolkit (to install it on Ubuntu use: easy_install SQLAchemy)
and MySQL database (where user:root, password:1234, host:localhost, port:default, database:entudb
+ tables which are described in folder 'sql').

HOW TO RUN (more information in according test file)
python save_entity_test.py ['entity_definition_keyname'] ['parent_id']
python save_and_change_property_test.py ['entity_id'] ['property_definition_keyname'] ['value']
python save_and_change_property_test.py ['entity_id'] ['property_id'] ['property_definition_keyname'] ['value']

OUTPUT
Returns OK if test was successful, otherwise ERROR message

BUGS
Tests need their own database or correct database cleaning after test execution. 
