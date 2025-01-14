# Import the Turtle Graphics module
import turtle

# Define program constants
WIDTH = 500
HEIGHT = 500
DELAY = 500  # Milliseconds

offsets = {
    "Up":(0,20),
    "Down":(0,-20),
    "Left":(-20,0),
    "Right":(20,0)
}

def go_up():
    global snake_direction
    if snake_direction != "Down":
        snake_direction = "Up"

def go_right():
    global snake_direction
    if snake_direction != "Left":
        snake_direction = "Right"

def go_down():
    global snake_direction
    if snake_direction != "Up":
        snake_direction = "Down"

def go_left():
    global snake_direction
    if snake_direction != "Right":
        snake_direction = "Left"


def game_loop():
    stamper.clearstamps()  # Remove existing stamps made by stamper.

    new_head = snake[-1].copy()
    new_head[0] += offsets[snake_direction][0]
    new_head[1] += offsets[snake_direction][1]

    # check collisions
    if new_head in snake or new_head[0] < -WIDTH / 2 or new_head[0] > WIDTH / 2 \
        or new_head[1] <- HEIGHT / 2 or new_head[1] > HEIGHT / 2:
        turtle.bye()
    else:
        # Add new head to snake body.
        snake.append(new_head)

        # Remove last segment of snake.
        snake.pop(0)

        # Draw snake for the first time.
        for segment in snake:
            stamper.goto(segment[0], segment[1])
            stamper.stamp()

        # Refresh screen
        screen.update()

        # Rinse and repeat
        turtle.ontimer(game_loop, DELAY)


# Create a window where we will do our drawing.
screen = turtle.Screen()
screen.setup(WIDTH, HEIGHT)  # Set the dimensions of the Turtle Graphics window.
screen.title("Snake")
screen.bgcolor("pink")
screen.tracer(0)  # Turn off automatic animation.

# Event handlers
screen.listen()
screen.onkey(go_up, "Up")
screen.onkey(go_right, "Right")
screen.onkey(go_down, "Down")
screen.onkey(go_left, "Left")

# Create a turtle to do your bidding
stamper = turtle.Turtle()
stamper.shape("square")
stamper.penup()

# Create snake as a list of coordinate pairs.
snake = [[0, 0], [20, 0], [40, 0], [60, 0]]
snake_direction = "Up"

# Draw snake for the first time.
for segment in snake:
    stamper.goto(segment[0], segment[1])
    stamper.stamp()

# Set animation in motion
game_loop()

# Finish nicely
turtle.done()
