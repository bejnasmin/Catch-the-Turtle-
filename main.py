import turtle
import random

screen = turtle.Screen()
screen.bgcolor("yellow")
screen.title("Catch the Turtle")

FONT = ("Arial", 24, "normal")

score = 0
game_over = False

turtle_list = []

score_turtle = turtle.Turtle()
countdown_turtle = turtle.Turtle()


def setup_score_turtle():
    score_turtle.hideturtle()
    score_turtle.color("dark blue")
    score_turtle.penup()

    top_height = screen.window_height() / 2
    y = top_height * 0.9

    score_turtle.setpos(0, y)

    score_turtle.write(
        arg="Score: 0",
        move=False,
        align="center",
        font=FONT
    )


grid_size = 10

x_coordinates = [-20, -10, 0, 10, 20]
y_coordinates = [20, 10, 0, -10]


def make_turtle(x, y):
    t = turtle.Turtle()

    def handle_click(x, y):
        global score

        if not game_over:
            score += 1

            t.hideturtle()

            score_turtle.clear()

            score_turtle.write(
                arg=f"Score: {score}",
                move=False,
                align="center",
                font=FONT
            )

    t.penup()
    t.shape("turtle")
    t.color("green")
    t.shapesize(2, 2)

    t.goto(
        x * grid_size,
        y * grid_size
    )

    t.onclick(handle_click)

    turtle_list.append(t)


def setup_turtles():
    for x in x_coordinates:
        for y in y_coordinates:
            make_turtle(x, y)


def hide_turtles():
    for t in turtle_list:
        t.hideturtle()


def show_turtle_randomly():
    if not game_over:
        hide_turtles()

        random.choice(
            turtle_list
        ).showturtle()

        screen.ontimer(
            show_turtle_randomly,
            1000
        )


def countdown(time):
    global game_over

    countdown_turtle.hideturtle()
    countdown_turtle.penup()

    top_height = screen.window_height() / 2
    y = top_height * 0.9

    countdown_turtle.setpos(
        0,
        y - 30
    )

    countdown_turtle.clear()

    if time > 0:
        countdown_turtle.write(
            arg=f"Time: {time}",
            move=False,
            align="center",
            font=FONT
        )

        screen.ontimer(
            lambda: countdown(time - 1),
            1000
        )

    else:
        game_over = True

        hide_turtles()

        countdown_turtle.write(
            arg="Game Over!",
            move=False,
            align="center",
            font=FONT
        )


turtle.tracer(0)

setup_score_turtle()
setup_turtles()
hide_turtles()

show_turtle_randomly()
countdown(10)

turtle.tracer(1)

turtle.mainloop()