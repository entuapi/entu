
import sys, subprocess, os
if len(sys.argv) != 3:
    print 'python starter.py #port_number #host_address\n\n Eg: python starter.py 3912 127.0.0.1\n'
    sys.exit()

ENVIRONMENT = '/home/kom/entu_env'

subprocess.call(['%s/bin/python'%ENVIRONMENT,'%s/app/main.py'%os.path.realpath(__file__)[:os.path.realpath(__file__).rfind('/')],'--logging=debug','--debug=True','--port=%s'%sys.argv[1],'--mysql_host=%s'%sys.argv[2],'--mysql_database=entudb','--mysql_user=entuapp','--mysql_password=0000'])

