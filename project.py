#put into function
BoardList = []


for i in range(8):
	BoardListTemp = []
	for x in range(8):
		BoardListTemp.append("  ")
	BoardList.append(BoardListTemp)


def displayBoard():#Displays Board DONE
	for z in range(25):
		print("-", end = '')
	print("-")
	for x in BoardList:
		for y in x:
			print('|', end = '')

			print(y, end = '')
		print('|', end = '')
		print()
		for z in range(25):
			print("-", end = '')
		print()


def populateBoard():#Creates peices on board DONE
	check = 11
	for x in range(3):
		for y in range(8):
			 if ((x+y)%2 == 1):
			 	BoardList[x][y] = check
			 	check = check+2
	check = 10
	for x in range(3):
		for y in range(8):
			 if (((7-x)+y)%2 == 1):
			 	BoardList[7-x][y] = check
			 	check = check+2
			



def recursivePlayerPrimer(x,y): # {[[x,y],[jumped peices],true],
					#  [x,y] [12, 14] [false]]}
	listOfMoves = []

	if((x-1 > -1) & (y-1 > -1)):
		if(BoardList[x-1][y-1] == "  "):
			listToAppend = []
			listXY = []
			listJumped = []
			listXY.append(x-1)
			listXY.append(y-1)
			listToAppend.append(listXY)
			listToAppend.append(listJumped)#done LEFT UPPER
			listOfMoves.append(listToAppend)

		elif (x-2 > -1) & (y-2 > -1):
			if BoardList[x-1][y-1] != "  " and BoardList[x][y] != "  ":
				if(BoardList[x-1][y-1]%2 != BoardList[x][y]%2):
					if(BoardList[x-2][y-2] == "  "):
						BoardList[x-2][y-2] == BoardList[x][y]
						listToAppend = []
						listXY = []
						listXY.append(x-2)
						listXY.append(y-2)
						listJumped = []
						listJumped.append(BoardList[x-1][y-1])
						listToAppend.append(listXY)
						listToAppend.append(listJumped)
						listOfMoves.append(listToAppend)
						######APPEND CURRENT SOLUTION THEN ADD MORE recursively
						recursivePlayerEngine(x-2,y-2, listJumped, listToAppend)
						############recursive plus list########## LEFT JUMP
						BoardList[x-2][y-2] == "  "

	if((x-1 > -1) & (y+1 < 8)):
		if(BoardList[x-1][y+1] == "  "):
			listToAppend = []
			listXY = []
			listJumped = []
			listXY.append(x-1)
			listXY.append(y+1)
			listToAppend.append(listXY)
			listToAppend.append(listJumped)#done RIGHT UPPER
			listOfMoves.append(listToAppend)

		elif (BoardList[x-1][y+1]%2 != BoardList[x][y]%2):
			if BoardList[x-1][y+1] != "  " and BoardList[x][y] != "  ":
				if (x-2 > -1) & (y+2 < 8):
					if(BoardList[x-2][y+2] == "  "):
						BoardList[x-2][y+2] == BoardList[x][y]
						listToAppend = []
						listXY = []
						listXY.append(x-2)
						listXY.append(y+2)
						listJumped = []
						listJumped.append(BoardList[x-1][y+1])
						listToAppend.append(listXY)
						listToAppend.append(listJumped)
						listOfMoves.append(listToAppend)
						######APPEND CURRENT SOLUTION THEN ADD MORE recursively
						recursivePlayerEngine(x-2,y+2, listJumped, listToAppend)
						###########recursive plus list##########
						BoardList[x-2][y+2] == "  "




		#########################################OVER 50 SPEARATION
		if BoardList[x][y] != "  ":
			if BoardList[x][y] > 49:
				if((x+1 < 8) & (y+1 < 8)):
					if(BoardList[x+1][y+1] == "  "):
						listToAppend = []
						listXY = []
						listJumped = []
						listXY.append(x+1)
						listXY.append(y+1)
						listToAppend.append(listXY)
						listToAppend.append(listJumped)#done RIGHT UPPER
						listOfMoves.append(listToAppend)
	
					elif (BoardList[x+1][y+1]%2 != BoardList[x][y]%2):
						if BoardList[x+1][y+1] != "  " and BoardList[x][y] != "  ":
							if(x+2 < 8) & (y+2 < 8):
								if(BoardList[x+2][y+2] == "  "):
									BoardList[x+2][y+2] == BoardList[x][y]
									listToAppend = []
									listXY = []
									listXY.append(x+2)
									listXY.append(y+2)
									listJumped = []
									listJumped.append(BoardList[x+1][y+1])
									listToAppend.append(listXY)
									listToAppend.append(listJumped)
									listOfMoves.append(listToAppend)
									######APPEND CURRENT SOLUTION THEN ADD MORE recursively
									recursivePlayerEngine(x+2,y+2, listJumped, listToAppend)
									###########recursive plus list########## LEFT JUMP
									BoardList[x-2][y+2] == "  "
	
				if((x+1 < 8) & (y-1 > -1)):
					if(BoardList[x+1][y-1] == "  "):
						listToAppend = []
						listXY = []
						listJumped = []
						listXY.append(x+1)
						listXY.append(y-1)
						listToAppend.append(listXY)
						listToAppend.append(listJumped)#done LEFT UPPER
						listOfMoves.append(listToAppend)
	
					elif (x+2 < 8) & (y-2 > -1):
						if BoardList[x+1][y-1] != "  " and BoardList[x][y] != "  ":
							if(BoardList[x+1][y-1]%2 != BoardList[x][y]%2):
								if(BoardList[x+2][y-2] == "  "):
									BoardList[x+2][y-2] == BoardList[x][y]
									listToAppend = []
									listXY = []
									listXY.append(x+2)
									listXY.append(y-2)
									listJumped = []
									listJumped.append(BoardList[x+1][y-1])
									listToAppend.append(listXY)
									listToAppend.append(listJumped)
									listOfMoves.append(listToAppend)
									######APPEND CURRENT SOLUTION THEN ADD MORE recursively
									recursivePlayerEngine(x+2,y-2, listJumped, listToAppend)
									############recursive plus list########## LEFT JUMP
									BoardList[x+2][y-2] == "  "

	return listOfMoves


