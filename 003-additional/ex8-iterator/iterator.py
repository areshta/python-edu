#  Implement an iterator with a user predicate. 
#  The predicate returns true if the current element can be returned 
#  by your iterator __next_() method

class MyIterator:
    def __init__(self,start,stop,step = 1):
        self.__stop = stop
        self.__step = step
        self.__current = start

    def get_predicate(self):
        # in this place current eq next value
        predicate = False
        if self.__current < self.__stop:
            predicate = True
        return predicate

    def __next__(self):
        while self.__current < self.__stop:
            result = self.__current
            self.__current += self.__step
            return result, self.get_predicate()
        else:
            raise StopIteration()

        
class MyRange:
    def __init__(self,start,stop,step = 1):
        self.__stop = stop
        self.__step = step
        self.__start = start
    def __iter__(self):
        return MyIterator(self.__start,self.__stop,self.__step)
    
#-----------------------------------
c = MyRange(1,10,2)

for (i, predicate) in c:
    print("value  = ", i, "   predicate next available = ", predicate)
