import turtle
import random


def draw_circle(color, size, x, y):
    # draw a circle of radius equals to size at x, y coordinates and
    # paint it with color
    turtle.penup()
    turtle.color(color)
    turtle.fillcolor(color)
    turtle.goto(x, y)
    turtle.pendown()
    turtle.begin_fill()
    turtle.circle(size)
    turtle.end_fill()


class Ball:
    def __init__(self, canvas_width, canvas_height,
                 ball_radius, num_balls):
        self.xpos = []
        self.ypos = []
        self.vx = []
        self.vy = []
        self.ball_color = []
        self.canvas_width = canvas_width
        self.canvas_height = canvas_height
        self.ball_radius = ball_radius
        self.num_balls = num_balls

    def initializing(self):
        for i in range(self.num_balls):
            self.xpos.append(
                random.randint(-1 * self.canvas_width + self.ball_radius,
                               self.canvas_width - self.ball_radius))
            self.ypos.append(
                random.randint(-1 * self.canvas_height + self.ball_radius,
                               self.canvas_height - self.ball_radius))
            self.vx.append(random.randint(1, 0.01 * self.canvas_width))
            self.vy.append(random.randint(1, 0.01 * self.canvas_height))
            self.ball_color.append((random.randint(0, 255),
                                    random.randint(0, 255),
                                    random.randint(0, 255)))

    def move_circle(self, i):
        # update the x, y coordinates of ball i with velocity in
        # the x (vx) and y (vy) components
        self.xpos[i] += self.vx[i]
        self.ypos[i] += self.vy[i]

        # if the ball hits the side walls,
        # reverse the vx velocity
        if (abs(self.xpos[i] + self.vx[i]) >
                (self.canvas_width - self.ball_radius)):
            self.vx[i] = -self.vx[i]

        # if the ball hits the ceiling or the floor,
        # reverse the vy velocity
        if (abs(self.ypos[i] + self.vy[i]) >
                (self.canvas_height - self.ball_radius)):
            self.vy[i] = -self.vy[i]
