from tkinter import *
import time

from settings import *
from objects import *


class Game:
    
    def __init__(self, canvas, score):
        self.canvas = canvas

        self.score = score.add_point()

        self.game_started = False
        self.canvas.bind_all("<KeyPress-Return>", self.start_game)

        

        
    def start_game(self, event):
        self.game_started = True

    def speed_increase(self):
        i = self.score

        if i < 5:
            time.sleep(0.01)
        
        elif i < 10:
            time.sleep(0.005)

        else:
            time.sleep(0.001)
            

root = Tk()
root.title(GAME_NAME)
root.resizable(0, 0)
root.wm_attributes('-topmost', 1)
root["bg"] = "gray22"

canvas = Canvas(root, width=WIDTH, height=HEIGHT, highlightthickness=0, bg=COLOR_CANVAS)
canvas.pack()
root.update()





paddle = Paddle(canvas, COLOR_PADDLE, HEIGHT_PADDLE, WIDTH_PADDLE)
score = Score(canvas, COLOR_SCORE, HEIGHT_TEXT_SCORE, WIDTH_TEXT_SCORE)
ball = Ball(canvas, paddle, score, COLOR_BALL, HEIGHT_BALL, WIDTH_BALL)
game = Game(canvas, score)

while not ball.hit_bottom:

    if game.game_started:
        ball.draw(COLOR_END_TEXT, HEIGHT_END_TEXT, WIDTH_END_TEXT)
        paddle.draw()

    root.update_idletasks()
    root.update()

    #time.sleep(0.01)

    game.speed_increase()
time.sleep(3)