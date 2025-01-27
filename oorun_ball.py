import turtle
from ooball import Ball, draw_circle


num_balls = int(input("Number of balls to simulate: "))
turtle.speed(0)
turtle.tracer(0)
turtle.hideturtle()
canvas_width = turtle.screensize()[0]
canvas_height = turtle.screensize()[1]
ball_radius = 0.05 * canvas_width
turtle.colormode(255)
tur_ball = Ball(canvas_width, canvas_height, ball_radius, num_balls)
tur_ball.initializing()
while True:
    turtle.clear()
    for i in range(num_balls):
        draw_circle(tur_ball.ball_color[i],
                    tur_ball.ball_radius,
                    tur_ball.xpos[i],
                    tur_ball.ypos[i])
        tur_ball.move_circle(i)
    turtle.update()

# hold the window; close it by clicking the window close 'x' mark
turtle.done()
