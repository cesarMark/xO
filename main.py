import os
import random
def displayMat(mat): #Function that displays the matrix
    for(i) in range(0,3):
         for(j) in range(0,3):
             print("|",matrix[i][j],end=" |")
         print("")
         print("________________")

#This function counts if one of the players won the game by checking if the whole row/column/diagonal is full
def checkWin(mat):
    for(i) in range(0 , 3):
        countXRow = 0
        countXDiagLeft = 0
        countORow = 0
        countODiagLeft = 0
        countXDiagRight = 0
        countODiagRight = 0
        countOCol = 0
        countXCol = 0
        for(j) in range(0 , 3):
            if matrix[j][j] == 'X':
                countXDiagLeft += 1
            if matrix[j][2-j] == 'X':
                countXDiagRight += 1
            if matrix[j][2-j] == 'O':
                countODiagRight += 1
            if matrix[j][j] == 'O':
                countODiagLeft += 1
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
        if countXDiagRight == 3:
            return True
        if countODiagRight == 3:
            return False
        if countXDiagLeft == 3:
            return True
        if countXCol == 3:
            return True
        if countORow == 3:
            return False
        if countODiagLeft == 3:
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
flag = 1
matrix = ([['_','_','_'],
           ['_','_','_'],
           ['_','_','_']])
while(flag > 0): #Flag is defined as the sequence of the game 
    os.system('cls')
    displayMat(matrix)
    print("Input the coordinates [row] (space) [column]")
    x, y = map(int, input().split())
    if x > 2 or x < 0 or y > 2 or y < 0 or matrix[x][y] == 'O' or matrix[x][y] == 'X': #One of the tests that makes sure that the player didn't input any wrong coordinates
        continue
    matrix[x][y] = 'X'
    if checkWin(matrix) == True: #Checks if the player won
         os.system('cls')
         displayMat(matrix)
         flag = 0
         print("CONGRATZ! YOU WON!")
    computerMove(matrix)
    if checkWin(matrix) == False: #The false reperesents the computer and if the function will return false than the computer won
        os.system('cls')
        displayMat(matrix)
        print("YOU LOST :( , TRY AGAIN")
        flag = 0