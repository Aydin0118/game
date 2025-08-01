"""
谷歌浏览器恐龙跑酷游戏的简化版本
使用 Pygame 实现，包含跳跃、障碍物和计分功能
"""
import pygame
import random
import sys

# 初始化 Pygame
pygame.init()

# 游戏窗口设置
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 300
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("恐龙跑酷")

# 颜色定义
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (100, 100, 100)

# 游戏参数
clock = pygame.time.Clock()
FPS = 60
GRAVITY = 1
JUMP_FORCE = -15
GAME_SPEED = 5
score = 0
font = pygame.font.SysFont(None, 36)

# 恐龙类
class Dino:
    def __init__(self):
        self.width = 30
        self.height = 40
        self.x = 50
        self.y = SCREEN_HEIGHT - self.height - 20
        self.vel_y = 0
        self.is_jumping = False
    
    def jump(self):
        if not self.is_jumping:
            self.vel_y = JUMP_FORCE
            self.is_jumping = True
    
    def update(self):
        # 应用重力
        self.vel_y += GRAVITY
        self.y += self.vel_y
        
        # 地面检测
        if self.y >= SCREEN_HEIGHT - self.height - 20:
            self.y = SCREEN_HEIGHT - self.height - 20
            self.is_jumping = False
    
    def draw(self):
        pygame.draw.rect(screen, GRAY, (self.x, self.y, self.width, self.height))

# 障碍物类
class Obstacle:
    def __init__(self):
        self.width = 20
        self.height = random.randint(20, 40)
        self.x = SCREEN_WIDTH
        self.y = SCREEN_HEIGHT - self.height - 20
    
    def update(self):
        self.x -= GAME_SPEED
    
    def draw(self):
        pygame.draw.rect(screen, BLACK, (self.x, self.y, self.width, self.height))
    
    def is_off_screen(self):
        return self.x < -self.width

# 游戏主循环
def main():
    global score, GAME_SPEED
    
    dino = Dino()
    obstacles = []
    obstacle_timer = 0
    running = True
    
    while running:
        # 事件处理
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    dino.jump()
        
        # 更新游戏状态
        dino.update()
        
        # 生成障碍物
        obstacle_timer += 1
        if obstacle_timer >= random.randint(50, 150):
            obstacles.append(Obstacle())
            obstacle_timer = 0
        
        # 更新障碍物
        for obstacle in obstacles[:]:
            obstacle.update()
            if obstacle.is_off_screen():
                obstacles.remove(obstacle)
                score += 1
                # 随着分数增加游戏加速
                if score % 5 == 0:
                    GAME_SPEED += 0.5
            
            # 碰撞检测
            if (dino.x < obstacle.x + obstacle.width and
                dino.x + dino.width > obstacle.x and
                dino.y < obstacle.y + obstacle.height and
                dino.y + dino.height > obstacle.y):
                running = False
        
        # 绘制
        screen.fill(WHITE)
        dino.draw()
        for obstacle in obstacles:
            obstacle.draw()
        
        # 显示分数
        score_text = font.render(f"分数: {score}", True, BLACK)
        screen.blit(score_text, (10, 10))
        
        pygame.display.update()
        clock.tick(FPS)
    
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()   