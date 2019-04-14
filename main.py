import os
import random
#This function counts if one of the players won the game by checking if the whole row/column/diagonal is full
def checkWin(mat):
    for(i) in range(0 , 3):
        countXRow = 0
        countXDiag = 0
        countORow = 0
        countODiag = 0
        countOCol = 0
        countXCol = 0
        for(j) in range(0 , 3):
            if matrix[j][j] == 'X':
                countXDiag += 1
            if matrix[j][j] == 'O':
                countODiag += 1
            if matrix[i][j] == 'X':
                countXRow += 1
            if matrix[i][j] == 'O':
                countORow += 1
            if matrix[j][i] == 'X':
                countXCol += 1
            if matrix[j][i] == 'O':
                countOCol += 1
        if countXRow == 3:
            return True
        if countXDiag == 3:
            return True
        if countXCol == 3:
            return True
        if countORow == 3:
            return False
        if countODiag == 3:
            return False
        if countOCol == 3:
            return False
#This function implements the computer's move by picking 2 random coordinates and choosing it as long as its not been taken
def computerMove(mat):
    flag = 1
    while flag > 0:
        compRow = random.randint(0,2)
        compColumn = random.randint(0,2)
        if  matrix[compRow][compColumn] != 'O' and matrix[compRow][compColumn] != 'X':
             matrix[compRow][compColumn] = 'O'
             flag = 0
matrix = ([['_','_','_'],
           ['_','_','_'],
           ['_','_','_']])
flag = 1
while(flag > 0): #Flag is defined as the sequence of the game 
    os.system('cls')
    for(i) in range(0,3): #The nested loop will show up the matrix
         for(j) in range(0,3):
             print("|",matrix[i][j],end=" |")
         print("")
         print("________________")
    print("Input the coordinates [row] (space) [column]")
    x, y = map(int, input().split())
    if x > 2 or x < 0 or y > 2 or y < 0: #One of the tests that makes sure that the player didn't input any wrong coordinates
        continue
    if  matrix[x][y] == 'O' or matrix[x][y] == 'X':
        print("")
        print("*****Please try a different place where X or O are not located*****")
        print("")
        continue
    matrix[x][y] = 'X'
    computerMove(matrix)
    if checkWin(matrix) == True: #Checks if the player won
        print("CONGRATZ! YOU WON!")
        flag = 0
    elif checkWin(matrix) == False: #The false reperesents the computer and if the function will return false than the computer won
        print("YOU LOST :( , TRY AGAIN")
        flag = 0