"""
*    test_suit_file layout:
*        id{separator}query{separator}response
*
*    Example (suit1):
*        1>>http://www.example.com/search?id=5>>Example_nr_5
*        2>>http://www.getFriends.com/get?name=Igor>>{'name':'Igor Tolstoi','tel':'523709617'}
*
*    calling http_test:
*        python http_test.py test_suit_file1 test_suit_file2 .. test_suit_fileN {separator}
*
*    Example:
*        python http_test.py suit1 '>>'
*
*
*    // To try editing property of entity: set conf_file='testsuits/edit_property.conf' and then run
*        python http_test.py testsuits/edit_property '>>'
*
"""

import urllib
import sys
from time import gmtime, strftime

conf_file = 'http_test.conf'

output_name = strftime("archive/test_%Y-%m-%d___%H-%M-%S")
output = open(output_name, 'w')

output.write("Failed at:\n\n- - - - - - - - - - - - - - - - - - -\n\n")

failures = 0

handler_to_method = {}

config = open(conf_file, 'r')
config_entries = map(lambda entry: entry.rstrip('\n').split(':'),config.readlines())

for entry in config_entries:
    handler_to_method[entry[0]] = entry[1]

for file_name in sys.argv[1:-1]:
    input = open(file_name,'r')
    line = input.readline().rstrip('\n')

    while line:
        id,query,expected_response = line.rstrip('\n').split(sys.argv[-1])
        
        # find handler name        
        handler_start_idx = query.rfind('/')+1
        handler_end_idx = query.find('?') if '?' in query else None
        
        handler = query[handler_start_idx:handler_end_idx]
        
        # find handler's server-implemented HTTP method
        method = handler_to_method[handler]
        
        # parse arguments
        query_args = {}
        
        if handler_end_idx != None:
            for arg_pair in query[handler_end_idx + 1:].split('&'):
                arg,val = arg_pair.split('=')
                query_args[arg] = val
            
        
        encoded_args = urllib.urlencode(query_args)
        url = query[:handler_end_idx]
        
        actual_response = urllib.urlopen(url, encoded_args).read() if method == 'POST' else urllib.urlopen("%s?%s"%(url,encoded_args)).read()
        
        
        if actual_response != expected_response:
            failures += 1
            output.write("File : %s\nID : %s\nQuery : %s\n\nExpected : %s\n     Got : %s\n\n- - - - - - - - - - - - - - - - - - -\n\n"%(file_name,id,query,expected_response,actual_response))
        
        line = input.readline()

    input.close()

output.close()
            
if failures == 0:
    print "\nSUCCESS!\n"
else:
    print "\nFAILURE - consult archive/%s\n"%output_name