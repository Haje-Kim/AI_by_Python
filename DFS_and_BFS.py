class State:
    def __init__(self, board, goal, moves=0):
        self.board = board
        self.moves = moves
        self.goal = goal

    # exchange i1 and i2 to return a new state 
    def get_new_board(self, i1, i2, moves):
        new_board = self.board[:]
        new_board[i1], new_board[i2] = new_board[i2], new_board[i1]
        return State(new_board, self.goal, moves)

    # expand child node, save in the list and return 
    def expand(self, moves):
        result = []
        i = self.board.index(0) # number 0's location 
        if not i in [0, 1, 2]:  # operator 'Up'
            result.append(self.get_new_board(i, i-3, moves))
        if not i in [0, 3, 6]:  # operator 'Left'
            result.append(self.get_new_board(i, i-1, moves))
        if not i in [2, 5, 8]:  # operator 'Right'
            result.append(self.get_new_board(i, i+1, moves))
        if not i in [6, 7, 8]:  # operator 'Down'
            result.append(self.get_new_board(i, i+3, moves))
        return result 

    # Use to print the instance 
    def __str__(self):
        return str(self.board[:3])+"\n"+str(self.board[3:6])+"\n"+str(self.board[6:])+"\n"+"------------"

# initial state 
puzzle =   [1, 2, 3,
            0, 4, 6,
            7, 5, 8]

# desired state 
goal =     [1, 2, 3,
            4, 5, 6,
            7, 8, 0]

# open list 
open_queue = []
open_queue.append(State(puzzle, goal))

closed_queue = []
moves = 0

searchType = int(input("1. Breadth-First Search.     2. Depth-First Search.     :"))

while len(open_queue) != 0:

    current = open_queue.pop(0)
    print(current)

    if current.board == goal:
        print('탐색 성공')
        print("number of moves:", moves)
        break

    moves = current.moves+1
    closed_queue.append(current)

    for state in current.expand(moves):
        if(state in closed_queue) or (state in open_queue): # if the node was already used 
            continue    # keep going 
        else:
            if searchType == 1: 
                open_queue.append(state) 
            # elif searchType == 2:
            #     open_queue.insert(0, state)
