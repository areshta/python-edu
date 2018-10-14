#Python-3 strings example

print("\n*** Quotes example. ***\n")

str1 = "char 'a'. str1 can include single quotes"
str2 = 'name "Some". str2 can include double quotes'
str3 = """  
        Triple quotes.
        str3 can include
        several lines and other qoutes"""

print(str1)
print(str2)
print(str3)
           
print("\n*** Escape characters and row strings example. ***\n")

str1 = "It is Windows path: d:\\Program Files\\some program"
str2 = "Lines and tabs:\n\tLine 1\n\tLine 2\n\tLine 3"
str3 = r"No escape, all as is: \\, \n, \t"

print(str1)
print(str2)
print(str3)

print("\n*** F-strings. Strings with place holders  ***\n")

name = "John"
age = 12
print (f"{name} is {age} years old")
