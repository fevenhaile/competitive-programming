class Robot:
    def __init__(self, width: int, height: int):
        self.labels = ["East", "North", "West", "South"]
        self.x = 0
        self.y = 0
        self.col = width
        self.row = height
        self.dir = 0
        self.direction = [(1, 0), (0, 1), (-1, 0), (0, -1)]

    def step(self, num: int) -> None:
        num %= (self.col - 1 + self.row - 1) * 2
        if num == 0:
            num += (self.col - 1 + self.row - 1) * 2
        for _ in range(num):
            tempx = self.x + self.direction[self.dir][0]
            tempy = self.y + self.direction[self.dir][1]
            while not (0 <= tempx < self.col and 0 <= tempy < self.row):
                self.dir = (self.dir + 1) % 4
                tempx = self.x + self.direction[self.dir][0]
                tempy = self.y + self.direction[self.dir][1]
            self.x = tempx
            self.y = tempy

    def getPos(self) -> List[int]:
        return [self.x, self.y]

    def getDir(self) -> str:
        return self.labels[self.dir]