import pygame
import random

colors = {
	"empty": (212, 212, 212),
	"open": (255, 255, 255),
	"hover": (251, 251, 251),
}


class Slot():
	def __init__(self, x, y, size):
		self.x = x
		self.y = y
		self.size = size
		self.offset = 5
		self.is_flagged = False
		self.is_bomb = False
		self.type = '0'
		self.update_color()
		
		self.rect_x = (self.x * self.size) + self.offset
		self.rect_y = (self.y * self.size) + self.offset
		self.rect_size = self.size - self.offset
		self.rect = (
			self.rect_x,
			self.rect_y,
			self.rect_size,
			self.rect_size
		)

	def __str__(self):
		props = vars(self)
		return f'Slot Object ({props})'

	def __repr__(self):
		props = vars(self)
		return f'Slot Object ({props})'

	def get_is_hover(self):
		Mouse_x, Mouse_y = pygame.mouse.get_pos()
		mouse_pos = (Mouse_x, Mouse_y)
		if pygame.Rect(self.rect).collidepoint(mouse_pos):
			return True
		else:
			return False

	def update_color(self):
		self.color = colors.get('empty')

	def check_pressed(self):
		mousex, mousey = pygame.mouse.get_pos()
		click = pygame.mouse.get_pressed()

		if click != (0, 0, 0):
			if (
				mousex >= self.rect_x and 
				mousex <= self.rect_x + self.rect_size and 
				mousey >= self.rect_y and 
				mousey <= self.rect_y + self.rect_size
			):
				self.handle_pressed()
				
	def handle_pressed(self): 
		print('clicked')

	def show(self, win):
		self.check_pressed()
		is_hover = self.get_is_hover()
		if is_hover:
			self.color = colors.get('hover')
		else:
			self.update_color()
		pygame.draw.rect(win, self.color, self.rect)
		pygame.display.update()