def recursivePlayerEngine(x,y, removedList, listToAdd):

	tempRemoved = removedList


	if (x-2 > -1) & (y-2 > -1):
		if BoardList[x-1][y-1] != "  " and BoardList[x][y] != "  ":
			if(BoardList[x-1][y-1]%2 != BoardList[x][y]%2):
				if(BoardList[x-2][y-2] == "  "):
					BoardList[x-2][y-2] == BoardList[x][y]
					listToAppend = []
					listXY = []
					listXY.append(x-2)
					listXY.append(y-2)
					tempRemoved.append(BoardList[x-1][y-1])
					listToAppend.append(listXY)
					listToAppend.append(tempRemoved)
					listToAdd.append(listToAppend)
					######APPEND CURRENT SOLUTION THEN ADD MORE recursively
					recursivePlayerEngine(x-2,y-2, tempRemoved, listToAdd)
					############recursive plus list########## LEFT JUMP
					BoardList[x-2][y-2] == "  "

	tempRemoved = removedList


	if((x-1 < 8) & (y+1 < 8)):
		if BoardList[x-1][y+1] != "  " and BoardList[x][y] != "  ":
			if (BoardList[x-1][y+1]%2 != BoardList[x][y]%2):
				if (x-2 > -1) & (y+2 < 8):
					if(BoardList[x-2][y+2] == "  "):
						BoardList[x-2][y+2] == BoardList[x][y]
						listToAppend = []
						listXY = []
						listXY.append(x-2)
						listXY.append(y+2)
						tempRemoved.append(BoardList[x-1][y+1])
						listToAppend.append(listXY)
						listToAppend.append(tempRemoved)
						listToAdd.append(listToAppend)
						######APPEND CURRENT SOLUTION THEN ADD MORE recursively
						recursivePlayerEngine(x-2,y+2, tempRemoved, listToAdd)
						###########recursive plus list##########
						BoardList[x-2][y+2] == "  "





	############add over 50
	tempRemoved = removedList
	if BoardList[x][y] != "  ":
		if BoardList[x][y] > 49:
			tempRemoved = removedList
			if BoardList[x+1][y+1] != "  " and BoardList[x][y] != "  ":
				if (x+2 < 8) & (y+2 < 8):
					if (BoardList[x+1][y+1]%2 != BoardList[x][y]%2):
						if(BoardList[x+2][y+2] == "  "):
							BoardList[x+2][y+2] == BoardList[x][y]
							listToAppend = []
							listXY = []
							listXY.append(x+2)
							listXY.append(y+2)
							tempRemoved.append(BoardList[x+1][y+1])
							listToAppend.append(listXY)
							listToAppend.append(tempRemoved)
							listToAdd.append(listToAppend)
							######APPEND CURRENT SOLUTION THEN ADD MORE recursively
							recursivePlayerEngine(x+2,y+2, tempRemoved, listToAdd)
							############recursive plus list##########
							BoardList[x+2][y+2] == "  "


		tempRemoved = removedList

		if((x+1 < 8) & (y-1 > -1)):#bottom left
			if BoardList[x+1][y-1] != "  " and BoardList[x][y] != "  ":
				if (BoardList[x+1][y-1]%2 != BoardList[x][y]%2):
					if (x+2 < 8) & (y-2 > -1):
						if(BoardList[x+2][y-2] == "  "):
							BoardList[x+2][y-2] == BoardList[x][y]
							listToAppend = []
							listXY = []
							listXY.append(x+2)
							listXY.append(y-2)
							tempRemoved.append(BoardList[x+1][y-1])
							listToAppend.append(listXY)
							listToAppend.append(tempRemoved)
							listToAdd.append(listToAppend)
							######APPEND CURRENT SOLUTION THEN ADD MORE recursively
							recursivePlayerEngine(x+2,y-2, tempRemoved, listToAdd)
							###########recursive plus list########## LEFT JUMP
							BoardList[x+2][y-2] == "  "
	return

