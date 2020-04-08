import pygame
import pprint
from .slot import Slot
from ..services.bombService import initialize_bombs
from ..services.neighborsService import count_neighbors


class Game_Table:
	def __init__(self, bombs_count, Main):
		self.Main = Main
		self.bombs_count = bombs_count
		self.table_data = None
		self.rows = 5
		self.cols = 5
		

	def initialize_table_data(self, game_width, game_height):
		self.table_data = []
		size = 100
		for x in range(self.rows):
			if not x in self.table_data:
				self.table_data.append([])

			for y in range(self.cols):
				if not y in self.table_data[x]:
					self.table_data[x].append([])

				new_slot = Slot(
					x=x,
					y=y,
					size=size,
					on_clicked_bomb=self.Main.end_game,
					win=self.Main.win
				)
				self.table_data[x][y] = new_slot

		bombed_table = initialize_bombs(self.table_data, self.bombs_count)
		self.table_data = count_neighbors(bombed_table)

	def print_table(self):
		pp = pprint.PrettyPrinter(depth=6)
		pp.pprint(self.table_data)

	def update_table(self):
		if not self.table_data:
			return

		for x in range(len(self.table_data)):
			for y in range(len(self.table_data[x])):
				slot = self.table_data[x][y]
				slot.show()
