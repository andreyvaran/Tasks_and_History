class Robot():
    def __init__(self, start):
        self.start = start
        self.arrmove = []
        x, y = self.start
        self.arrmove.append((x, y))

    def move(self, str):
        movearr = list(str)
        self.arrmove = []
        x, y = self.start
        self.arrmove.append((x, y))
        for i in movearr:
            if (i == "N"):
                y += 1
                self.arrmove.append((x, y))
            elif (i == "S"):
                y -= 1
                self.arrmove.append((x, y))
            elif (i == "W"):
                x -= 1
                self.arrmove.append((x, y))
            elif (i == "E"):
                x += 1
                self.arrmove.append((x, y))

        self.start = (x, y)
        return self.start

    def path(self):
        return self.arrmove


r = Robot((0, 0))
print(r.move('NENW'))
print(*r.path())
