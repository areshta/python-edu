# Write a Python program which takes two digits m (row) and n (column) as
# arguments(given from command line) and generates a two dimensional
# array. The element value in the i-th row and j-th column of the array
# should be i*j.

import argparse
parser = argparse.ArgumentParser()
parser.add_argument('--m', help='m rows', default = 4)
parser.add_argument('--n', help='n columns', default = 5)
args = parser.parse_args()

def create_matrix (m, n):
    return [[i*j for j in range(0,n)] for i in range(0,m)]
    
m = int(args.m)
n = int(args.n)

matrix = create_matrix(m,n)

for i in range(0, m):
    for j in range(0, n):
        print(matrix[i][j], end = " ")
    print()