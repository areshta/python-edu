# Python-3 Comment/Quotation/Statements example

str1 = \
"""This is
using several lines
example"""

print(
str1
) # statement can take one line or more

str2 = '\nWe can use "double" quotes inside \'single quotes\''  # \' will ouput as '
str3 = "\nand ' quotes inside other\n"							# \n - next line symbol
print( str2 + \
str3) # back slash can contnue statement

print("We can ", end = '')
print("print some words by different prints ", end = '')
print("in the same line")

a = 5; b = a**2; c = b+3; print("Some statements in one line. c = ", c)

print(r"Raw string \n prints 'as is' \n escapes are ignored")