def recursiveAiPrimer(x,y):

	listOfMoves = []

	if((x+1 < 8) & (y-1 > -1)):
		if(BoardList[x+1][y-1] == "  "):
			listToAppend = []
			listXY = []
			listJumped = []
			listXY.append(x+1)
			listXY.append(y-1)
			listToAppend.append(listXY)
			listToAppend.append(listJumped)#done LEFT UPPER
			fitness = 1
			listToAppend.append(fitness)
			listToAppend.append(x)
			listToAppend.append(y)
			listOfMoves.append(listToAppend)

		elif (x+2 < 8) & (y-2 > -1):
			if BoardList[x+1][y-1] != "  " and BoardList[x][y] != "  ":
				if (BoardList[x+1][y-1]%2 != BoardList[x][y]%2):
					if(BoardList[x+2][y-2] == "  "):
						BoardList[x+2][y-2] == BoardList[x][y]
						listToAppend = []
						listXY = []
						listXY.append(x+2)
						listXY.append(y-2)
						listJumped = []
						listJumped.append(BoardList[x+1][y-1])
						listToAppend.append(listXY)
						listToAppend.append(listJumped)
						fitness = 3
						listToAppend.append(fitness)
						listToAppend.append(x)
						listToAppend.append(y)
						listOfMoves.append(listToAppend)
						######APPEND CURRENT SOLUTION THEN ADD MORE recursively
						recursiveAiEngine(x+2,y-2, listJumped, listToAppend, fitness, x, y)
						############recursive plus list########## LEFT JUMP
						BoardList[x+2][y-2] == "  "

	if((x+1 < 8) & (y+1 < 8)):
		if(BoardList[x+1][y+1] == "  "):
			listToAppend = []
			listXY = []
			listJumped = []
			listXY.append(x+1)
			listXY.append(y+1)
			listToAppend.append(listXY)
			listToAppend.append(listJumped)#done RIGHT UPPER
			fitness = 1
			listToAppend.append(fitness)
			listToAppend.append(x)
			listToAppend.append(y)
			listOfMoves.append(listToAppend)


		elif ((BoardList[x+1][y+1]%2 != BoardList[x][y]%2) & (x+2 < 8) & (y+2 < 8)):
			if(BoardList[x+2][y+2] == "  "):
				BoardList[x+2][y+2] == BoardList[x][y]
				listToAppend = []
				listXY = []
				listXY.append(x+2)
				listXY.append(y+2)
				listJumped = []
				listJumped.append(BoardList[x+1][y+1])
				listToAppend.append(listXY)
				listToAppend.append(listJumped)
				fitness = 3
				listToAppend.append(fitness)
				listToAppend.append(x)
				listToAppend.append(y)
				listOfMoves.append(listToAppend)
				######APPEND CURRENT SOLUTION THEN ADD MORE recursively
				recursiveAiEngine(x+2,y+2, listJumped, listToAppend, fitness, x, y)
				###########recursive plus list##########
				BoardList[x+2][y+2] == "  "


		#########################################OVER 50 SPEARATION
		if BoardList[x][y] != "  ":
			if BoardList[x][y] > 49:
				if((x-1 > -1) & (y+1 < 8)):
					if(BoardList[x-1][y+1] == "  "):
						listToAppend = []
						listXY = []
						listJumped = []
						listXY.append(x-1)
						listXY.append(y+1)
						listToAppend.append(listXY)
						listToAppend.append(listJumped)#done RIGHT UPPER
						fitness = 1
						listToAppend.append(fitness)
						listToAppend.append(x)
						listToAppend.append(y)
						listOfMoves.append(listToAppend)
	
					elif ((BoardList[x-1][y+1]%2 != BoardList[x][y]%2) & (x-2 > -1) & (y+2 < 8)):
						if(BoardList[x-2][y+2] == "  "):
							BoardList[x-2][y+2] == BoardList[x][y]
							listToAppend = []
							listXY = []
							listXY.append(x-2)
							listXY.append(y+2)
							listJumped = []
							listJumped.append(BoardList[x-1][y+1])
							listToAppend.append(listXY)
							listToAppend.append(listJumped)
							fitness = 3
							listToAppend.append(fitness)
							listToAppend.append(x)
							listToAppend.append(y)
							listOfMoves.append(listToAppend)
							######APPEND CURRENT SOLUTION THEN ADD MORE recursively
							recursiveAiEngine(x-2,y+2, listJumped, listToAppend, fitness, x, y)
							###########recursive plus list########## LEFT JUMP
							BoardList[x-2][y+2] == "  "
	
				if((x-1 > -1) & (y-1 > -1)):
					if(BoardList[x-1][y-1] == "  "):
						listToAppend = []
						listXY = []
						listJumped = []
						listXY.append(x-1)
						listXY.append(y-1)
						listToAppend.append(listXY)
						listToAppend.append(listJumped)#done LEFT UPPER
						fitness = 1
						listToAppend.append(fitness)
						listToAppend.append(x)
						listToAppend.append(y)
						listOfMoves.append(listToAppend)
	
					elif ((x-2 > -1) & (y-2 > -1) & (BoardList[x-1][y+1]%2 != BoardList[x][y]%2)):
						if(BoardList[x-2][y+2] == "  "):
							BoardList[x-2][y+2] == BoardList[x][y]
							listToAppend = []
							listXY = []
							listXY.append(x-2)
							listXY.append(y+2)
							listJumped = []
							listJumped.append(BoardList[x-1][y+1])
							listToAppend.append(listXY)
							listToAppend.append(listJumped)
							fitness = 3
							listToAppend.append(fitness)
							listToAppend.append(x)
							listToAppend.append(y)
							listOfMoves.append(listToAppend)
							######APPEND CURRENT SOLUTION THEN ADD MORE recursively
							recursiveAiEngine(x-2,y+2, listJumped, listToAppend, fitness, x, y)
							############recursive plus list########## LEFT JUMP
							BoardList[x-2][y+2] == "  "

	return listOfMoves

