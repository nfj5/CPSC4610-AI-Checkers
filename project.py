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

	tempRemoved = removedList

	if((x-1 > -1) & (y+1 < 8):
		if(boardList[x-1][y+1] == "  "):
			listToAppend = []
			listXY = []
			listJumped = []
			listXY.append(x-1)
			listXY.append(y+1)
			listToAppend.append(listXY)
			listToAppend.append(listJumped)#done LEFT UPPER
			listOfMoves.append(listToAppend)

	else if((x-2 > -1) & (y+2 < 8) & (boardList[x-1][y+1]%2 != boardList[x][y]%2)):
		if(boardList[x-2][y+2] == "  "):
			boardList[x-2][y+2] == boardList[x][y]
			tempRemoved.append(boardList[x+1][y+1])
			listToAppend = []
			listXY = []
			listXY.append(x-2)
			listXY.appennd(y+2)
			listJumped = []
			listJumped.append(boardList[x-1][y+1])
			listToAppend######APPEND CURRENT SOLUTION THEN ADD MORE recursively
			recursivePlayerEngine(x-2,y+2, tempRemoved, listToAppend)

			############recursive plus list########## LEFT JUMP
			boardList[x-2][y+2] == "  "

	tempRemoved = removedList

	if((x+1 < 8) & (y+1 < 8):
		if(boardList[x+1][y+1] == "  "):
			listToAppend = []
			listXY = []
			listJumped = []
			listXY.append(x+1)
			listXY.append(y+1)
			listToAppend.append(listXY)
			listToAppend.append(listJumped)#done RIGHT UPPER
			listOfMoves.append(listToAppend)

		else if((boardList[x+1][y+1]%2 != boardList[x][y]%2) & (x+2 < 8) & (y+2 < 8)):
			if(boardList[x+2][y+2] == "  "):
				boardList[x+2][y+2] == boardList[x][y]
				tempRemoved.append(boardList[x+1][y+1])



				####################recursive plus list########## RIGHT JUMP - copy above change numbers in coordinates
				boardList[x+2][y+2] == "  "


		##########################Add king functionality

def recursivePlayerEngine(x,y, removedList, listToAdd):

	tempRemoved = removedList
	##copy second part of above



	if(BoardList[x][y] > 50):
		tempRemoved = removedList

		if((x-1 > -1) & (y-1 > -1):
			if(boardList[x-1][y-1] == "  "):
				#nonrecursive return
			else if((boardList[x-1][y-1]%2 != boardList[x][y]%2) & (x-2 > -1) & (y-2 > -1)):
				if(boardList[x-2][y-2] == "  "):
					boardList[x-2][y-2] == boardList[x][y]
					tempRemoved.append(boardList[x+1][y-1])
					#recursive plus list
					boardList[x-2][y+2] == "  "

		tempRemoved = removedList

		if((x+1 < 8) & (y-1 > -1):
			if(boardList[x+1][y-1] == "  "):
				#no recursive end
			else if((boardList[x+1][y-1]%2 != boardList[x][y]%2) & (x-2 < 8) & (y-2 >0)):
				if(boardList[x+2][y+2] == "  "):
					boardList[x+2][y+2] == boardList[x][y]
					tempRemoved.append(boardList[x+1][y-1])
					#recursive plus list
					boardList[x+2][y+2] == "  "


	return 




def validateBoard(mod):#Kings pieces and returns false if game is over DONE
	for x in range(8):
		if((BoardList[0][x]%2 == 0) & (BoardList[0][x] < 50)):
			BoardList[0][x] = BoardList[0][x] + 40
		if((BoardList[7][x]%1 == 0) & (BoardList[7][x] < 50)):
			BoardList[7][x] = BoardList[0][x] + 40

	for x in BoardList:
		for y in x:
			if(y != " "):
				if(y%mod != 0):
					return True
	return False


def moveForTurn():


def AIturn():
	listOfAI = []

	for x in range (8):
		for y in range (8):
			if BoardList[x][y]%2 == 1:
				tempList = recursiveAIPrimer(x,y)
				listOfAI.


def runGame():

	populateBoard
	displayBoard
	winner = 0
	while(winner == 0):

		playerTurn():
		if(validateBoard(1) == False):
			winner = 1
			break
		displayBoard()
		AIturn()
		if(validateBoard(2) == False):
			winner = 2

	displayBoard()
	if()



	

#Add valid move check
#add Move
#add turn order
#User input

populateBoard()


displayBoard()














