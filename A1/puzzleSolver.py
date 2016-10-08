import sys
import heapq

class puzzleSolver(object):

    def __init__(self, board):
        self.goal_state = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 0]]
        self.actions = ['up', 'down', 'right', 'left']
        self.moves = dict(up=[-1, 0], right=[0, 1],
                          down=[1, 0], left=[0, -1])

        self.input_matrix = board
        self.m = len(board)
        self.n = len(board[0])

    def get_valid_moves(self, matrix):
        result = []
        x, y = -1, -1
        x, y = [[i, j] for i in range(self.m)
                        for j in range(self.n) if matrix[i][j] == 0][0]

        for action in self.actions:
            x2, y2 = x + self.moves[action][0], y + self.moves[action][1]

            next_move = None

            if (x2 >= 0) and (x2 < self.m) and (y2 >= 0) and (y2 < self.n):
                next_move = [row[:] for row in matrix]

                tmp = next_move[x][y]
                next_move[x][y] = next_move[x2][y2]
                next_move[x2][y2] = tmp

            if next_move is not None:
                result.append([next_move, action])

        return result

    def heuristics_misplaced_tiles(self, matrix):
        misplaced_count = 0

        for i in range(self.m):
            for j in range(self.n):
                if self.goal_state[i][j] != matrix[i][j]:
                    misplaced_count += 1

        return [misplaced_count, matrix]

    def heuristics_manhattan_distance(self, matrix):
        sum_mhd = 0
        for i in range(self.m):
            for j in range(self.n):
                if matrix[i][j] == 0:
                    continue
                row_distance = abs(i - int((matrix[i][j]-1) / self.m))
                col_distance = abs(j - ((matrix[i][j]-1) % self.n))
                sum_mhd += row_distance + col_distance
        return [sum_mhd, matrix]

    def solver(self, method=0):
        explored_states = []

        start = self.input_matrix

        frontier = []
        backtrack = []

        if method == 0:
            h_fn = self.heuristics_misplaced_tiles
        elif method == 1:
            h_fn = self.heuristics_manhattan_distance

        hnode = h_fn(start)
        hnode.append('')
        heapq.heappush(frontier, hnode)

        while len(frontier) > 0:
            (h, current_state, path) = heapq.heappop(frontier)
            if path != '':
                backtrack.append(path)

            if current_state in explored_states:
                continue

            explored_states.append(current_state)

            # check if current_state is goal_state
            # you have found your node
            if h == 0:
                break

            for move in self.get_valid_moves(current_state):
                hnode = h_fn(move[0])
                hnode.append(move[1])
                heapq.heappush(frontier, hnode)

        return backtrack


def read_input(f_name):
    m = []
    with open(f_name, 'r') as f:
        for line in f.readlines():
            line = line.strip('\n')
            row = [int('0'+x) for x in line.split(',')]
            m.append(row)
            print(row)
    return m

if __name__ == '__main__':
    filename = "answer.txt"
    matrix = read_input(filename)
    s = puzzleSolver(matrix)
    path = s.solver(0)
    # print(path)
    print(len(path))
    path = s.solver(1)
    # print(path)
    print(len(path))
