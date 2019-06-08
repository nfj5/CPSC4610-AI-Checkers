
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
			
def isValidMove(x,y,modulus, proX, proY):#in progress - FULL REDESIGN - make all valid moves a letter on the board then choose from all letters
	if(BoardList[proX][proY] == "  "):
		return [True, proX, proY]
	if((BoardList[proX][proY]%2) != modulus):
		if(BoardList[proX+(proX-X)])



def validateBoard(mod):#Kings pieces and returns false if game is over DONE / WATCH MODULUS
	for x in range(8):
		if((BoardList[0][x]%2 == 0) & (BoardList[0][x] < 50)):
			BoardList[0][x] = BoardList[0][x] + 40
		if((BoardList[7][x]%1 == 0) & (BoardList[7][x] < 50)):
			BoardList[7][x] = BoardList[0][x] + 40

	for x in BoardList:
		for y in x:
			if(y%mod != 0):
				return True
	return False


def moveForTurn():


def AIturn():



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









