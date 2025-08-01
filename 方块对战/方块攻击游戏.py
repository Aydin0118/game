import tkinter as tk
import random

class PlaneGame:
    def __init__(self, root):
        self.root = root
        self.root.title("飞机大作战")
        self.canvas = tk.Canvas(root, width=400, height=600, bg="black")
        self.canvas.pack()

        # 玩家飞机
        self.player = self.canvas.create_rectangle(180, 550, 220, 590, fill="blue")

        # 敌机列表
        self.enemies = []
        # 子弹列表
        self.bullets = []
        self.score = 0
        self.score_label = tk.Label(root, text=f"得分: {self.score}", fg="white", bg="black")
        self.score_label.pack()

        # 绑定键盘事件
        self.root.focus_set()
        self.root.bind("<KeyPress-Left>", self.move_left)
        self.root.bind("<KeyPress-Right>", self.move_right)
        self.root.bind("<KeyPress-space>", self.fire_bullet)

        # 生成敌机
        self.spawn_enemy()

    def move_left(self, event):
        pos = self.canvas.coords(self.player)
        if pos[0] > 0:
            self.canvas.move(self.player, -20, 0)

    def move_right(self, event):
        pos = self.canvas.coords(self.player)
        if pos[2] < 400:
            self.canvas.move(self.player, 20, 0)
        
    def fire_bullet(self, event):
        x1, y1, x2, y2 = self.canvas.coords(self.player)
        bullet = self.canvas.create_rectangle(x1 + 15, y1 - 10, x1 + 25, y1, fill="yellow")
        self.bullets.append(bullet)
        self.move_bullet(bullet)

    def move_bullet(self, bullet):
        self.canvas.move(bullet, 0, -15)
        pos = self.canvas.coords(bullet)
        
        # 检测子弹与敌机碰撞
        for enemy in self.enemies[:]:
            enemy_pos = self.canvas.coords(enemy)
            if (pos[0] < enemy_pos[2] and pos[2] > enemy_pos[0] and
                pos[1] < enemy_pos[3] and pos[3] > enemy_pos[1]):
                self.canvas.delete(enemy)
                self.enemies.remove(enemy)
                self.canvas.delete(bullet)
                self.bullets.remove(bullet)
                self.score += 1
                self.score_label.config(text=f"得分: {self.score}")
                return
        
        # 检测子弹是否飞出屏幕
        if pos[1] < 0:
            self.canvas.delete(bullet)
            self.bullets.remove(bullet)
        else:
            self.root.after(50, lambda: self.move_bullet(bullet))

    def spawn_enemy(self):
        x = random.randint(0, 350)
        enemy = self.canvas.create_rectangle(x, 0, x + 50, 40, fill="red")
        self.enemies.append(enemy)
        self.move_enemy(enemy)
        delay = max(500, 2000 - self.score * 50)
        self.root.after(delay, self.spawn_enemy)

    def move_enemy(self, enemy):
        self.canvas.move(enemy, 0, 10)
        pos = self.canvas.coords(enemy)

        # 检测碰撞
        player_pos = self.canvas.coords(self.player)
        if (pos[0] < player_pos[2] and pos[2] > player_pos[0] and
            pos[1] < player_pos[3] and pos[3] > player_pos[1]):
            self.game_over()
            return

        # 检测是否飞出屏幕
        if pos[1] < 600:
            self.root.after(100, lambda: self.move_enemy(enemy))
        else:
            self.canvas.delete(enemy)
            self.enemies.remove(enemy)

    def game_over(self):
        self.canvas.create_text(200, 300, text="游戏结束，请重启游戏", fill="white", font=("Arial", 30))
        self.root.unbind("<KeyPress-Left>")
        self.root.unbind("<KeyPress-Right>")
        self.root.unbind("<KeyPress-space>")
        for enemy in self.enemies[:]:
            self.canvas.delete(enemy)
        for bullet in self.bullets[:]:
            self.canvas.delete(bullet)
        self.enemies.clear()
        self.bullets.clear()

if __name__ == "__main__":
    root = tk.Tk()
    try:
        root.iconbitmap(r"D:\党培祥\tkinter教程\腾讯一天一个游戏\跑酷\target_bulls_eye_target_goal_hit_icon-icons.com_59974.ico")
    except:
        pass
    game = PlaneGame(root)
    root.mainloop()