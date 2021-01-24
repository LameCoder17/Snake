import turtle as t
import random as r

t.bgcolor('black')  # Sets background colour as black
t.title('Snake Game') # Sets title
t.setup(width=800, height=600)  # Sets screen size
gameStarted = False  # False as game hasnt started yet


snake = t.Turtle()  # This is the snake 
snake.shape('square')
snake.color('white')
snake.speed(0)
snake.penup()
snake.hideturtle()

fruit = t.Turtle()  # This is the fruit
fruit.shape('square')
fruit.color('yellow')
fruit.penup()
fruit.speed()
fruit.hideturtle()

textTurtle = False  # Will be false till we start the game
textTurtle = t.Turtle()
textTurtle.color('white')
textTurtle.penup()
textTurtle.write('Snake Game', align='center',
                 font=('Comic Sans MS', 48))
textTurtle.goto(0,-80)
textTurtle.write('Press Space to Start or Escape to Quit', align='center',
                 font=('Comic Sans MS', 28))
textTurtle.hideturtle()

scoreTurtle = t.Turtle()  # Shows score
scoreTurtle.color('white')
scoreTurtle.hideturtle()
scoreTurtle.speed(0)


def outsideWindow():  # Checks if snake goes out of bounds or not
    leftWall = -t.window_width()/2
    rightWall = t.window_width()/2
    topWall = t.window_height()/2
    bottomWall = -t.window_height()/2

    (x, y) = snake.pos()
    outside = x < leftWall or x > rightWall or y > topWall or y < bottomWall
    return outside


def placeFruit():  # Places fruit at random location
    fruit.hideturtle()
    fruit.setx(r.randint(-200, 200))
    fruit.sety(r.randint(-200, 200))
    fruit.showturtle()


def gameOver():  # For the game over screen 
    global gameStarted

    snake.hideturtle()
    fruit.hideturtle()

    t.penup()
    t.hideturtle()
    t.color('white')
    t.write('Game Over', align='center', font=('Comic Sans MS', 44, 'bold'))

    t.goto(0,-80)
    t.write('Press Space to Restart or Escape to Quit', align='center', font=('Comic Sans MS', 28, 'normal'))
    gameStarted = False
    t.goto(0,0)

def showScore(currentScore):  # Shows the current score
    scoreTurtle.clear()
    scoreTurtle.penup()
    x = t.window_width()/2 - 10
    y = t.window_height()/2 - 50
    scoreTurtle.setpos(x, y)
    scoreTurtle.write(str(currentScore), align='right',
                      font=('Comic Sans MS', 32))


def startGame():  # Starts the game
    global gameStarted

    if gameStarted:  # To check if game is already started
        return

    gameStarted = True
    score = 0
    textTurtle.clear()
    t.clear()

    snakeSpeed = 2  # Sets starting speed
    snakeLength = 3  # Sets starting length
    snake.shapesize(1, snakeLength, 1)  # Sets shape
    snake.goto(0,0)

    snake.showturtle()
    showScore(score)
    placeFruit()

    while True:
        snake.forward(snakeSpeed)
        if snake.distance(fruit) < 10:  # Checking if snake hits fruit
            placeFruit()  # Places new fruit
            snakeLength += 1  # Increases length
            snake.shapesize(1, snakeLength, 1)  # Changes shape
            snakeSpeed += 1  # Increases speed
            score += 10  # Increases score
            showScore(score)  # Updates on-display score

        if outsideWindow():  # If snake hits window border, game over
            gameOver()
            break


def moveUp():  # As snake can move up only when it is moving left or right, we check angles
    if snake.heading() == 0 or snake.heading() == 180:
        snake.setheading(90)


def moveDown():  # As snake can move down only when it is moving left or right, we check angles
    if snake.heading() == 0 or snake.heading() == 180:
        snake.setheading(270)


def moveLeft():  # As snake can move left only when it is moving up or down, we check angles
    if snake.heading() == 90 or snake.heading() == 270:
        snake.setheading(0)


def moveRight():  # As snake can move right only when it is moving up or down, we check angles
    if snake.heading() == 90 or snake.heading() == 270:
        snake.setheading(180)

def quitGame():
    global gameStarted
    if gameStarted == False:
        t.bye() 


t.onkey(startGame, 'space')
t.onkey(moveUp, 'w')
t.onkey(moveDown, 's')
t.onkey(moveLeft, 'd')
t.onkey(moveRight, 'a')
t.onkey(quitGame, 'Escape')

t.listen() 
t.mainloop()

