AI Checkers

Nick Jones (jonesn6@seattleu.edu)
Will Lathrop (lathropw@seattleu.edu)

RUN THE CODE:
	python3 project.py

THE ALGORITHM:
	For our algorithm, we calculate the fitness of every potential move for each piece on the board (generating a tree of all possible moves).
	We then pick the best move for each piece using DFS and then choose the piece with the "fittest" move.