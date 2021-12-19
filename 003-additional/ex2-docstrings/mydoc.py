"""This is a module doc string.
    You could try to use python command line:
    C:\>python
    >>> import mydoc
    >>> help(mydoc)
"""

def doc_str_example1(param1, param2):
    """Example of doc string for doc_str_example1.
        param1 is the first argument,
        param2 is the second argument,
        returnes nothing.
    """
    pass

class Some_class:
    """This is class doc string"""

    def class_fun():
        """This is class function doc string"""
if __name__ == "__main__":
    print("Extracting string using __doc__:")
    print(__doc__)
    print(doc_str_example1.__doc__)

    print("\nUsing help:")
    help(doc_str_example1)
    help(Some_class)
    help(Some_class.class_fun)
