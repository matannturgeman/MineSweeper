import pygame
import random

colors = {
	"empty": (255, 0, 0),
	"open": (255, 255, 255)
}


class Slot():
	def __init__(self, x, y):
		self.x = x
		self.y = y
		self.is_flagged = False
		self.is_bomb = False
		self.type = '0'

	def __str__(self):
		props = vars(self)
		return f'Slot Object ({props})'

	def __repr__(self):
		props = vars(self)
		return f'Slot Object ({props})'

	def show(self, win):
		color = random.choice(list(colors.values()))
		print('color', color)
		pygame.draw.rect(win, color, (self.x, self.y, 50, 50))
		pygame.display.update()
