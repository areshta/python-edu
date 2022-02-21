import os

def tmp_db_path():
    return os.path.dirname(os.path.realpath(__file__)) + '/example.db'

#test
if __name__ == '__main__':
    print( tmp_db_path() )