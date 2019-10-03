import turtle

# Named Constants
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 600
FLAG_SPEED = 10
DEV_CARD_X = -490
DEV_CARD_Y = 260

STRIPES_POSITION = -490
STRIPES_LONG = 950
STRIPES_SIZE = 38
STRIPES_COLOR = 'RED'
STRIPES_STARTPOS = 200
STRIPES_MARGIN = 66

BLUE_BOX_X = -490
BLUE_BOX_Y = 240
BLUE_ANGLE = 90
BLUE_HEIGHT = 256
BLUE_WIDTH = 380
BLUE_COLOR = 'blue'

WHITE_ANGLE = 90
WHITE_HEIGHT = 500
WHITE_WIDTH = 960
WHITE_PENSIZE = 40
WHITE_PENCOLOR = 'white'

# Setup the window
turtle.setup(SCREEN_WIDTH, SCREEN_HEIGHT)
turtle.speed(FLAG_SPEED)
turtle.hideturtle()
turtle.penup()

# Display Developer Info
turtle.goto(DEV_CARD_X, DEV_CARD_Y)
turtle.write("OUSSAMA BENSAID\nAmerican Flag Version 1.02")

# Draw flag stripes
turtle.goto(STRIPES_POSITION, (STRIPES_STARTPOS))
turtle.pendown()
turtle.pensize(STRIPES_SIZE)
turtle.color(STRIPES_COLOR)
turtle.forward(STRIPES_LONG)
turtle.penup()

turtle.goto(STRIPES_POSITION, STRIPES_STARTPOS-(STRIPES_MARGIN*1))
turtle.pendown()
turtle.forward(STRIPES_LONG)
turtle.penup()

turtle.goto(STRIPES_POSITION, STRIPES_STARTPOS-(STRIPES_MARGIN*2))
turtle.pendown()
turtle.forward(STRIPES_LONG)
turtle.penup()

turtle.goto(STRIPES_POSITION, STRIPES_STARTPOS-(STRIPES_MARGIN*3))
turtle.pendown()
turtle.forward(STRIPES_LONG)
turtle.penup()

turtle.goto(STRIPES_POSITION, STRIPES_STARTPOS-(STRIPES_MARGIN*4))
turtle.pendown()
turtle.forward(STRIPES_LONG)
turtle.penup()

turtle.goto(STRIPES_POSITION, STRIPES_STARTPOS-(STRIPES_MARGIN*5))
turtle.pendown()
turtle.forward(STRIPES_LONG)
turtle.penup()

turtle.goto(STRIPES_POSITION, STRIPES_STARTPOS-(STRIPES_MARGIN*6))
turtle.pendown()
turtle.forward(STRIPES_LONG)
turtle.penup()

# Small Box
turtle.goto(BLUE_BOX_X, BLUE_BOX_Y)
turtle.color(BLUE_COLOR)
turtle.fillcolor(BLUE_COLOR)

turtle.begin_fill()
turtle.pendown()
turtle.pensize(0)
turtle.forward(BLUE_WIDTH)
turtle.right(BLUE_ANGLE)
turtle.forward(BLUE_HEIGHT)
turtle.right(BLUE_ANGLE)
turtle.forward(BLUE_WIDTH)
turtle.right(BLUE_ANGLE)
turtle.forward(BLUE_HEIGHT)
turtle.end_fill()

# Border to Clear
turtle.pensize(WHITE_PENSIZE)
turtle.color(WHITE_PENCOLOR)
turtle.right(WHITE_ANGLE)
turtle.forward(WHITE_WIDTH)
turtle.right(WHITE_ANGLE)
turtle.forward(WHITE_HEIGHT)
turtle.right(WHITE_ANGLE)
turtle.forward(WHITE_WIDTH)
turtle.right(WHITE_ANGLE)
turtle.forward(WHITE_HEIGHT)

# To keep Graphics Window Open.
turtle.done()




