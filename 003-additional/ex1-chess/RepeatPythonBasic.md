# Repeat Python basic

As user I want emulated next chess functionality:
1. Set to the chess board 10 random figures of Bishop and Rook.
2. Move a figure from one place to other according restrictions:
    * Destination cell must be empty
    * Bishop and Rook must moving according theirs rules
3. Interface: console input/output
4. Input format: <source_call><source_row>-<distant_call><distant_row>
    example: a1-b4
5. Only one step is executing by run of the application
6. Chess board is printed before step and after step

Output example:

```
 Generated field

   a   b   c   d   e   f   g   h
8  ..  ..  ..  ..  ..  WB  WB  ..

7  ..  ..  ..  ..  ..  BB  ..  ..

6  ..  ..  ..  WB  ..  ..  ..  ..

5  WR  WB  ..  ..  ..  ..  WB  ..

4  ..  ..  ..  WB  ..  ..  ..  ..

3  ..  ..  ..  ..  ..  ..  ..  ..

2  BB  ..  ..  ..  BR  ..  ..  ..

1  ..  ..  ..  ..  ..  ..  ..  ..

   a   b   c   d   e   f   g   h
Enter your step (example a6-c6) : e2-e7


 Field after step

   a   b   c   d   e   f   g   h
8  ..  ..  ..  ..  ..  WB  WB  ..

7  ..  ..  ..  ..  BR  BB  ..  ..

6  ..  ..  ..  WB  ..  ..  ..  ..

5  WR  WB  ..  ..  ..  ..  WB  ..

4  ..  ..  ..  WB  ..  ..  ..  ..

3  ..  ..  ..  ..  ..  ..  ..  ..

2  BB  ..  ..  ..  ..  ..  ..  ..

1  ..  ..  ..  ..  ..  ..  ..  ..

```

Tasks :
1. Generate chess field with 10 figures (Bishops, Rooks) in random positions
and display the chess board
2. Implement step from any cell to any cell without verification. Coordinates have to be input using console.
3. Implement next verification: Rook moves along rows and columns, Bishop moves along diagonals ignoring other figures.
4. Implement next validation: all moves are done according chess rules.

