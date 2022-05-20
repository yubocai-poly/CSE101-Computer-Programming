class Point:
    """Encodes a live point in the Game of Life.
    Data attributes:
    x -- x-coordinate
    y -- y-coordinate
    """
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f'Point({self.x}, {self.y})'

    def __eq__(self, other):
        if self.x == other.x and self.y == other.y:
            return True
        else:
            return False

    def __hash__(self):
        return hash((self.x, self.y))

    def get_neighbors(self):
        """Return the neighbors of the Point as a set."""
        return {
            Point(self.x - 1, self.y - 1),
            Point(self.x - 1, self.y),
            Point(self.x - 1, self.y + 1),
            Point(self.x, self.y - 1),
            Point(self.x, self.y + 1),
            Point(self.x + 1, self.y - 1),
            Point(self.x + 1, self.y),
            Point(self.x + 1, self.y + 1),
        }


class Board:
    """A board to play the Game of Life on.
    Data attributes:
    points -- a set of Points
    x_size  -- size in x-direction
    y_size  -- size in y-direction
    """
    def __init__(self, x_size, y_size, points):
        self.points = points
        self.x_size = x_size
        self.y_size = y_size

    def is_legal(self, point):
        """Check if a given Point is on the board."""
        if point.x < 0 or point.y < 0 or self.x_size <= point.x or self.y_size <= point.y:
            return False
        else:
            return True

    def number_live_neighbors(self, p):
        """Compute the number of live neighbors of p on the Board."""
        list = []
        for people in p.get_neighbors():
            if people in self.points:
                list.append(people)
        return len(list)

    def next_step(self):
        """Compute the points alive in the next round and update the
        points of the Board.
        """
        next_alive = set()
        next_dead = set()

        for i in range(self.x_size):
            for j in range(self.y_size):
                point_alive = Point(i, j) in self.points
                number = self.number_live_neighbors(Point(i, j))
                if number < 2:  # Rules 1
                    next_dead.add(Point(i, j))
                elif point_alive and (number == 2 or number == 3):  # Rules 2
                    #I first try to write number == 2 or 3 but failed in test 3 and TA gave me a hint to solve it
                    next_alive.add(Point(i, j))
                elif not point_alive and number == 2:  # Rules 3
                    next_dead.add(Point(i, j))
                elif not point_alive and number == 3:  # Rules 4
                    next_alive.add(Point(i, j))
                elif number > 3:  # Rules 5
                    next_dead.add(Point(i, j))

        self.points = next_alive

    def load_from_file(self, filename):
        """Load a board configuration from file in the following format:
        - The first two lines contain a number representing the size in
            x- and y-coordinates, respectively.
        - Each of the following lines gives the coordinates of a single
            point, with the two coordinate values separated by a comma.
            Those are the points that are alive on the board.
        """

        with open(filename, 'r') as file:
            self.x_size = int(file.readline())  # Line 0
            self.y_size = int(file.readline())  # Line 1
            for line in file:
                sep_list = line.split(',')
                x = int(sep_list[0].strip())
                y = int(sep_list[1].strip())
                self.points.add(Point(x, y))

    def toggle_point(self, x, y):
        """Add Point(x,y) if it is not in points, otherwise delete it
        from points.
        """
        point = Point(x, y)
        if point in self.points:
            self.points.remove(point)
        else:
            self.points.add(point)

def is_periodic(board):
    """
    Return (True, 0) if the input board is periodic, otherwise (False, i),
    where i is the smallest index of the state to which it loops
    """
    # I didn't come up with this questions and this is the hint from Junyuan Wang
    list = [board.points]
    i = 1
    while True:
        board.next_step()
        if board.points == list[0]:
            return (True, 0)
        elif board.points in list:
            return (False, list.index(board.points))

        list.append(board.points)
        i += 1
