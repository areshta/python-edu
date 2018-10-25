#Python-3 Boolean example
arg1 = (False, True)
arg2 = (False, True)

print("Truth table: \n")
print("{:-^30}".format(""))
print("! arg1 ! arg2 !!  and !  or  !")
print("{:-^30}".format(""))

format_str = "!{:^6}!{:^6}!!{:^6}!{:^6}!\n"
str1 = format_str.format(arg1[0],arg2[0],arg1[0] and arg2[0], arg1[0] or arg2[0]) 
str2 = format_str.format(arg1[0],arg2[1],arg1[0] and arg2[1], arg1[0] or arg2[1]) 
str3 = format_str.format(arg1[1],arg2[0],arg1[1] and arg2[0], arg1[1] or arg2[0]) 
str4 = format_str.format(arg1[1],arg2[1],arg1[1] and arg2[1], arg1[1] or arg2[1]) 
print(str1 + str2 +str3 + str4)

