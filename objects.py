import random

class Ball:
    def __init__(self, canvas, paddle, score, color, height, width):
        self.canvas = canvas
        self.paddle = paddle
        self.score = score

        self.id = canvas.create_oval(height, height, width, width, fill=color)
        self.canvas.move(self.id, 250, 100)
        self.canvas_width = self.canvas.winfo_width()

        starts = [-2, -1, 1, 2]

        random.shuffle(starts)

        self.x = starts[0]

        self.y = 2

        self.canvas_height = self.canvas.winfo_height()
        self.canvas_weight = self.canvas.winfo_width()

        self.hit_bottom = False


    def hit_paddle(self, pos):
        paddle_pos = self.canvas.coords(self.paddle.id)
# pos - position
        if pos[2] >= paddle_pos[0] and pos[0] <= paddle_pos[2]:
            if pos[3] >= paddle_pos[1] and pos[3] <= paddle_pos[3]:
                self.score.add_point()
                return True
        return False
    
    def draw(self, color_end_text, height, width):
        self.canvas.move(self.id, self.x, self.y)

        pos = self.canvas.coords(self.id)

        if pos[1] <= 0:
            self.y = 2

        if pos[3] >= self.canvas_height:
            self.hit_bottom = True
            self.canvas.create_text(height, width, text='Game over :(', font=('Courier', 30), fill=color_end_text)

        if self.hit_paddle(pos) == True:
            self.y = -2

        if pos[0] <= 0:
            self.x = 2

        if pos[2] >= self.canvas_weight:
            self.x = -2

class Paddle:

    def __init__(self, canvas, color, height, width):
        self.canvas = canvas
        self.id = canvas.create_rectangle(0, 0, height, width, fill=color)

        start_1 = [40, 60, 120, 150, 180, 200] 
        random.shuffle(start_1)

        self.start_pos_x = start_1[0]
        self.canvas.move(self.id, self.start_pos_x, 400)

        self.x = 0

        self.canvas_width = self.canvas.winfo_width()

        self.game_started = False

        self.canvas.bind_all("<KeyPress-Right>", self.turn_right)
        self.canvas.bind_all("<KeyPress-Left>", self.turn_left)


    def turn_right(self, event):
        self.x = 2

    def turn_left(self, event):
        self.x = -2

    def draw(self):
        self.canvas.move(self.id, self.x, 0)
        pos = self.canvas.coords(self.id)

        if pos[0] <= 0:
            self.x = 0

        elif pos[2] >= self.canvas_width:
            self.x = 0

class Score:

    def __init__(self, canvas, color, height, width):
        self.canvas = canvas
        self.score = 0
        self.id = canvas.create_text(height, width, text=self.score, font=('Courier', 20), fill=color)

    def add_point(self):
        self.score += 1
        self.canvas.itemconfig(self.id, text=self.score)
        return self.score