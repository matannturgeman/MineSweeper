import pygame
import pprint
from .slot import Slot
from ..services.bombService import initialize_bombs

class Game_Table:
	def __init__(self, bombs_count, Main):
		self.Main = Main
		self.bombs_count = bombs_count
		self.table_data = None
		self.rows = 5
		self.cols = 5
		
	def end_game(self):
		self.Main.end_game()


	def initialize_table_data(self, win, game_width, game_height):
		self.table_data = []
		size = 100
		for x in range(self.rows):
			if not x in self.table_data:
				self.table_data.append([])

			for y in range(self.cols):
				if not y in self.table_data[x]:
					self.table_data[x].append([])

				self.table_data[x][y] = Slot(x, y, size, on_clicked_bomb=self.end_game)
		
		self.table_data = initialize_bombs(self.table_data, self.bombs_count)


	def print_table(self):
		pp = pprint.PrettyPrinter(depth=6)
		pp.pprint(self.table_data)


	def update_table(self, win):
		if not self.table_data:
			return

		for x in range(len(self.table_data)):
			for y in range(len(self.table_data[x])):
				slot = self.table_data[x][y]
				slot.show(win)
