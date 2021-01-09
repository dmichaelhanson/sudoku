#Sukoku.py

Sudoku.py is a sudoku game and solver

##Information:

NAME: DOMENIC HANSON
ASSIGNMENT: PORTFOLIO PROJECT - SUDOKU
DATE: December 7, 2020
FILES SUBMITTED: portfolio.py
ABOUT: This README File is to accompany the above file and explain its behavior.
Version: All files should be run with Python 3.6 or later. Please run with python3

**Command to run on Flip:**

python3 sukoku.py

**Repl.it:**

Sukoku.py is also available at [https://repl.it/join/ukyaemfh-mikehanson](https://repl.it/join/ukyaemfh-mikehanson)

**Output:**

Sudoku game in the terminal

**Objective:**

Play a game of sudoku in the terminal. Sudoku is played on a 9x9 grid composed of 9 &quot;boxes&quot; of 3x3 grids that divide the grid equally and do not overlap. The rules of sudoku are to complete a 9x9 grid using the integers 1-9 where each row, column, and box in the grid contains each number from 1 to 9 with no repeated or missing numbers in an given row, column, or box. A given number of cells are prepopulated at the start of the game and the user must fill in the remaining cells adhering to these rules until the board is solved.

##Functions:

**play():**

This function handles the running of the game. It generates the default board and prints instructions. It then continues to print the board and prompt the user for moves until the board is solved, the user quits, or the user selects to have the program solve the board. If the user solves the board or has the program solve the board, the user is prompted to play again or quit.

##Classes:

**Sudoku:** 
The Sudoku class creates a sudoku game and contains the relevant attributes and methods to generate a board, allow a user to make moves, verify the moves, verify the board is solved, and solve the board according to the rules of sudoku. When an object of this class is initially constructed, it creats a &quot;base board&quot; that has a hard coded sudoku starting puzzle, a player board that copies these hard coded values and will maintain the player&#39;s moves, a boxes board to track the values used in each box, and arrays to track if a number was used in a given row, column, or box.

**Attributes:**

self.base\_board = Int List of lists - 9x9 array to hold the base board hard coded sudoku puzzle

self.board = Int List of lists - 9x9 array to hold the player&#39;s entries on the board

self.boxes = Int List of lists – 9x9 array to hold the players entries in each box

self.solved = bool – tracks if the board has been solved yet

self.in\_box = Int List of lists – 9x9 array that tracks how many times a number has been used in a 3x3 box by incrementing a count in the position in the array corresponding with that number

self.in\_row = Int List of lists – 9x9 array that tracks how many times a number has been used in row by incrementing a count in the position in the array corresponding with that number

self.in\_col = Int List of lists – 9x9 array that tracks how many times a number has been used in col by incrementing a count in the position in the array corresponding with that number

**Methods:**

\_\_init\_\_(self): Constructor method that creates the Sudoku Object. Does not take in any parameters. It sets the attributes to their default values and builds the default board.

checkBoard(self): This uses an exhaustive approach (brute force) to check each row, column, and box tracking array to see if a number has been uses once and only once. It also makes sure the board has been completed. It runs in O(n^2) time where n is the length of a column/row by iterating though an inner and outer loop checking each element in each array to see if the count is \&gt; 1 (meaning there are duplicates). It also uses the same nested loops to check the actual game board for 0s (indicating an empty cell). If there are any duplicate values, it prints a hint to inform the user as to the row/column/box that has the duplicate. If the board has been completely filled in but has duplicates, it also informs the user of this fact. If the board is completely filled out and each tracking array indicates there are no duplicates, it sets the self.solved attribute to True to indicate that the array was solved successfully.

fillUsed(self): Uses nested for loops to fill in the value tracking arrays and sets the array position equal to the count of the number of times that the value appeared in a given row/column/box.

markUsed(self, r, c, num, used): Takes in a row number &quot;r&quot;, column number &quot;c&quot;, a value that was used &quot;num&quot;, and an increment or decrement amount (+1 or -1) as &quot;used&quot; to indicate if it is being marked as used or unmarked. It increases or decreases the count for a provided value in the tracking arrays for the position of the value in the row/column/box. It receives a positive 1 for &quot;used&quot; to increase the count and a negative value for &quot;used&quot; to decrease the count.

generateBoard(self): Hard codes the base starting board then calls the copyBaseBoard() function to copy over the cells to the user&#39;s board.

copyBaseBoard(self): Fills in the user&#39;s board with the values that are in the base starting board .

printBoard(self): Prints the board to the terminal in a way that makes the Sudoku board easy to see. Cells that can have a value entered/changed by the user (not in the base board) are printed underlined. Numbers to indicate the rows and columns are displayed and the boxed areas are divided to make them more apparent to the user.

makeMove(self): Called by the main function to play the game and continue to get the user&#39;s desired moves. Calls the validateMove() method to get the user&#39;s validated desired move. If the user wants to quit, it returns false to the calling function. If the user wants to solve the puzzle, it calls the resetAndSolve() function to solve the puzzle and then checks the solution. If the user enters &#39;0&#39; for the value, the cell selected is cleared by setting it to 0 and the count for the number that was in the cell is reduced by 1. If a value is entered, the cell selected is set to that value and the count for that number is increased by 1 in each row/column/box tracking array.

validateMove(self): This prompts the user to enter a move, solve the board, or quit and validates their input. It makes sure that the column and row selected by the user are in the proper range (1-9) and ensures that the value is either in the proper range (1-9) or the user wishes to erase the value in the selected cell (0). Additionally, it ensures that the user cannot select a cell that has a hard coded value from the base board that was set as part of the original puzzle. Error messages are given for most common cases of invalid input and a general error is given to cover all other cases. The valid input is stored in a list and returned to the calling method (makeMove()).

resetAndSolve(self): This method resets the board and number counts (sets arrays tracking the counts of numbers for rows/columns/boxes to 0, regenerates the hard coded original puzzle board, and recounts the number of times a number is used and fills the tracking arrays). It then calls the solveBoard() method to solve the board and print it. The user is then informed if a solution was found or not.

findEmpty(self, index): Takes in a list &quot;index&quot; that contains a row and column number. Used in backtracking by solveBoard() to find the next empty cell on the board and store its coordinates in the &#39;index&#39; list to be used in the main solveBoard() algorithm. If no empty cell is found, it returns False.

noConflicts(self, num, r, c): Takes in a number &quot;num&quot; to be entered into a row &quot;r&quot; and column &quot;c&quot;. Checks the count for a given number in a given row and column against what is recorded for that number in the corresponding row/column/box count tracking arrays. If the number is not the row/column/box it returns True.

solveBoard(self): This method solves the Sudoku board using a recursive backtracking algorithm, which is brute force approach. It is based on the algorithm described here (given in C++): https://see.stanford.edu/materials/icspacs106b/H19-RecBacktrackExamples.pdf. It works by finding the next empty cell and getting its coordinates. (If there is no empty cell remaining, it returns True, indicating the base case that the board is solved). It then tries all the possible numbers in that cell (loops through trying 1-9), checking if there is a conflict for that number in the row, column, and box if it is placed. If there is no conflict, it assigns the cell that number, updates the arrays that track that the number has been placed in that row/cell/box, and calls itself recursively. The next recursive call finds the next empty cell and repeats the process. If a number cannot be placed without a conflict it &#39;backtracks&#39; to a previous good decision point, setting the previously set values back to 0 and updating the tracking arrays using the markedUsed() method, and then tries the next number. If it backtracks all the way out and has no more numbers to try, then there is no solution and it returns False. If it reaches the &quot;bottom&quot; where each cell has been filled, it returns True from the base case all the way back through the stack and returns True to indicate a solution has been found. The board remains with the solution in place.
