#huge thank you to the youtube channel bro code: https://www.youtube.com/channel/UC4SVo0Ue36XCfOyb5Lh1viQ
#subscribe to his channel here:
#find the video that helped me here: https://www.youtube.com/watch?v=bfRwxS5d0SI&ab_channel=BroCode
#this is my first python project so enjoy :)

from tkinter import * 
import random

THE_HEIGHT = 700
THE_WIDTH = 700
SPEED = 100
SPACE_SIZE = 50 
BODY_PARTS = 3
COLOR = "#0000FF"
FOOD_COLOR = "#FF0000"
BACKGROUND_COLOR = "#000000"

class Snake:
    def __init__ (self):
        self.body_size = BODY_PARTS
        self.coordinates = []
        self.squares = []

        for i in range (0, BODY_PARTS):
            self.coordinates.append([0,0])
        
        for x, y in self.coordinates:
            square = canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill = COLOR, tag = "snake")
            self.squares.append(square)
class Food:
    
    def __init__(self):
        x = random.randint(0,(THE_WIDTH/SPACE_SIZE)-1)*SPACE_SIZE
        y = random.randint(0,(THE_HEIGHT/SPACE_SIZE)-1)*SPACE_SIZE


        self.coordinates = [x, y]
        canvas.create_oval(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=FOOD_COLOR, tag="apples" )

def turn(snake, food):
    
    x, y = snake.coordinates[0]
    if direction == "up":
        y -= SPACE_SIZE
    elif direction == "down":
        y+= SPACE_SIZE
    elif direction == "left":
        x -= SPACE_SIZE
    elif direction == "right":
        x += SPACE_SIZE
    
    snake.coordinates.insert(0, (x, y))
    square = canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill = COLOR)
    snake.squares.insert(0, square)

    if x == food.coordinates[0] and y == food.coordinates [1]:
        global score
        score += 1
        label.config(text = "Points: {}".format(score))
        canvas.delete("apples")
        food = Food()
    else:
        del snake.coordinates[-1]
        canvas.delete(snake.squares[-1])
        del snake.squares[-1]
    if check_wall(snake):
        game_over()
    else:

        window.after(SPEED, turn, snake, food) #could be issue with food or apples


def change_direction(new_direction):
    global direction
    if new_direction == 'left':
        if direction != 'right':
            direction = new_direction
    elif new_direction == 'right':
        if direction != 'left':
            direction = new_direction
    elif new_direction == 'up':
        if direction != 'down':
            direction = new_direction

    elif new_direction == 'down':
        if direction != 'up':
            direction = new_direction
def check_wall(snake):
    x, y = snake.coordinates[0]
    if x < 0 or x >= THE_WIDTH:
        return True
    elif y < 0 or y >= THE_HEIGHT:
        return True
    for body_part in snake.coordinates[1:]:
        if x == body_part[0] and y == body_part[1]:
            return True
    return False
def game_over():
    canvas.delete(ALL)
    canvas.create_text(canvas.winfo_width()/2, canvas.winfo_height()/2, font = ('consolas', 70), text = "Game Over", fill = "red", tag = "gameover")
   


window = Tk()
window.title("Hunter's Snake Game")
window.resizable(False, False)
score = 0 
direction = 'down'
label = Label(window, text = "Points: {}".format(score), font = ('consolas', 40))
label.pack()

canvas = Canvas(window, bg = BACKGROUND_COLOR, height = THE_HEIGHT, width = THE_WIDTH )
canvas.pack()
window.update()
window_width = window.winfo_width()
window_height = window.winfo_height()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

x = int((screen_width/2) - (window_width/2))
y= int ((screen_height / 2) - (window_height / 2))

window.geometry(f"{window_width}x{window_height}+{x}+{y}")
window.bind('<Left> ', lambda event: change_direction('left'))
window.bind('<Right> ', lambda event: change_direction('right'))
window.bind('<Up> ', lambda event: change_direction('up'))
window.bind('<Down> ', lambda event: change_direction('down'))


snake = Snake()
food = Food()
turn(snake, food)

window.mainloop()



