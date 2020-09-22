
import turtle
import time
import random

#To slow down the movement of the snake
delay=0.1

#Score
score = 0
high_score = 0

#SET UP OF THE SCREEN
#.Screen used to create a window
wn = turtle.Screen()
#Giving the window a name
wn.title("Snake Game by DuncanScu")
#Giving the window a background colour
wn.bgcolor("green")
#Setting up the height and width for the window
wn.setup(width=600, height=600)
#Turning off screen updates
wn.tracer(0)

#Snake Head
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("black")
head.penup()
head.goto(0,0)
head.direction = "stop"

#Functions to move the snake
def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)
 
    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)
 
    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)
 
    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)


#Defining a function for each direction
def go_up():
    if head.direction != "down":
        head.direction = "up"
 
def go_down():
    if head.direction != "up":
        head.direction = "down"
 
def go_right():
    if head.direction != "left":
        head.direction = "right"
 
def go_left():
    if head.direction != "right":
        head.direction = "left"



#Adding function so the snake listenes to our control keys
wn.listen()
wn.onkey(go_up, "w")
wn.onkey(go_down, "s")
wn.onkey(go_right, "d")
wn.onkey(go_left, "a")

#Adding Items into the game
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.shapesize(0.50, 0.50)
food.goto(0,100)

segments = []

#Add scoring
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Score: 0 High Score: {}".format(high_score), align="center", font=("Courier", 24, "normal"))

#Main Game Loop
while True:
    wn.update()

    #Collision Checking for boarders
    if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
        time.sleep(1)
        head.goto(0, 0)
        head.direction = "stop" #Snake dies and stops moving

        for segment in segments:   #Have to hide the segments
            segment.goto(1000, 1000)
            segment=[]

    #When the food and head come into contact
    #Food is moved to the next random postion on the screen
    if head.distance(food) <15:
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        food.goto(x, y)

        # add a segment
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("grey")
        new_segment.penup()
        segments.append(new_segment)

        #Increase the score
        score += 10

        if score > high_score:
            high_score = score

        pen.clear()
        pen.write("score: {} High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))

    for index in range(len(segments)-1, 0, -1):
        x = segments[index -1].xcor()
        y = segments[index - 1].ycor()
        segments[index].goto(x, y)

    #Moving Segment 0 to where the head is
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x,y)

    move()
    
    #Checking for body collisions
    for segment in segments:
        if segment.distance(head)<20:
            time.sleep(1)
            head.goto(0,0)
            head.direction= "stop"
            for segment in segments:
                segment.goto(1000,1000)

            segment.clear()

            #Reset the score
            score = 0
            #Reset the delay
            delay = 0.1

            #Update the score display
            pen.clear()
            pen.write("Score: {} High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))

    time.sleep(delay)
wn.mainloop()