#Python 3. Try-catch example

fn = input("Filename (a.txt could be OK): ")

try:
    f = open(fn,"r")
    txt = f.read()
    f.close()
except Exception: 
    print("File " + fn + " reading error!")
else:
    print(txt)
finally:
    if 'f' in locals():
        f.close()

