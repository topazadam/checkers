# Adam's checkers game
import pygame
import random

# Define game colors
BLACK    = (   0,   0,   0)
WHITE    = ( 255, 255, 255)
GREEN    = (   0, 255,   0)
RED      = ( 255,   0,   0)
BLUE     = (   0,   0, 255)
YELLOW   = ( 255, 255,   0)
TRANS    = (   1,   2,   3)

# Set the game size
WIDTH = 700
HEIGHT = 700
MARK_SIZE = 50

# define the rows of the game board
# 7 
# 6
# 5
# 4
# 3
# 2
# 1 (1,0) (1,1) 
# 0 (0,0) (1,0)
#     0     1    2
row = {}

# ====================================================================
class GameBoard():
	def __init__(self):
		self.boardColours = [] # colour of tiles
		self.boardState = [] # location of counters

		# Initialise board colour array
		for i in range(8):
		    self.boardColours.append([])
		    for j in range(1):
		    	for k in range(8):
		        	self.boardColours[i].append(0)

		# initialise board state array        	
		for i in range(8):
		    self.boardState.append([])
		    for j in range(1):
		    	for k in range(8):
		        	self.boardState[i].append('---')
# ==================================================
		# set all white player pieces- 1,3,5,7
		for i in range(0,8,2):
			self.boardState[0][i] = self.get_pieceID('w',i)

		# set all white player pieces- 2,4,6,8
		for i in range(1,8,2):
			self.boardState[1][i] = self.get_pieceID('w',i)

		# set white pieces on 3rd row - 9,10,11,12
		self.boardState[2][0] = self.get_pieceID('w',8)
		self.boardState[2][2] = self.get_pieceID('w',9)
		self.boardState[2][4] = self.get_pieceID('w',10)
		self.boardState[2][6] = self.get_pieceID('w',11)
# ==================================================
		# set all black player pieces- 1,3,5,7
		for i in range(0,8,2):
			self.boardState[7][i] = self.get_pieceID('b',i)

		# set all black player pieces- 2,4,6,8
		for i in range(1,8,2):
			self.boardState[6][i] = self.get_pieceID('b',i)

		# set black pieces on 5th row - 9,10,11,12
		self.boardState[5][0] = self.get_pieceID('b',8)
		self.boardState[5][2] = self.get_pieceID('b',9)
		self.boardState[5][4] = self.get_pieceID('b',10)
		self.boardState[5][6] = self.get_pieceID('b',11)

		#set black player pieces - 1,3,5,7
		for j in range(0,8,2):
			for i in range(1,8,2):
				self.boardColours[j][i] ='b'

		#set black player pieces - 2,4,6,8
		for j in range(1,8,2):
			for i in range(0,8,2):
				self.boardColours[j][i] ='b'
# ==================================================
		#set all black tiles - 1,3,5,7
		for j in range(0,8,2):
			for i in range(0,8,2):
				self.boardColours[j][i] ='b'

		#set all black tiles - 2,4,6,8
		for j in range(1,8,2):
			for i in range(1,8,2):
				self.boardColours[j][i] ='b'

		#set white tiles - 1,3,5,7
		for j in range(0,8,2):
			for i in range(1,8,2):
				self.boardColours[j][i] ='w'

		#set white tiles - 2,4,6,8
		for j in range(1,8,2):
			for i in range(0,8,2):
				self.boardColours[j][i] ='w'

	def disply_board_colours(self):
		# print the whole board
		print("  Col:   0    1    2    3    4    5    6    7")
		for i in range(8):
		    print("Row " + str(i) +": " + str(self.boardColours[i]))

	def disply_board_state(self):
		# print the whole board
		print("  Col:   0      1      2      3      4      5      6      7")
		for i in range(8):
		    print("Row " + str(i) +": " + str(self.boardState[i]))

	def setTileState(self,x,y,state):
		self.boardState[x][y] = state	

	def get_pieceID(self,player,pieceID):
		if pieceID < 10:
			return "{}0{}".format(player,pieceID)	
		if pieceID >= 10:
			return "{}{}".format(player,pieceID)			
# ====================================================================

# create the board 
myBoard = GameBoard()

# set an individual tile state - i.e. what piece is on the tile
#myBoard.setTileState(4,4,'r01')
myBoard.disply_board_colours()
#myBoard.disply_board_state()



	# def printRow(self):
	# 	print("===")
	# 	print("|"+str(self.occupiedBy)+"|")
	# 	print("===")

