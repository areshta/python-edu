import os

path_src = '/home/alex/tmp/test_fldr_1'
path_dist = '/home/alex/tmp/test_fldr_2'

# import os
#
# path = 'c:\\projects\\hc2\\'
#
# folders = []
#
# # r=root, d=directories, f = files
# for r, d, f in os.walk(path):
#     for folder in d:
#         folders.append(os.path.join(r, folder))
#
# for f in folders:
#     print(f)



def get_folder_list(path):

    files = []
    # r=root, d=directories, f = files
    for r, d, f in os.walk(path):
        for file in f:
            files.append(os.path.join(r, file))
    return files

def print_list(list):
    for el in list:
        print(el)


files_src = get_folder_list(path_src)
print_list(files_src)

files_dist = get_folder_list(path_src)
print_list(files_dist)

# if os.path.isfile(myfile):
#     os.remove(myfile)