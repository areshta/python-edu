#Python-3 regular expression example. Extract IP v4 adress

import re

print("\n*** Looking for IP example ***\n") 
text = """IP addresses are usually written and displayed in human-readable notations, 
such as 172.16.254.1 in IPv4, and 2001:db8:0:1234:0:567:8:1 in IPv6."""

print( "The sting includes IP = " + re.search(r'\d+\.\d+\.\d+\.\d+', text).group() )

print("\n*** Looking for cpp code example ***\n") 
paths = [
"/home/user/work/some_file.txt", 
"/var/log/code.cpp",
"/opt.cpp/set/set.a12",
"/optc/set/not_cpp",
"/cpp/set/other.cpp"
] 

for st in paths:
    sc = re.search(r'\w+\.cpp$', st) 
    if sc:
        print(st)
        print("File: ", sc.group())
  

