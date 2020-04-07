import pygame
from src.components.table import initialize_table_data, print_table, update_table

pygame.init()

game_width = 1100
game_height = 800

LEFT_KEY = pygame.K_LEFT
RIGHT_KEY = pygame.K_RIGHT
UP_KEY = pygame.K_UP
DOWN_KEY = pygame.K_DOWN

win = pygame.display.set_mode((game_width, game_height))
pygame.display.set_caption('Mine Sweeper')

initialize_table_data(win, game_width, game_height)

run = True
try:
	while run:
		# pygame.time.delay(100)
		win.fill((0, 0, 0))
		update_table(win)
		pygame.display.update()
		
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False
				
	pygame.display.quit()
	pygame.quit()
	
except Exception as e:
	run = False
	pygame.display.quit()
	pygame.quit()
