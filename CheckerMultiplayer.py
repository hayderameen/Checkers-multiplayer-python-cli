

def printMatrix(matrix):
    print ("\n\n")
    print ("-------------Checker Board-----------------")
    print ("\n")
    print (" 0 |  1  |  2  |  3  |  4  |  5  |  6  |  7 \n")
    print ("-------------------------------------------")
    for row in matrix:
        #print (" 1 | ")
        print ("  |  ".join(map(str,row)))
        print ("-------------------------------------------")
    print ("\n")
    print ("------------Checker Board Ends-------------")
    print ("\n\n")

# Initialize the checker Board
matrix = [[]]
matrix = [[' ' for x in range(8)] for y in range(8)]

no1 = [0, 2, 4, 6]
no2 = [1, 3, 5, 7]

for position in no1:
    matrix[0][position] = "X"
    matrix[2][position] = "X"
    matrix[6][position] = "O"
    
for position in no2:
    matrix[1][position] = "X"
    matrix[5][position] = "O"
    matrix[7][position] = "O"
    
printMatrix(matrix)

# Initialization of matrix ends here

# Checking moves of X and O

    # Checking moves of X Checkers

def moveXChecker():
    print ("X Turn: ")
    # Here x is row and y is column
    x = int(input("Enter row number: "))
    y = int(input("Enter column number: "))

    moveLeft = False
    moveRight = False
    cutLeft = False
    cutRight = False
    answer = " "
    cut = " "

    if (str(matrix[x][y]) == "X"):
        
        # Checking simple checker moves
        if (not y == 7 and not y == 0):
            if (str(matrix[x + 1][y + 1]) == " "):
                moveRight = True
            if (str(matrix[x + 1][y - 1]) == " "):
                moveLeft = True
        elif (y == 7):
            if (str(matrix[x + 1][y - 1]) == " "):
                moveLeft = True
        else:
            if (str(matrix[x + 1][y + 1]) == " "):
                moveRight = True
        
        
        # Checking cutting checker moves
        if (not y > 5 and not y < 2):
            if (str(matrix[x + 1][y + 1]) == "O" and not str(matrix[x + 2][y + 2]) == "O" and not str(matrix[x + 2][y + 2]) == "X"):
                cutRight = True
            if (str(matrix[x + 1][y - 1]) == "O" and not str(matrix[x + 2][y - 2]) == "O" and not str(matrix[x + 2][y - 2]) == "X"):
                cutLeft = True
        elif (y > 5):
            if (str(matrix[x + 1][y - 1]) == "O" and not str(matrix[x + 2][y - 2]) == "O" and not str(matrix[x + 2][y - 2]) == "X"):
                cutLeft = True
        else:
            if (str(matrix[x + 1][y + 1]) == "O" and not str(matrix[x + 2][y + 2]) == "O" and not str(matrix[x + 2][y + 2]) == "X"):
                cutRight = True

        if (any([cutLeft, cutRight])):
            moveLeft = False
            moveRight = False
           

        # If simple move rule was correct then...
        if (any([moveLeft, moveRight])):
            if (moveLeft):
                if (moveRight):
                    answer = input("Move left or right? Answer with R or L: ")
                    answer = answer.upper()
                else:
                    answer = "L"
            else:
                answer = "R"

        if (any([answer == "R", answer == "L"])):
            if (answer == "R"):
                matrix[x + 1][y + 1] = "X"
                matrix[x][y] = " "
                printMatrix(matrix)
            else:
                matrix[x + 1][y - 1] = "X"
                matrix[x][y] = " "
                printMatrix(matrix)
        
        # If cutting move rule was correct then...
        elif (any([cutLeft, cutRight])):
            if (cutLeft):
                if (cutRight):
                    answer = input("Move left or right? Answer with R or L: ")
                    answer = answer.upper()
                else:
                    answer = "L"
            else:
                answer = "R"

            if (any([answer == "R", answer == "L"])):
                if (answer == "R"):
                    matrix[x + 1][y + 1] = " "
                    matrix[x + 2][y + 2] = "X"
                    matrix[x][y] = " "
                    printMatrix(matrix)
                else:
                    matrix[x + 1][y - 1] = " "
                    matrix[x + 2][y - 2] = "X"
                    matrix[x][y] = " "
                    printMatrix(matrix)

            # In case there's one more checker to cut after this one
            if (not y > 5 and not y < 2):
                if (str(matrix[x + 1][y + 1]) == "O" and not str(matrix[x + 2][y + 2]) == "O" and not str(matrix[x + 2][y + 2]) == "X"):
                    cutRight = True
                if (str(matrix[x + 1][y - 1]) == "O" and not str(matrix[x + 2][y - 2]) == "O" and not str(matrix[x + 2][y - 2]) == "X"):
                    cutLeft = True
            elif (y > 5):
                if (str(matrix[x + 1][y - 1]) == "O" and not str(matrix[x + 2][y - 2]) == "O" and not str(matrix[x + 2][y - 2]) == "X"):
                    cutLeft = True
            else:
                if (str(matrix[x + 1][y + 1]) == "O" and not str(matrix[x + 2][y + 2]) == "O" and not str(matrix[x + 2][y + 2]) == "X"):
                    cutRight = True

        # If none of the moves were correct...
        else:
            print ("No Valid Moves !!! Try again....")
            moveXChecker()

        
    else:
        print ("Not a checker!")
        moveXChecker()

    # End of checking of moves of X Checker

    # Checking O Checker Moves

