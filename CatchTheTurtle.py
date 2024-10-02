import turtle
import random

# Setup screen
screen = turtle.Screen()
screen.bgcolor("yellow")
screen.title("Catch The Turtle")
FONT1 = ("Roboto", 25, "bold")
score = 0
game_over = False

# Turtle list
turtle_list = []

# Score turtle
score_turtle = turtle.Turtle()

# Countdown turtle
count_down_turtle = turtle.Turtle()

# Setup score turtle
def setup_score_turtle():
    score_turtle.hideturtle()
    score_turtle.color("black")
    score_turtle.penup()

    top_height = screen.window_height() / 2
    y = top_height - top_height / 10 
    score_turtle.setpos(0, y)
    score_turtle.write(arg="Score: 0", move=False, align="center", font=FONT1)

grid_size = 50  # Changed grid size for better turtle visibility

# Function to create a turtle at a grid position
def make_turtle(x, y):
    t = turtle.Turtle()

    # Define click handler
    def handle_click(x, y):
        global score
        score += 1
        score_turtle.clear()  # Clear previous score before updating
        score_turtle.write(arg="Score: {}".format(score), move=False, align="center", font=FONT1)

    t.onclick(handle_click)
    t.penup()
    t.shape("turtle")
    t.shapesize(2, 2)
    t.color("green")
    t.goto(x * grid_size, y * grid_size)
    turtle_list.append(t)

# Coordinates for turtles
x_coordinates = [-2, -1, 0, 1, 2]
y_coordinates = [2, 1, 0, -1, -2]

# Setup turtles on screen
def setup_turtles():
    for x in x_coordinates:
        for y in y_coordinates:
            make_turtle(x, y)

# Hide all turtles
def hide_turtles():
    for t in turtle_list:
        t.hideturtle()

# Show turtles randomly
def show_turtles_randomly():
    if not game_over:
        hide_turtles()
        random.choice(turtle_list).showturtle()
        screen.ontimer(show_turtles_randomly, 500)

# Countdown timer
def countdown(time):
    global game_over
    top_height = screen.window_height() / 2
    y = top_height - top_height / 10
    count_down_turtle.hideturtle()
    count_down_turtle.penup()
    count_down_turtle.setpos(0, y - 40)
    count_down_turtle.clear()

    if time > 0:
        count_down_turtle.write(arg="Time: {}".format(time), move=False, align="center", font=FONT1)
        screen.ontimer(lambda: countdown(time - 1), 1000)
    else:
        game_over = True
        hide_turtles()
        count_down_turtle.write(arg="Game Over!", align="center", font=FONT1)

# Start the game
def start_game_up():
    global game_over, score
    game_over = False
    score = 0
    turtle.tracer(0)
    setup_score_turtle()
    setup_turtles()
    hide_turtles()
    show_turtles_randomly()
    countdown(10)
    turtle.tracer(1)

# Start the game
start_game_up()
turtle.mainloop()
