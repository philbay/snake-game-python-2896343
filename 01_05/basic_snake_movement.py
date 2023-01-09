# Import the Turtle Graphics module
import turtle

# Define program constants
WIDTH = 500
HEIGHT = 500
DELAY = 400 # Milliseconds

def move_snake():
    stamper.clearstamps() # remvoe existing stamps made by stamper
    new_head = snake[-1].copy()
    new_head[0] += 20

    # add new head to sanke body
    snake.append(new_head)

    # remove last segment
    snake.pop(0)

    for segment in snake:
        stamper.goto(segment[0], segment[1])
        stamper.stamp()

    # Refresh screen
    screen.update()

    # RINSE and
    turtle.ontimer(move_snake, DELAY)

# Create a window where we will do our drawing.
screen = turtle.Screen()
screen.setup(WIDTH, HEIGHT)  # Set the dimensions of the Turtle Graphics window.
screen.title("Snake")
screen.bgcolor("pink")
screen.tracer(0) # Turn off automatic animation

# Create a turtle to do your bidding
stamper = turtle.Turtle()
stamper.shape("square")
stamper.penup()

# create snake rep
snake = [[0,0],[20,0],[40,0],[60,0]]

for segment in snake:
    stamper.goto(segment[0], segment[1])
    stamper.stamp()

move_snake()

# Finish nicely
turtle.done()