def recursiveAiEngine(x,y, removedList, listToAdd, fitnessIn, xOriginal, yOriginal):
	
	tempRemoved = removedList


	if (x+2 < 8) & (y-2 > -1):
		if BoardList[x+1][y-1] != "  " and BoardList[x][y] != "  ":
			if BoardList[x+1][y-1]%2 != BoardList[x][y]%2:
				if(BoardList[x+2][y-2] == "  "):
					BoardList[x+2][y-2] == BoardList[x][y]
					listToAppend = []
					listXY = []
					listXY.append(x+2)
					listXY.append(y-2)
					tempRemoved.append(BoardList[x+1][y-1])
					listToAppend.append(listXY)
					listToAppend.append(tempRemoved)
					fitnessIn += 3
					listToAppend.append(fitnessIn)
					listToAppend.append(xOriginal)
					listToAppend.append(yOriginal)
					listToAdd.append(listToAppend)
					######APPEND CURRENT SOLUTION THEN ADD MORE recursively
					recursiveAiEngine(x+2,y-2, tempRemoved, listToAdd, fitnessIn, xOriginal, yOriginal)
					############recursive plus list########## LEFT JUMP
					BoardList[x+2][y-2] == "  "

	tempRemoved = removedList


	if((x+1 < 8) & (y+1 < 8)):
		if BoardList[x+1][y+1] != "  " and BoardList[x][y] != "  ":						#### ADDED ###########################################################################
			if ((BoardList[x+1][y+1]%2 != BoardList[x][y]%2) & (x+2 < 8) & (y+2 < 8)):
				if(BoardList[x+2][y+2] == "  "):
					BoardList[x+2][y+2] == BoardList[x][y]
					listToAppend = []
					listXY = []
					listXY.append(x+2)
					listXY.append(y+2)
					tempRemoved.append(BoardList[x+1][y+1])
					listToAppend.append(listXY)
					listToAppend.append(tempRemoved)
					fitnessIn += 3
					listToAppend.append(fitnessIn)
					listToAppend.append(xOriginal)
					listToAppend.append(yOriginal)
					listToAdd.append(listToAppend)
					######APPEND CURRENT SOLUTION THEN ADD MORE recursively
					recursiveAiEngine(x+2,y+2, tempRemoved, listToAdd, fitnessIn, xOriginal, yOriginal)
					###########recursive plus list##########
					BoardList[x+2][y+2] == "  "





	############add over 50
	tempRemoved = removedList
	if BoardList[x][y] != "  ":
		if(int(BoardList[x][y]) > 49):
			tempRemoved = removedList
			if (x-2 > -1) & (y+2 < 8):
				if BoardList[x-1][y+1] != "  " and BoardList[x][y] != "  ":
					if (BoardList[x-1][y+1]%2 != BoardList[x][y]%2):
						if(BoardList[x-2][y+2] == "  "):
							BoardList[x-2][y+2] == BoardList[x][y]
							listToAppend = []
							listXY = []
							listXY.append(x-2)
							listXY.append(y+2)
							tempRemoved.append(BoardList[x-1][y+1])
							listToAppend.append(listXY)
							listToAppend.append(tempRemoved)
							fitnessIn += 3
							listToAppend.append(fitnessIn)
							listToAppend.append(xOriginal)
							listToAppend.append(yOriginal)
							listToAdd.append(listToAppend)
							######APPEND CURRENT SOLUTION THEN ADD MORE recursively
							recursiveAiEngine(x-2,y+2, tempRemoved, listToAdd, fitnessIn, xOriginal, yOriginal)
							############recursive plus list##########
							BoardList[x-2][y+2] == "  "


		tempRemoved = removedList

		if((x-1 > -1) & (y-1 > -1)):#bottom left
			if BoardList[x-1][y-1] != "  " and BoardList[x][y] != "  ":
				if ((BoardList[x-1][y-1]%2 != BoardList[x][y]%2) & (x-2 > -1) & (y-2 > -1)):
					if(BoardList[x-2][y-2] == "  "):
						BoardList[x-2][y-2] == BoardList[x][y]
						listToAppend = []
						listXY = []
						listXY.append(x-2)
						listXY.append(y-2)
						tempRemoved.append(BoardList[x-1][y-1])
						listToAppend.append(listXY)
						listToAppend.append(tempRemoved)
						fitnessIn += 3
						listToAppend.append(fitnessIn)
						listToAppend.append(xOriginal)
						listToAppend.append(yOriginal)
						listToAdd.append(listToAppend)
						######APPEND CURRENT SOLUTION THEN ADD MORE recursively
						recursiveAiEngine(x-2,y-2, tempRemoved, listToAdd, fitnessIn, xOriginal, yOriginal)
						###########recursive plus list########## LEFT JUMP
						BoardList[x-2][y-2] == "  "
	return


