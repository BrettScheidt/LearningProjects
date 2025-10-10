import tkinter as tk
import random

Game = tk.Tk()
Game.title("CTX-PONG")
Game.geometry("405x305")

global score
score = 0
class Ball:
    
    def __init__(self, master, x, y):
        self.master = master
        self.canvas = tk.Canvas(master, width=400, height=300, bg="black")
        self.canvas.pack()
        self.title = self.canvas.create_text(200, 150, fill="Blue", font="Times 20 bold", text="ConsortiEX")

        self.ball = self.canvas.create_oval(190, 140, 210, 160, fill="orange")
        self.dx = 3
        self.dy = -3
        
        self.paddle = self.canvas.create_rectangle(x, y, x + 50, y + 10, fill="blue")
        self.move_element()
        self.canvas.bind_all("<KeyPress-Left>", self.move_left)
        self.canvas.bind_all("<KeyPress-Right>", self.move_right)



    def move_element(self):
        global score
        self.canvas.move(self.ball, self.dx, self.dy)
        pos = self.canvas.coords(self.ball)
        paddle_pos = self.canvas.coords(self.paddle)
        if pos[0] <= 0 or pos[2] >= 400:
            if(self.dx > 0):
                self.dx = -(random.randint(3, 6))
            else:
                self.dx = random.randint(3, 6)
            #self.dx = -self.dx
        if pos[1] <= 0:
            if(self.dy > 0):
                self.dy = -(random.randint(3, 6))
            else:
                self.dy = random.randint(3, 6)
            #self.dy = -self.dy
        if (pos[3] >= paddle_pos[1] and pos[2] >= paddle_pos[0] and pos[0] <= paddle_pos[2] and pos[3] <= paddle_pos[3] + 10 and self.dy > 0):
            if(self.dy > 0):
                self.dy = -(random.randint(3, 6))
            else:
                self.dy = random.randint(3, 6)
            score += 1
            #self.dy = -self.dy
        if pos[3] >= 300:
            self.canvas.coords(self.ball, 190, 140, 210, 160)
            self.dx = 3
            self.dy = -3
            print("Game Over! Your score was: " + str(score))
            score = 0
        self.master.after(20, self.move_element)

    def move_left(self,arg):
        pos = self.canvas.coords(self.paddle)
        if pos[0] > 0:
            self.canvas.move(self.paddle, -20, 0)

    def move_right(self,arg):
        pos = self.canvas.coords(self.paddle)
        if pos[2] < 400:
            self.canvas.move(self.paddle,20,0)

app = Ball(Game, 10, 270)
Game.mainloop()