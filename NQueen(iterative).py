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




# prints chess_board to the console
def print_board(chess_board):
	for array in chess_board:
		line = ""
		for item in array:
			line += " %s " % str(item)
		print(line)


def iterative(column = 0):
	
	chess_board = [[0 for x in range(size)] for y in range(size)] 
	positions = []

	for col in range(size):
		for row in range(size):
			if check_position(chess_board, row, col):
				# my_list.add(row,col)
				chess_board[row][col] = "Q"
				positions.append((row,col))
				break
			else:
				if row == size - 1:
					for r in range(positions[len(positions)-1][0] + 1, size - 1):
						if check_position(chess_board, r, positions[len(positions)-1][1]-1):
							chess_board[r][positions[len(positions)-1][1]-1] = "Q"
							positions.append((r,positions[len(positions)-1][1]-1))
							break
				
	print_board(chess_board)


iterative()

def solveNQueen():
	# makes board 
	chess_board = [[0 for x in range(size)] for y in range(size)] 
	
	if check_solution(chess_board, 0) == False:
		print("There is no solution")
		return False
	print_board(chess_board)
	return True


# solveNQueen()


# class Node(object):
#     def __init__(self, x, y, n = None):
#         self.x = x
#         self.y = y
#         self.next_node = n
    
#     def get_next(self):
#         return self.next_node
    
#     def set_next(self, n):
#         self.next_node = n
    
#     def get_data(self):
#         return self.data
    
#     def set_data(self, d):
#         self.data = d

# class LinkedList(object):
#     def __init__(self, r=None):
#         self.root = r
#         self.size = 0

#     def get_size(self):
#         return self.size

#     def add(self, d):
#         new_node = Node(d, self.root)
#         self.root = new_node
#         self.size += 1

#     def remove(self, d):
#         this_node = self.root
#         prev_node = None
#         while this_node:
#             if this_node.get_data() == d:
#                 if prev_node:
#                     prev_node.set_next(this_node.get_next())
#                 else:
#                     self.root = this_node
#                 self.size -= 1
#                 return True
#             else:
#                 prev_node = this_node
#                 this_node = this_node.get_next()
#         return False

#     def find(self, d):
#         this_node = self.root
#         while this_node:
#             if this_node.get_data() == d:
#                 return d
#             else:
#                 self.root = this_node.get_next()
#         return None
#     def display(self):
#         elements = []
#         this_node = self.root
#         while this_node != None:
#             elements.append(this_node.data)
#             this_node = this_node.get_next()
#         return elements
    

# myList = LinkedList()
# myList.add(5)
# myList.add(23)
# myList.add(34)
# myList.add(1)

# print(myList.remove(5))
# print(myList.find(1))
# print(myList.display())
