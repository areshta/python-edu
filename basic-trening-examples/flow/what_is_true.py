#Python-3 "What is True" example

def lie_detector(arg):
    if(arg):
        print("True")
    else:
        print("False")

lie_detector(True)          # True
lie_detector(5)             # True
lie_detector("False")       # True 
lie_detector([1,2,3])       # True
lie_detector(lie_detector)  # True

lie_detector(False)         # False
lie_detector(None)          # False
lie_detector(0)             # False
lie_detector("")            # False
lie_detector([])            # False
lie_detector(not True)      # False

lie_detector( 3 > 2 and 3 <5) # True
lie_detector( "abc" == "abc") # True

a = [1]; b = [1]; c = [1, -100]; d = [-1, 100]
lie_detector(a == b)    # True
lie_detector(c > a)     # True
lie_detector(d > a)     # False



