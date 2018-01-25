
# choose size of board (example- 8: 8x8, 7: 7x7)
size = int(input("Enter board size: "))



''' checks if the position is available by checking
row, column, and diagonals '''
def check_position(chess_board, row, column):
	for i in range(size):
		if chess_board[row][i] == "Q" or chess_board[i][column] == "Q":
			return False

	for i in range(size):
		for j in range(size):
			if abs(row - i) == abs(column - j):
				if chess_board[i][j] == "Q":
					return False  
	# chess_board[row][column] = "Q"
	return True

# def check_all_solutions(chess_board, column):
# 	counter = 0

# 	if column >= size:
# 		counter += 0


def iterative(chess_board, column = 0):
	
	positions = []

	for col in range(size):
		for row in range(size):
			if check_position(chess_board, row, col):
				chess_board[row][col] = "Q"
				positions.append((row,col))
				break




def check_solution(chess_board, column):
    
    if column >= size:
        return True

    for i in range(size):
        if check_position(chess_board, i, column):
        	chess_board[i][column] = "Q"
        	if check_solution(chess_board, column + 1) == True:
        		return True
            
        	chess_board[i][column] = 0

    return False

# prints chess_board to the console
def print_board(chess_board):
	for array in chess_board:
		line = ""
		for item in array:
			line += " %s " % str(item)
		print(line)


def solveNQueen():
	# makes board 
	chess_board = [[0 for x in range(size)] for y in range(size)] 
	
	if check_solution(chess_board, 0) == False:
		print("There is no solution")
		return False
	print_board(chess_board)
	return True


solveNQueen()


	# Better for Readability but takes more time

	# for c in range(size):
	# 	if chess_board[row][c] == "Q":
	# 		print("cannot place because of row: %s col: %s" % (row, c))
	# 		return False

	# for r in range(size):
	# 	if chess_board[r][column] == "Q":
	# 		print("cannot place because of row: %s col: %s" % (r, column))
	# 		return False
