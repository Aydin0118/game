import tkinter as tk
import random

class SnakeGame:
    def __init__(self, master):
        self.master = master
        self.master.title("贪吃蛇游戏")
        self.master.geometry("400x400")
        self.master.resizable(False, False)
        self.canvas = tk.Canvas(self.master, bg="black", width=400, height=400)
        self.canvas.pack()
        self.snake = [(100, 100), (90, 100), (80, 100)]
        self.food = self.create_food()
        self.direction = "Right"
        self.score = 0
        self.master.bind("<KeyPress>", self.change_direction)
        self.update()

    def create_food(self):
        x, y = random.randint(0, 39) * 10, random.randint(0, 39) * 10
        return (x, y)

    def change_direction(self, event):
        key = event.keysym
        if key == "Up" and self.direction != "Down": self.direction = key
        elif key == "Down" and self.direction != "Up": self.direction = key
        elif key == "Left" and self.direction != "Right": self.direction = key
        elif key == "Right" and self.direction != "Left": self.direction = key

    def update(self):
        head_x, head_y = self.snake[0]
        if self.direction == "Up": new_head = (head_x, head_y - 10)
        elif self.direction == "Down": new_head = (head_x, head_y + 10)
        elif self.direction == "Left": new_head = (head_x - 10, head_y)
        elif self.direction == "Right": new_head = (head_x + 10, head_y)
        self.snake.insert(0, new_head)
        if new_head == self.food:
            self.score += 1
            self.food = self.create_food()
        else: self.snake.pop()
        if new_head in self.snake[1:]:
            self.game_over()
            return
        # 穿墙逻辑
        if new_head[0] < 0: new_head = (390, new_head[1])
        elif new_head[0] >= 400: new_head = (0, new_head[1])
        if new_head[1] < 0: new_head = (new_head[0], 390)
        elif new_head[1] >= 400: new_head = (new_head[0], 0)
        self.snake[0] = new_head
        self.draw()
        self.master.after(100, self.update)

    def draw(self):
        self.canvas.delete("all")
        for x, y in self.snake: self.canvas.create_rectangle(x, y, x + 10, y + 10, fill="green")
        x, y = self.food
        self.canvas.create_oval(x, y, x + 10, y + 10, fill="red")
        self.canvas.create_text(50, 10, text=f"得分: {self.score}", fill="white", font=("Arial", 10))

    def game_over(self):
        self.canvas.delete("all")
        self.canvas.create_text(200, 150, text=f"游戏结束! 最终得分: {self.score}", fill="white", font=("Arial", 16))
        tk.Button(self.master, text="重新开始", command=self.restart_game).pack()

    def restart_game(self):
        self.snake = [(100, 100), (90, 100), (80, 100)]
        self.food = self.create_food()
        self.direction = "Right"
        self.score = 0
        self.canvas.delete("all")
        self.update()

if __name__ == "__main__":
    root = tk.Tk()
    root.iconbitmap(r'D:\党培祥\tkinter教程\ico图标\snake_38881.ico')
    game = SnakeGame(root)
    root.mainloop()