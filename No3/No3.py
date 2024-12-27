import turtle as t

class Disk(object):
    def __init__(self, name="", xpos=0, ypos=0, height=20, width=40):
        self.dname = name
        self.dxpos = xpos
        self.dypos = ypos
        self.dheight = height
        self.dwidth = width

    def showdisk(self):
        t.penup()
        t.goto(self.dxpos, self.dypos)
        t.setheading(0)
        t.pendown()
        t.begin_fill()
        for _ in range(2):
            t.fd(self.dwidth)
            t.left(90)
            t.fd(self.dheight)
            t.left(90)
        t.end_fill()

    def newpos(self, xpos, ypos):
        self.cleardisk()
        self.dxpos = xpos
        self.dypos = ypos
        self.showdisk()

    def cleardisk(self):
        t.penup()
        t.goto(self.dxpos, self.dypos)
        t.setheading(0)
        t.pendown()
        t.color("white")
        t.begin_fill()
        for _ in range(2):
            t.fd(self.dwidth)
            t.left(90)
            t.fd(self.dheight)
            t.left(90)
        t.end_fill()
        t.color("black")

class Pole(object):
    def __init__(self, name="", xpos=0, ypos=0, thick=10, length=100):
        self.pname = name
        self.stack = []
        self.toppos = 0
        self.pxpos = xpos
        self.pypos = ypos
        self.pthick = thick
        self.plength = length

    def showpole(self):
        t.penup()
        t.goto(self.pxpos, self.pypos)
        t.setheading(90)
        t.pendown()
        t.forward(self.plength)

    def pushdisk(self, disk):
        disk.newpos(self.pxpos - disk.dwidth / 2, self.pypos + len(self.stack) * disk.dheight)
        self.stack.append(disk)

    def popdisk(self):
        if self.stack:
            return self.stack.pop()
        return None


class Hanoi(object):
    def __init__(self, n=3, start="A", workspace="B", destination="C"):
        self.startp = Pole(start, 0, 0)
        self.workspacep = Pole(workspace, 150, 0)
        self.destinationp = Pole(destination, 300, 0)
        self.startp.showpole()
        self.workspacep.showpole()
        self.destinationp.showpole()

        for i in range(n):
            self.startp.pushdisk(Disk("d" + str(i), 0, i * 20, 20, (n - i) * 30))

    def move_disk(self, start, destination):
        disk = start.popdisk()
        destination.pushdisk(disk)

    def move_tower(self, n, s, d, w):
        if n == 1:
            self.move_disk(s, d)
        else:
            self.move_tower(n - 1, s, w, d)
            self.move_disk(s, d)
            self.move_tower(n - 1, w, d, s)

    def solve(self):
        self.move_tower(3, self.startp, self.destinationp, self.workspacep)
        t.done()  # Finish the turtle drawing


# Initialize Turtle window
t.speed(0)  # Set drawing speed to fastest
t.bgcolor("white")  # Set background color to white

# Solve the puzzle
h = Hanoi()
h.solve()
