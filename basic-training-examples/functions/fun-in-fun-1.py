#Python 3. Call inside function

def wall():
    print("I have insider function")
    def insider(msg):
        print("Output from insider:\n"+msg)
    return insider

hiden = wall()
hiden("Ops! You can call me!")
