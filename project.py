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
		if(BoardList[y-1][x+1] == "  "):
			listToAppend = []
			listXY = []
			listJumped = []
			listXY.append(x-1)
			listXY.append(y+1)
			listToAppend.append(listXY)
			listToAppend.append(listJumped)#done LEFT UPPER
			listOfMoves.append(listToAppend)

		elif ((x-2 > -1) & (y-2 > -1) & (BoardList[x-1][y-1]%2 != BoardList[x][y]%2)):
			if(BoardList[x-2][y-2] == "  "):
				BoardList[x-2][y-2] == BoardList[x][y]
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
				recursivePlayerEngine(x-2,y-2, listJumped, listToAppend)
				############recursive plus list########## LEFT JUMP
				BoardList[x-2][y-2] == "  "

	if((x+1 < 8) & (y-1 > -1)):
		if(BoardList[x+1][y-1] == "  "):
			listToAppend = []
			listXY = []
			listJumped = []
			listXY.append(x+1)
			listXY.append(y-1)
			listToAppend.append(listXY)
			listToAppend.append(listJumped)#done RIGHT UPPER
			listOfMoves.append(listToAppend)

		elif ((BoardList[x+1][y-1]%2 != BoardList[x][y]%2) & (x+2 < 8) & (y-2 > -1)):
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
				###########recursive plus list########## 
				BoardList[x-2][y-2] == "  "
		#########################################OVER 50 SPEARATION
		if(BoardList[x][y] > 49):
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
						listOfMoves.append(listToAppend)
						######APPEND CURRENT SOLUTION THEN ADD MORE recursively
						recursivePlayerEngine(x+2,y+2, listJumped, listToAppend)
						###########recursive plus list########## LEFT JUMP
						BoardList[x-2][y+2] == "  "

			if((x-1 > -1) & (y+1 < 8)):
				if(BoardList[x-1][y+1] == "  "):
					listToAppend = []
					listXY = []
					listJumped = []
					listXY.append(x-1)
					listXY.append(y+1)
					listToAppend.append(listXY)
					listToAppend.append(listJumped)#done LEFT UPPER
					listOfMoves.append(listToAppend)

				elif ((x-2 > -1) & (y+2 > -1) & (BoardList[x-1][y+1]%2 != BoardList[x][y]%2)):
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
						############recursive plus list########## LEFT JUMP
						BoardList[x-2][y+2] == "  "

	return listOfMoves

def recursivePlayerEngine(x,y, removedList, listToAdd):

	tempRemoved = removedList

	if((x-1 > -1) & (y+1 < 8)):
		if ((x-2 > -1) & (y+2 < 8) & (BoardList[x-1][y+1]%2 != BoardList[x][y]%2)):
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
				############recursive plus list########## LEFT JUMP
				BoardList[x-2][y+2] == "  "

	tempRemoved = removedList


	if((x+1 < 8) & (y+1 < 8)):
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
				listToAdd.append(listToAppend)
				######APPEND CURRENT SOLUTION THEN ADD MORE recursively
				recursivePlayerEngine(x+2,y+2, tempRemoved, listToAdd)
				###########recursive plus list########## 
				BoardList[x-2][y+2] == "  "





	############add over 50
	tempRemoved = removedList
	if(BoardList[x][y] > 49):
		tempRemoved = removedList
		if ((x-2 > -1) & (y-2 > -1) & (BoardList[x-1][y-1]%2 != BoardList[x][y]%2)):
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
				############recursive plus list##########
				BoardList[x-2][y-2] == "  "


		tempRemoved = removedList

		if((x+1 < 8) & (y-1 > -1)):#bottom left
			if ((BoardList[x+1][y-1]%2 != BoardList[x][y]%2) & (x+2 < 8) & (y-2 > -1)):
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
					BoardList[x-2][y-2] == "  "
	return







def validateBoard(mod):#Kings pieces and returns false if game is over DONE
	for x in range(8):
		if((BoardList[0][x]%2 == 0) & (BoardList[0][x] < 50)):
			BoardList[0][x] = BoardList[0][x] + 40
		if((BoardList[7][x]%1 == 0) & (BoardList[7][x] < 50)):
			BoardList[7][x] = BoardList[0][x] + 40

	for x in BoardList:
		for y in x:
			if(y != "  "):
				if(y%mod != 0):
					return True
	return False


def moveForTurn():
	return

def AIturn():
	listOfAI = []

	for x in range (8):
		for y in range (8):
			if BoardList[x][y]%2 == 1:
				tempList = recursiveAIPrimer(x,y)
				#listOfAI.
				
	return


def runGame():

	populateBoard()
	displayBoard()
	winner = 0
	while(winner == 0):
		playerTurn()
		if(validateBoard(1) == False):
			winner = 1
			break
		displayBoard()
		AIturn()
		if(validateBoard(2) == False):
			winner = 2

	displayBoard()

#Add valid move check
#add Move
#add turn order
#User input

populateBoard()
displayBoard()
