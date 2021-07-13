import queue 

# State class, stores f(n) values.
class State:
    def __init__(self, board, goal, moves=0):
        self.board = board
        self.goal = goal
        self.moves = moves
    
    # Return new state after exchanging i1 and i2 
    def get_new_board(self, i1, i2, moves):
        new_board = self.board[:]
        new_board[i1], new_board[i2] = new_board[i2], new_board[i1]
        return State(new_board, self.goal, moves)
    
    # Expand child node, store it in a list and return 
    def expand(self, moves):
        result = []
        i = self.board.index(0)     # look for the index of '0' (empty)
        if not i in [0, 1, 2]: # 'UP'
            result.append(self.get_new_board(i, i-3, moves))
        if not i in [6, 7, 8]: # 'DOWN'
            result.append(self.get_new_board(i, i+3, moves))
        if not i in [0, 3, 6]: # 'LEFT'
            result.append(self.get_new_board(i, i-1, moves))
        if not i in [2, 5, 8]: # 'RIGHT'
            result.append(self.get_new_board(i, i+1, moves))
        return result

    # Calculate and return f(n)
    def f(self):
        return self.h()+self.g()

    # Calculate and return heuristic function value h(n)
    def h(self):
        return sum([1 if self.board[i] != self.goal[i] else 0 for i in range(8)])

    # Calculate and return heuristic function value g(n)
    def g(self):
        return self.moves

    # Define 'less than' operator to compare a state with another state 
    def __lt__(self, other):
        return self.f() < other.f()

    # Method to print out a state 
    def __str__(self):
        return "------------f(n)=" + str(self.f()) + '\n' + "------------h(n)=" + str(self.h()) + '\n' + "------------g(n)=" + str(self.g()) + '\n' + str(self.board[:3]) +'\n'+ str(self.board[3:6]) +'\n'+ str(self.board[6:]) +'\n'+ "------------"

puzzle = [1, 2, 3,
          0, 4, 6,
          7, 5, 8]

goal =   [1, 2, 3,
          4, 5, 6,
          7, 8, 0]

# Create pen list with priority queue
open_queue = queue.PriorityQueue()
open_queue.put(State(puzzle, goal))

closed_queue = []
moves = 0
while not open_queue.empty():
    current = open_queue.get()
    print(current)

    if current.board == goal:
        print('Search success!')
        break
    
    moves = current.moves+1

    for state in current.expand(moves):
        if state not in closed_queue:
            open_queue.put(state)
        closed_queue.append(current)
else:
    print('Search Failure')