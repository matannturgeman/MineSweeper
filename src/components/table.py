import pygame
import pprint
from ..classes.slot import Slot
pp = pprint.PrettyPrinter(depth=6)

table_data = None
rows = 5
cols = 5

# def draw_lines():
# 	for x in range(rows):
# 		for y in range(cols):


def initialize_table_data(win, game_width, game_height):
	global table_data
	table_data = []
	size = 100
	center = (game_width + game_height) / 2
	print('center', center, 'game_width', game_width, 'game_height', game_height)
	for x in range(rows):
		if not x in table_data:
			table_data.append([])

		for y in range(cols):

			if not y in table_data[x]:
				table_data[x].append([])
			
			# mid_x = int((center / 2) + x)
			# print('mid_x:', mid_x, 'x:', x)
			table_data[x][y] = Slot(x, y, size)

	# draw_lines()


def print_table():
	pp.pprint(table_data)


def update_table(win):
	global table_data
	if not table_data:
		return

	for x in range(len(table_data)):
		for y in range(len(table_data[x])):
			slot = table_data[x][y]
			slot.show(win)