def moveOChecker():
    print ("O Turn: ")
    # Here x is row and y is column
    x = int(input("Enter row number: "))
    y = int(input("Enter column number: "))

    moveLeft = False
    moveRight = False
    cutLeft = False
    cutRight = False
    answer = " "
    cut = " "

    if (str(matrix[x][y]) == "O"):
        
        # Checking simple checker moves
        
        if (not y == 7 and not y == 0):
            if (str(matrix[x - 1][y + 1]) == " "):
                moveRight = True
            if (str(matrix[x - 1][y - 1]) == " "):
                moveLeft = True
        elif (y == 7):
            if (str(matrix[x - 1][y - 1]) == " "):
                moveLeft = True
        else:
            if (str(matrix[x - 1][y + 1]) == " "):
                moveRight = True
        
        # Checking cutting checker moves
        if (not y > 5 and not y < 2):
            if (str(matrix[x - 1][y + 1]) == "X" and not str(matrix[x - 2][y + 2]) == "X" and not str(matrix[x - 2][y + 2]) == "O"):
                cutRight = True
            if (str(matrix[x - 1][y - 1]) == "X" and not str(matrix[x - 2][y - 2]) == "X" and not str(matrix[x - 2][y - 2]) == "O"):
                cutLeft = True
        elif ( y > 5 ):
            if (str(matrix[x - 1][y - 1]) == "X" and not str(matrix[x - 2][y - 2]) == "X" and not str(matrix[x - 2][y - 2]) == "O"):
                cutLeft = True
        else:
            if (str(matrix[x - 1][y + 1]) == "X" and not str(matrix[x - 2][y + 2]) == "X" and not str(matrix[x - 2][y + 2]) == "O"):
                cutRight = True

        if (any([cutLeft, cutRight])):
            moveLeft = False
            moveRight = False
           

        # If simple move rule was correct then...
        if (any([moveLeft, moveRight])):
            if (moveLeft):
                if (moveRight):
                    answer = input("Move left or right? Answer with R or L: ")
                    answer = answer.upper()
                else:
                    answer = "L"
            else:
                answer = "R"

        if (any([answer == "R", answer == "L"])):
            if (answer == "R"):
                matrix[x - 1][y + 1] = "O"
                matrix[x][y] = " "
                printMatrix(matrix)
            else:
                matrix[x - 1][y - 1] = "O"
                matrix[x][y] = " "
                printMatrix(matrix)
        
        # If cutting move rule was correct then...
        elif (any([cutLeft, cutRight])):
            if (cutLeft):
                if (cutRight):
                    answer = input("Move left or right? Answer with R or L: ")
                    answer = answer.upper()
                else:
                    answer = "L"
            else:
                answer = "R"

            if (any([answer == "R", answer == "L"])):
                if (answer == "R"):
                    matrix[x - 1][y + 1] = " "
                    matrix[x - 2][y + 2] = "O"
                    matrix[x][y] = " "
                    printMatrix(matrix)
                else:
                    matrix[x - 1][y - 1] = " "
                    matrix[x - 2][y - 2] = "O"
                    matrix[x][y] = " "
                    printMatrix(matrix)
        
            # In case there's one more checker that can be cut
            if (not y > 5 and not y < 2):
                if (str(matrix[x - 1][y + 1]) == "X" and not str(matrix[x - 2][y + 2]) == "X" and not str(matrix[x - 2][y + 2]) == "O"):
                    cutRight = True
                if (str(matrix[x - 1][y - 1]) == "X" and not str(matrix[x - 2][y - 2]) == "X" and not str(matrix[x - 2][y - 2]) == "O"):
                    cutLeft = True
            elif ( y > 5 ):
                if (str(matrix[x - 1][y - 1]) == "X" and not str(matrix[x - 2][y - 2]) == "X" and not str(matrix[x - 2][y - 2]) == "O"):
                    cutLeft = True
            else:
                if (str(matrix[x - 1][y + 1]) == "X" and not str(matrix[x - 2][y + 2]) == "X" and not str(matrix[x - 2][y + 2]) == "O"):
                    cutRight = True

        # If none of the moves were correct...
        else:
            print ("No Valid Moves !!! Try again....")
            moveOChecker()

        
    else:
        print ("Not a checker!")
        moveOChecker()

    # End of checking of O Checker moves        

# End of checking moves of X and O

while True:
    moveXChecker()    
    moveOChecker()