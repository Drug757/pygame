import pygame

pygame.init()

screen = pygame.display.set_mode((600, 400))
pygame.display.set_caption("Мини игра")

clock = pygame.time.Clock()

player = pygame.Rect(50, 50, 40, 40)
obstacle = pygame.Rect(300, 150, 50, 50)

speed = 5
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_w]:
        player.y -= speed
    if keys[pygame.K_s]:
        player.y += speed
    if keys[pygame.K_a]:
        player.x -= speed
    if keys[pygame.K_d]:
        player.x += speed

    if player.colliderect(obstacle):
        print("Ты врезался! Игра окончена")
        running = False

    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, (0, 255, 0), player)
    pygame.draw.rect(screen, (255, 0, 0), obstacle)

    pygame.display.update()
    clock.tick(60)  

pygame.quit()