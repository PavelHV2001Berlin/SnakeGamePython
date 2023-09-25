from turtle import Turtle
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
class Snake:
    def __init__(self):
        self.turtles = []
        self.create_snake()
        self.head = self.turtles[0]
    def create_snake(self):
        for i in range(3):
            self.addSegment(((20-i*20),0))
         
    def addSegment(self, position):
           t1 = Turtle()
           t1.color("white")
           t1.penup()
           t1.shape("square")
           t1.goto(position)
           self.turtles.append(t1)
        
    def move(self):
        for i in range(len(self.turtles)-1, 0,-1):
            new_x = self.turtles[i -1].xcor()
            new_y = self.turtles[i -1].ycor()
            self.turtles[i].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)
       # self.head.left(90)
    def up(self):
        if not(self.head.heading() == DOWN):
            self.head.setheading(UP)
    def down(self):
        if not(self.head.heading() == UP):
            self.head.setheading(DOWN)

    def left(self):
        if not(self.head.heading() == RIGHT):
            self.head.setheading(LEFT)

    def right(self):
        if not(self.head.heading() == LEFT):
            self.head.setheading(RIGHT)
    def extend(self):
        self.addSegment(self.turtles[-1].position())

        
