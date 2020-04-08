from src.components.table import Game_Table
import pygame
pygame.init()

LEFT_KEY = pygame.K_LEFT
RIGHT_KEY = pygame.K_RIGHT
UP_KEY = pygame.K_UP
DOWN_KEY = pygame.K_DOWN

game_width = 1100
game_height = 800
bombs_count = 10

pygame.display.set_caption('Mine Sweeper')


class Main:
	def __init__(self):
		self.win = pygame.display.set_mode((game_width, game_height))
		# setting the game table
		self.new_table()
		# setting the game loop
		self.run = True
		self.min_game_loop()

	def new_table(self):
		game_table = Game_Table(bombs_count, Main=self)
		game_table.initialize_table_data(game_width, game_height)
		self.game_table = game_table

	def min_game_loop(self):
		try:
			while self.run:
				self.win.fill((0, 0, 0))
				self.game_table.update_table()
				pygame.display.update()

				for event in pygame.event.get():
					if event.type == pygame.QUIT:
						self.run = False

			pygame.display.quit()
			pygame.quit()

		except Exception as err:
			print('[Exception]:', err)
			self.run = False
			pygame.display.quit()
			pygame.quit()

	def end_game(self):
		self.new_table()


if __name__ == '__main__':
	Main()
