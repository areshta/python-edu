import random
# attention! 
# input coordinates as b7 has (symbol col, number row) format
# storing coordinates have traditional (number row, number col) format
# inside row coordinates is reversed row index is 0..7 when input raw is 8 .. 1
# so, a1 chess coordinate is matrix[7][0]

class Figure:
    def __init__(self,row,col,c) -> None:
        self.col = col
        self.row = row
        self.color = c

    def is_valid_step(self, r2,c2):
        print("Valdation is not implemented yet for this figure")
        return True

class Bishop(Figure):
    def __init__(self,row,col,c) -> None:
        Figure.__init__(self,row,col,c)
        self.sym = self.color+'B'

    def is_valid_step(self, r2,c2):
        if abs(self.row - r2) == abs(self.col - c2) :
            return True
        else:
            print("Invalid step for Bishop. Please try again.")

class Rook(Figure):
    def __init__(self,row, col,c) -> None:
        Figure.__init__(self,row, col,c)
        self.sym = self.color+'R'    
    
    def is_valid_step(self, r2,c2):
        is_valid = True
        if (self.row == r2) or (self.col == c2) :
            return True
        else:
            print("Invalid step for Rook. Please try again.")
    
class Empty(Figure):
    def __init__(self,row, col,c) -> None:
        Figure.__init__(self,row, col,c)
        self.sym = '..'    

class Chess: 
    def __init__(self) -> None:
        self.matrix =[[Empty(j,i,'W') for j in range(8)] for i in range(8)]
        self.fig_num = 10
        self.generate()
    
    def output(self, title):
        print("\n\n", title, "\n")
        #print('       0   1   2   3   4   5   6   7')
        #title = '       a   b   c   d   e   f   g   h'
        title = '   a   b   c   d   e   f   g   h'
        print(title)
        for i in range(8):
            #print(i, '|', 7-i+1 ,' ',end='')
            print(7-i+1 ,' ',end='')
            for j in range(8):
                print(self.matrix[i][j].sym,' ',end='')
            print('\n')
        print(title)

    def generate(self):
        step = 0
        while(step < self.fig_num):
            col = random.randrange(0,7)
            row = random.randrange(0,7)
            if self.matrix[row][col].sym == Empty(row, col,'W').sym:
                color = random.choice(['B','W'])
                self.matrix[row][col] = random.choice([Bishop(row, col,color),Rook(row, col,color)])
                step += 1
    
    def test_begin(self, row, col):
        if self.matrix[row][col].sym == Empty(row, col,'W').sym: 
            print("Source cell is empty. Please try again")
            return False
        return True

    def test_end(self, row, col):
        if self.matrix[row][col].sym != Empty(row, col,'W').sym: 
            print("Target cell is busy. Please try again")
            return False
        return True

    def test_is_valid_for_figure(self, i1, j1, i2, j2):
        return self.matrix[i1][j1].is_valid_step(i2,j2)

    def step(self, r1, c1, r2, c2):
        # step is swap of figure and empty cell
        self.matrix[r1][c1], self.matrix[r2][c2] = self.matrix[r2][c2], self.matrix[r1][c1]        

class Inp:
    def __init__(self) -> None:
        self.j1 = None
        self.i1 = None 
        self.j2 = None
        self.i2 = None 

    def get(self):

        while True:
            cmd = ''
            cmd = input('Enter your step (example a6-c6) : ')
            if self.parse_coord(cmd):
                break
        return self.i1, self.j1, self.i2, self.j2

    def x_to_index(self, sym):
        return ord(sym)- ord('a')

    def y_to_index(self, sym):
        return 8-int(sym) # y is reversed. 8 -> 0, 1->7

    def parse_coord(self,cmd):
        self.j1, self.i1 = self.x_to_index(cmd[0]), self.y_to_index(cmd[1])  
        self.j2, self.i2 = self.x_to_index(cmd[3]), self.y_to_index(cmd[4]) 
        if self.i1 in range (0,8) and self.j1 in range (0,8) and self.i2 in range (0,8) and self.j2 in range (0,8):
            return True
        print('command ', cmd, ' is invalid. Please try again.')
        return False

#Begin is here
            
chess = Chess()
chess.output("Generated field")
inp = Inp()
i1, j1, i2, j2 = -1, -1, -1, -1
while True:
    i1, j1, i2, j2 = inp.get()
    if chess.test_begin(i1,j1):            
        #print("inside: ", i1, j1, i2, j2)
        if chess.test_end(i2,j2):
            if chess.test_is_valid_for_figure(i1, j1, i2, j2):            
                break        
chess.step(i1, j1, i2, j2)
chess.output("Field after step")
