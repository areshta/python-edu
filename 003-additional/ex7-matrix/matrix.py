# Exercise 7. Multiplication with scalar is not implemented: trivial as add

class MyMatrix(list):
    
    def __init__(self, nrow, ncol) -> None:
        self.nrow = nrow
        self.ncol = ncol
        for i in range(nrow):
            super().append([0 for i in range(ncols)])
    
    def print(self):
        print(self.__str__())

    def __str__(self) -> str:
        txt = ''
        for i in range(self.nrow):
            for j in range(self.ncol):
                txt += str(super().__getitem__(i)[j]) + ' '
            txt += '\n'
        return txt

    def __repr__(self):
        return 'MyMatrix(nrow, ncol)'

    def __index__(self, row):
        return super().__getitem__(row)

    def __add__(self, x):
        return self._add(x)

    def __radd__(self, x):
        return self._add(x)
    
    def _add(self, x):
        for i in range(self.nrow):
            for j in range(self.ncol):
                super().__getitem__(i)[j] += x
        return self

    def __bool__(self):
        sum = 0
        for i in range(self.nrow):
            for j in range(self.ncol):
                sum += super().__getitem__(i)[j]
        return bool(sum)


nrows = 3
ncols = 4

Matr = MyMatrix(nrows, ncols)
Matr.print()
print("Matr has non-zero elements:", bool(Matr))

print("=== Init cells with nums in format <row><col> starts from 1 === ")
for row in range(nrows):
    Matr[row] = [ (row+1)*10 + col+1 for col in range(ncols) ]
Matr.print()

print("=== add scalar to matrix === ")
Matr = Matr + 2
print(Matr)

print("=== add matrix to scalar === ")
Matr = 2 + Matr
Matr.print()
print("Matr has non-zero elements:", bool(Matr))

