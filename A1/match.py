import Queue


class Board:

    def __init__(self):
        self.board = [range(1, 5), range(5, 9), range(9, 13), range(13, 16) + ['*']]
        self.goal = []
        for i in self.board:
            self.goal.append(tuple(i))
        self.goal = tuple(self.goal)
        self.empty = [3, 3]

    def match(self, copy):
            a = Board()
            a.board = copy
            for row in range(0, 4):
                for col in range(0, 4):
                    if a.board[row][col] == '*':
                        a.empty = [row, col]
            result = []
            for i in a.board:
                result.append(list(i))
            a.board = result
            return a

    def solve(self):

        start = self.convert_to_tuple(self.board)
        pred = {}
        visited = []
        frontier = Queue.Queue()
        frontier.put(start)

        while frontier.qsize() > 0:
            tmp = frontier.get()

            if tmp not in visited:
                visited.append(tmp)
                tmpboard = self.match(tmp)
                print tmpboard
                tmpboard.move_up()
                if self.convert_to_tuple(tmpboard.board) != tmp:
                    frontier.put(self.convert_to_tuple(tmpboard.board))
                    if not pred.has_key(self.convert_to_tuple(tmpboard.board)):
                        pred[self.convert_to_tuple(tmpboard.board)]=[tmp, 'up']
