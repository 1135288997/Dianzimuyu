import pygame
import os

# 初始化 Pygame
pygame.init()

# 设置屏幕尺寸
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("电子木鱼-聂鸿博")

# 获取脚本所在目录
base_dir = os.path.dirname(os.path.abspath(__file__))

# 加载木鱼图像
wooden_fish_image_path = os.path.join(base_dir, 'muyu.png')
wooden_fish_image = pygame.image.load(wooden_fish_image_path)
wooden_fish_rect = wooden_fish_image.get_rect(center=(screen_width // 2, screen_height // 2))

# 加载功德图像
img_gd_path = os.path.join(base_dir, "gongde.png")
img_gd = pygame.image.load(img_gd_path)
gongde = img_gd.get_rect().move(screen_width // 2 + 150, screen_height // 2 - 200)
gongde_move = gongde
speed = [0, -20]

# 加载敲击声音
hit_sound_path = os.path.join(base_dir, 'muyu.mp3')
hit_sound = pygame.mixer.Sound(hit_sound_path)

# 设置字体为系统字体微软雅黑
font = pygame.font.SysFont('Microsoft YaHei', 36)

# 渲染中文文本
text_prompt = font.render("敲击空格键或点击木鱼敲打", True, (255, 255, 255))
text_prompt_rect = text_prompt.get_rect(center=(screen_width // 2, screen_height - 100))

# 初始化敲击次数
hit_count = 0

# 主循环
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                hit_sound.play()
                gongde_move = gongde_move.move(speed)
                hit_count += 1
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if wooden_fish_rect.collidepoint(event.pos):
                hit_sound.play()
                gongde_move = gongde_move.move(speed)
                hit_count += 1

        if gongde_move.top < 0:
            gongde_move = gongde

            # 渲染敲击次数
    hit_count_text = font.render(f"敲击次数: {hit_count}", True, (255, 255, 255))
    hit_count_rect = hit_count_text.get_rect(bottomright=(screen_width - 10, screen_height - 10))

    screen.fill((0, 0, 0))
    screen.blit(wooden_fish_image, wooden_fish_rect)
    screen.blit(img_gd, gongde_move)
    screen.blit(text_prompt, text_prompt_rect)
    screen.blit(hit_count_text, hit_count_rect)  # 添加敲击次数文本
    pygame.display.flip()

pygame.quit()