def validateBoard(mod):#Kings pieces and returns false if game is over DONE
	for x in range(8):
		if (BoardList[0][x] != "  "):
			if (BoardList[0][x]%2 == 0) & (BoardList[0][x] < 50):
				BoardList[0][x] = int(BoardList[0][x]) + 40
		if (BoardList[7][x] != "  "):
			if (BoardList[7][x]%2 == 1) & (BoardList[7][x] < 50):
				BoardList[7][x] = int(BoardList[7][x] + 40)

	for x in BoardList:
		for y in x:
			if y != "  ":
				if y%2 == mod:
					return False
	return True
	
def playerTurn():
	# find all possible moves
	pieces = {}
	for x in range(8):
		for y in range(8):
			if BoardList[x][y] != "  " and int(BoardList[x][y]) % 2 == 0:
				pieces[BoardList[x][y]] = [x, y]
	
	# make the player choose from possible pieces
	piece = 0
	moves = []
	while piece not in pieces.keys() or len(moves) == 0:
		print("Options: ", end="")
		print(", ".join(str(key) for key in pieces.keys()))
		
		piece = int(input("Select a piece: "))
		
		if piece in pieces.keys():
			# generate moves for pieces
			x = pieces[piece][0]
			y = pieces[piece][1]
			moves = recursivePlayerPrimer(x, y)
			
			if len(moves) == 0:
				print("That piece can't move!", end="\n\n")
	
	# print available moves
	print ("Moves [y, x]: ")
	move_num = 1
	for move in moves:
		print (str(move_num) + ". [" + str(move[0][0]+1) + "," + str(move[0][1]+1) + "]")
		move_num += 1
	print()
	
	# have the player select a move
	move = 0
	while move not in range(1, len(moves)+1):
		move = int(input("Select a move: "))
	
	new_x = moves[move-1][0][0]
	new_y = moves[move-1][0][1]
	
	temp = BoardList[x][y]
	BoardList[x][y] = "  "
	BoardList[new_x][new_y] = temp
	
		# removal code
	for piece in moves[move-1][1]:
		for x in range(8):
			for y in range(8):
				if BoardList[x][y] == piece:
					BoardList[x][y] = "  "
	
