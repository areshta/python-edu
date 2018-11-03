#Python3. File text output example

print("\n*** Operations with file using 'with' statement example ***\n")

fname = "j_b.txt"

#reading lines to the list
with open(fname,"r") as f:
    lines = f.readlines()    

#example of output without format
print("Number of lines in " + fname + " = " + str(len(lines)) + "\n" )

#pay attention 'ln = ln.funtion()'. The string will not change without assigment
for ln in lines:
    ln = ln.strip() #remove end of lines symbol
    print(ln)

