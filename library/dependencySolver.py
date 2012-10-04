from distutils.sysconfig import get_python_lib
import os

input = open('entu.pth','r')
output = open('%s/entu.pth'%get_python_lib(),'w')

lines = input.readlines()
input.close()

localDir = os.path.dirname(os.path.realpath(__file__))

for line in lines:
    output.write("%s%s"%(localDir,line))
    
output.close()