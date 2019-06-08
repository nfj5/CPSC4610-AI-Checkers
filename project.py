

BoardList = []


for i in range(8):
	BoardListTemp = []
	for x in range(8):
		BoardListTemp.append("  ")
	BoardList.append(BoardListTemp)


def displayBoard():
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


def populateBoard():
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
			
def isValidMove(x,y,modulus, proX, proY):
	if(BoardList[proX][proY] == "  "):
		return [True, proX, proY]
	if((BoardList[proX][proY]%2) != modulus):
		if(BoardList[proX+(proX-X)])

def moveForTurn():


def AIturn():

def runGame():


	

#Add valid move check
#add Move
#add turn order
#User input

populateBoard()


displayBoard()














