# Domenic Hanson
# Portfolio Project
# Sudoku

class Sudoku:
    # Constructor that creates the Sudoku starting board (values that cant be changed) and a copy
    # that will hold the player's entries as well as several other attributes needed to test
    # their solution
    def __init__(self):
        self.base_board = [[0 for x in range(9)] for n in range(9)] # Empty (0's) 9x9 array to hold the base board
        self.board = [[0 for x in range(9)] for n in range(9)]      # Empty (0's) 9x9 array to hold the player's entries
        self.boxes = [[0 for x in range(9)] for n in range(9)]      # Empty (0's) 9x9 array to track entries for each 3x3 box
        self.solved = False                                         # Attribute to track if the board has been solved
        self.in_box = [[0 for x in range(9)] for n in range(9)]     # Empty (0's) 9x9 array to track how many times a number has been used in a 3x3 box
        self.in_row = [[0 for x in range(9)] for n in range(9)]     # Empty (0's) 9x9 array to track how many times a number has been used in a row
        self.in_col = [[0 for x in range(9)] for n in range(9)]     # Empty (0's) 9x9 array to track how many times a number has been used in a 3x3 box
        self.generateBoard()                                        # Calls generateBoard() to fill in the base board with the puzzle
        self.fillUsed()                                             # Fills in the empty arrays to keep track of how many times a number has been used

    # This uses an exhaustive approach (brute force) to check each row, column, and box tracking array
    # to see if a number has been uses once and only once. It also makes sure the board has been completed
    # It runs in O(n^2) time where n is the length of a column/row by iterating  though an inner and outer loop
    # checking each element in each array to see if the count is > 1 (meaning there are duplicates) 
    # It also uses the same nested loops to check the actual game board for 0s (indicating an empty cell)
    # If there are any duplicate values, it prints a hint to inform the user as to the row/column/box that has the duplicate
    # If the board has been completely filled in but has duplicates, it also informs the user of this fact 
    # If the board is completely filled out and each tracking array indicates there are no duplicates, 
    # it sets the self.solved attribute to True to indicate that the array was solved successfully.   
    def checkBoard(self):
        valid = True
        complete = True
        for r in range(len(self.board)):
            for c in range(len(self.board)):
                if self.in_box[r][c] > 1:
                    valid = False
                    print(f"Hint: There is a conflict in box {r + 1}.")
                if self.in_row[r][c] > 1:
                    valid = False
                    print(f"Hint: There is a conflict in row {r + 1}.")
                if self.in_col[r][c] > 1:
                    valid = False
                    print(f"Hint: There is a conflict in column {r + 1}.")
                if self.board[r][c] == 0:
                    valid = False
                    complete = False
        if valid:
            self.solved = True
        if complete and not valid:
            print("There are conflicts in the board, please fix them to solve the puzzle.")
    
    # Uses nested for loops to fill in the value tracking arrays and sets the array position equal 
    # to the count of the number of times that the value appeared in a given row/column/box
    def fillUsed(self):
        for r in range(len(self.board)):
            for c in range(len(self.board)):
                self.boxes[r][c] = self.board[(r // 3 * 3) + (c // 3)][((r % 3) * 3) + (c % 3)]
                if self.boxes[r][c] != 0:
                    self.in_box[r][self.boxes[r][c]-1] += 1
                if self.board[r][c] != 0:
                    self.in_row[r][self.board[r][c]-1] += 1
                if self.board[c][r] != 0:
                    self.in_col[r][self.board[c][r]-1] += 1
    
    # Increases or decreases the count for a provided value in the tracking arrays for the position
    # of the value in the row/column/box. It receives a positive 1 for "used" to increase the count 
    # and a negative value for "used" to decrease the count
    def markUsed(self, r, c, num, used):
        self.in_row[r][num-1] += used
        self.in_col[c][num-1] += used
        self.in_box[(r // 3 * 3) + (c // 3)][num - 1] += used
    
    # Hard codes the base starting board then calls the copyBaseBoard() function to copy over
    # the cells to the user's board
    def generateBoard(self):
        # Board from https://en.wikipedia.org/wiki/Sudoku
        self.base_board[0] = [5,3,0,0,7,0,0,0,0]
        self.base_board[1] = [6,0,0,1,9,5,0,0,0]
        self.base_board[2] = [0,9,8,0,0,0,0,6,0]
        self.base_board[3] = [8,0,0,0,6,0,0,0,3]
        self.base_board[4] = [4,0,0,8,0,3,0,0,1]
        self.base_board[5] = [7,0,0,0,2,0,0,0,6]
        self.base_board[6] = [0,6,0,0,0,0,2,8,0]
        self.base_board[7] = [0,0,0,4,1,9,0,0,5]
        self.base_board[8] = [0,0,0,0,8,0,0,7,9]
        self.copyBaseBoard()

    # Fills in the user's board with the values that are in the base starting board            
    def copyBaseBoard(self):
        for r in range(len(self.base_board)):
            for c in range(len(self.base_board)):
                self.board[r][c] = self.base_board[r][c]

    # Prints the board to the terminal in a way that makes the Sudoku board easy to see.
    # Cells that can have a value entered/changed by the user (not in the base board)
    # are printed underlined. Numbers to indicate the rows and columns are displayed
    # and the boxed areas are divided to make them more apparent to the user
    def printBoard(self):
        print('')
        print("    1  2  3   4  5  6   7  8  9")
        div = "  +-----------------------------+"
        print(div)
        count_row = 0
        for count, r in enumerate(self.board, 1):
            line = str(count) + ' |'     
            if count_row == 3:
                print(div)
                count_row = 0
            count_row += 1
            count_box = 0
            for i, e in enumerate(r, 1):
                if e == 0:
                    space = "_"
                elif self.board[count-1][i-1] != self.base_board[count-1][i-1]:
                    space = "\u0332" + str(e)
                else:
                    space =  str(e)
                count_box += 1
                if count_box == 3:
                    line += " " + space +' |'
                    count_box = 0
                else:
                    line += " " + space + " "

            print(line)
        print(div)

    # Called by the main function to play the game and continue to get the user's desired moves.
    # Calls the validateMove() method to get the user's validated desired move. If the
    # user wants to quit it returns false to the calling function. If the user wants to solve the 
    # puzzle, it calls the resetAndSolve() function to solve the puzzle and then checks the solution
    # If the user enters '0' for the value, the cell selected is cleared by setting it to 0 and
    # the count for the number that was in the cell is reduced by 1
    # If a value is entered, the cell selected is set to that value and the count for that number
    # is increased by 1 in each row/column/box tracking array
    def makeMove(self):
        move_list = self.validateMove()
        if move_list[0] == "Q":
            return False
        elif move_list[0] == 'S':
            self.resetAndSolve()
            self.checkBoard()
        elif move_list[2] == '0':
            print(f"Clearing value {self.board[int(move_list[0])-1][int(move_list[1])-1]} placed at row {move_list[0]} column {move_list[1]}.")
            self.markUsed(int(move_list[0])-1, int(move_list[1])-1, self.board[int(move_list[0])-1][int(move_list[1])-1], -1)
            self.board[int(move_list[0])-1][int(move_list[1])-1] = int(move_list[2])
            self.checkBoard() 
        else:
            if self.board[int(move_list[0])-1][int(move_list[1])-1] != 0:
                self.markUsed(int(move_list[0])-1, int(move_list[1])-1, self.board[int(move_list[0])-1][int(move_list[1])-1], -1)
            self.board[int(move_list[0])-1][int(move_list[1])-1] = int(move_list[2])
            if not self.noConflicts(int(move_list[2]), int(move_list[0])-1, int(move_list[1])-1):
                print(f"Hint: There is a conflict for value {move_list[2]} placed at row {move_list[0]} column {move_list[1]}.")
            self.markUsed(int(move_list[0])-1, int(move_list[1])-1, int(move_list[2]), 1)
            self.checkBoard()
        return True
    
    # This prompts the user to enter a move, solve the board, or quit and validates their input
    # It makes sure that the column and row selected by the user are in the proper  range (1-9)
    # and ensures that the value is either in the proper range (1-9) or the user wishes to erase the 
    # value in the selected cell (0)
    # Additionally, it ensures that the user cannot select a cell that has a hard coded value from the
    # base board that was set as part of the original puzzle
    # Error messages are given for most common cases of invalid input and a general error is given to
    # cover all other cases
    # The valid input is stored in a list and returned to the calling method (makeMove())
    def validateMove(self):
        valid = False
        valid_input = [str(x) for x in range(0,10)]
        valid_index = [str(x) for x in range(1,10)]
        while not valid:
            print('Enter a row, column, and value separated with a space. Type "Q" to quit or "S" to solve: ')
            move_list = input().split(" ")
            try:
                if move_list[0] == 'Q' or move_list[0] == 'S':
                    valid = True
                elif len(move_list) != 3:
                    print("You did not enter the correct number of inputs. Try again")
                elif move_list[0] not in valid_index:
                    print("Row is out of range. Enter a number from 1 to 9.")
                elif move_list[1] not in valid_index:
                    print("Column is out of range. Enter a number from 1 to 9.")
                elif move_list[2] not in valid_input:
                    print("Value is out of range. Enter a number from 1 to 9 to select a value for the cell or enter 0 to clear it.")
                elif  self.base_board[int(move_list[0])-1][int(move_list[1])-1] != 0:
                    print("You cannot overwrite this value. Please select a different row and/or column.")
                else:
                    valid = True
            except:
                print("You did not enter a valid input. Try again.")
        return move_list
    
    # This method resets the board and number counts (sets arrays tracking the counts of numbers for rows/columns/boxes to 0,
    # regenerates the hard coded original puzzle board, and recounts the number of times a number is used and fills the tracking arrays )
    # It then calls the solveBoard() method to solve the board and print it
    # The user is then informed if a solution was found or not
    def resetAndSolve(self):
        self.in_box = [[0 for x in range(9)] for n in range(9)]
        self.in_row = [[0 for x in range(9)] for n in range(9)]
        self.in_col = [[0 for x in range(9)] for n in range(9)]
        self.generateBoard()
        self.fillUsed()
        print("Solving...")
        solution = self.solveBoard()
        if solution:
            print("As solution was found!")
        else:
            print("No solution was found.")
   
    # Used in backtracking by solveBoard() to find the next empty cell on the board and store its coordinates
    # in the 'index' list to be used in the main solveBoard() algorithm
    # If no empty cell is found, it returns False
    def findEmpty(self, index):
        for r in range(len(self.board)):
            for c in range(len(self.board)):
                if self.board[r][c] == 0:
                    index[0] = r
                    index[1] = c
                    return True
        return False
    
    # Checks the count for a given number in a given row and column against what is recorded for
    # that number in the corresponding row/column/box count tracking arrays.
    # If the number is not the row/column/box it returns True
    def noConflicts(self, num, r, c):
        if self.in_row[r][num - 1] == 0:
            not_in_row = True
        else:
            not_in_row = False
        if self.in_col[c][num - 1] == 0:
            not_in_col = True
        else:
            not_in_col = False
        if self.in_box[(r // 3 * 3) + (c // 3)][num - 1] == 0:
            not_in_box = True
        else:
            not_in_box = False
        return not_in_row and not_in_col and not_in_box 

    # This method solves the Sudoku board using a recursive backtracking algorithm, which is brute force approach.
    # It is based on the algorithm described here (given in C++): https://see.stanford.edu/materials/icspacs106b/H19-RecBacktrackExamples.pdf
    # It works by finding the next empty cell and getting its coordinates. (If there is no empty cell remaining, it returns True, 
    # indicating the base case that the board is solved)
    # It then tries all the possible numbers in that cell (loops through trying 1-9), checking if there is a conflict for 
    # that number in the row, column, and box if it is placed. If there is no conflict, it assigns the cell that number, updates the arrays that track that the 
    # number has been placed in that row/cell/box, and calls itself recursively. The next recursive call finds the next empty cell and repeats the process.
    # If a number cannot be placed without a conflict it 'backtracks' to a previous good decision point, setting the previously set values back to 0 and updating the
    # tracking arrays using the markedUsed() method, and then tries the next number. If it backtracks all the way out and has no more numbers to try,
    # then there is no solution and it returns False. If it reaches the "bottom" where each cell has been filled, it returns True from the base case all the way
    # back through the stack and returns True to indicate a solution has been found. The board remains with the solution in place.
    def solveBoard(self):
        index = [-1,-1]
        if not self.findEmpty(index):
            return True
        r = index[0]
        c = index[1]
        for num in range(1,10):
            if self.noConflicts(num, r, c):
                self.board[r][c] = num
                self.markUsed(r, c, num, 1)
                if self.solveBoard():
                    return True
                self.board[r][c] = 0
                self.markUsed(r,c, num, -1)
        return False

# This function handles the running of the game. It generates the default board and prints instructions.
# It then continues to print the board and prompt the user for moves until the board is solved, the user
# quits, or the user selects to have the program solve the board.
# If the user solves the board or has the program solve the board, the user is prompted to play again or quit.  
def play():
    myBoard = Sudoku()
    play_game = True
    print('')
    print('Welcome to Sudoku!')
    print('')
    print('To play, please enter your move in the form "row column value" with a single space between each number.')
    print('Rows and columns must be from 1 to 9 and values must be from 0 to 9.')
    print('Entering a value of "0" will clear the current value for the cell on the board.')
    print('You cannot clear or change the original values on the board.')
    print('If you would like to see the solution to the puzzle, you can enter "S".')
    print('To quit and exit, enter "Q".')
    print('Good luck!!!')
    while play_game:
        myBoard.printBoard()
        play_game = myBoard.makeMove()
        if myBoard.solved == True:
            myBoard.printBoard()
            print("Solved successfuly!")
            play_again = input('Would you like to play again? \nEnter "Q" to quit and exit or enter any other key to play again. ')
            if play_again == 'Q':
                play_game = False
            else:
                myBoard = Sudoku()

# Calls the play() function to start the game.
play()


