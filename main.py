board = [
    [7,8,0,4,0,0,1,2,0],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7]
]

def solve(board: list[list[int]]) -> bool:
    """
    Recursively solves the board square by square.  Starts by checking the first empty square and trying every number until a valid one is found, then moves onto the next square and repeating the process
    If there are no valid numbers in the second square then it moves back to the first recursive call and continues to move up the numbers until next valid one is found and then moves on.  
    The base case is when there are no empty squares left as that is when the board is fully solved.

    Args:
        board (list[list[int]]): A nested list where each internal list represents a row and the numbers in those lists represent the number in that row, column slot

    Returns:
        Boolean: Returns true if there is a valid number to place in the current slot, allowing the recursion to move onto the next call.  Returns false if there are not valid slots, moving back to the previous case.
    """
    find = find_empty(board)
    if not find:
        return True
    else:
        row, col = find
    
    for i in range(1, 10):
        if valid(board, i, (row, col)):
            board[row][col] = i

            if solve(board):
                return True
            
            board[row][col] = 0
    
    return False
    

def valid(board: list[list[int]], num: int, pos: tuple[int, int]) -> bool:
    """
    Checks to see if the chosen number can be placed in that square.  Checks the row, column and 3x3 square that the number is being placed in to see that it is unique.

    Args:
        board (list[list[int]]): A nested list where each internal list represents a row and the numbers in those lists represent the number in that row, column slot
        num (int): The number to be placed on the board
        pos (tuple[int, int]): A tuple containing the 'coordinates' of the selected square (row, col)

    Returns:
        bool: Returns true if the position is valid for the number, false if not
    """

    # Check row
    for i in range(len(board[0])):
        if board[pos[0]][i] == num and pos[1] != i:
            return False
    
    # Check column
    for i in range(len(board)):
        if board[i][pos[1]] == num and pos[0] != i:
            return False
    
    # Check box
    box_x = pos[1] // 3
    box_y = pos[0] // 3

    for i in range(box_y * 3, box_y * 3 + 3):
        for j in range(box_x * 3, box_x * 3 + 3):
            if board[i][j] == num and (i,j) != pos:
                return False
    
    return True
        

def print_board(board: list[list[int]]):
    """
    Prints the sudoku board

    Args:
        board (list[list[int]]): A nested list where each internal list represents a row and the numbers in those lists represent the number in that row, column slot
    """
    for i in range(len(board)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - ")

        for j in range(len(board[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")

            if j == 8:
                print(board[i][j])
            else:
                print(str(board[i][j]) + " ", end="")

def find_empty(board: list[list[int]]) -> tuple[int, int] | None:
    """
    Finds the first empty spot on the board by searching through the rows and the columns

    Args:
        board (list[list[int]]): A nested list where each internal list represents a row and the numbers in those lists represent the number in that row, column slot

    Returns:
        tuple[int, int] | None: Returns the coordinates of the empty spot if there is one (row, col), if there are no empty spots returns None
    """
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                return (i, j) # row, col
    
    return None

def main():
    print_board(board)
    solve(board)
    print('_______________________')
    print('')
    print_board(board)

if __name__ == "__main__":
    main()