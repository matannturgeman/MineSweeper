import pygame
pygame.init()

game_width = 1100
game_height = 800

LEFT_KEY = pygame.K_LEFT
RIGHT_KEY = pygame.K_RIGHT
UP_KEY = pygame.K_UP
DOWN_KEY = pygame.K_DOWN

win = pygame.display.set_mode((game_width, game_height))
pygame.display.set_caption('Mine Sweeper')

x = 50
y = 50

width = 40
height = 60
vel = 5

run = True


while run:
	pygame.time.delay(100)
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False

	keys = pygame.key.get_pressed()

	if keys[LEFT_KEY]:
		x -= vel
	if keys[RIGHT_KEY]:
		x += vel
	if keys[UP_KEY]:
		y -= vel
	if keys[DOWN_KEY]:
		y += vel

	win.fill((0, 0, 0))
	pygame.draw.rect(win, (255, 0, 0), (x, y, width, height))
	pygame.display.update()


pygame.quit()