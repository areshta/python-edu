#Python3. File text output example

print("\n*** Reading txt file and printing to console example ***\n")

f = open("j_b.txt","r")
txt = f.read()
f.close()

print(txt)

