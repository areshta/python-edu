# Write a Python program that pings localhost. Use os and subprocess
# modules. Save command output.

from codecs import ignore_errors
import os
import sys
import subprocess as sp

result = sp.run(['ping', 'localhost'], stdout=sp.PIPE).stdout.decode('cp866')


#result = result.encode('cp1251')
#result = result.decode('utf-8', ignore_errors = True)
#print(type(result))

print(result)