# [[x,y], [removed], fitness, x, y]
def AIturn():
	listOfAI = []

	for x in range (8):
		for y in range (8):
			if BoardList[x][y] != "  ":
				if BoardList[x][y]%2 == 1:
					tempList = recursiveAiPrimer(x,y)
					
					max_fit = -1
					max_move = []
					for move in tempList:
						if move[2] > max_fit:
							max_fit = move[2]
							max_move = move
							
					listOfAI.append(max_move)
	
	max_fit = -1
	max_move = []
	for move in listOfAI:
		if len(move) > 0:
			if move[2] > max_fit:
				max_fit = move[2]
				max_move = move
	
	new_x = max_move[0][0]
	new_y = max_move[0][1]
	
	temp = BoardList[max_move[3]][max_move[4]]
	BoardList[max_move[3]][max_move[4]] = "  "
	BoardList[new_x][new_y] = temp
	
	# removal code
	for piece in max_move[1]:
		for x in range(8):
			for y in range(8):
				if BoardList[x][y] == piece:
					print ("AI took " + str(piece))
					BoardList[x][y] = "  "


def runGame():

	populateBoard()
	displayBoard()
	winner = 0
	while(winner == 0):
		playerTurn()
		if validateBoard(0):
			winner = 1
			break
		displayBoard()
		AIturn()
		
		print ("AI Turn:")
		displayBoard()
		if validateBoard(1):
			winner = 2

	displayBoard()

runGame()