import pygame
import random

colors = {
	"empty": (212, 212, 212),
	"open": (255, 255, 255),
	"hover": (251, 251, 251),
	"bomb": (255, 0, 0),
	"debug": (0, 255, 255)
}


class Slot:
	def __init__(self, x, y, size, on_clicked_bomb, win):
		self.win = win
		self.font = pygame.font.SysFont('Arial', 25)
		# setting position variables
		self.x = x
		self.y = y
		self.size = size
		self.offset = 5
		# setting data variables
		self.is_flagged = False
		self.is_bomb = False
		self.neighbors_count = 0
		self.update_color()
		# setting method
		self.on_clicked_bomb = on_clicked_bomb
		# setting rectingle variables
		self.rect_x = (self.x * self.size) + self.offset
		self.rect_y = (self.y * self.size) + self.offset
		self.rect_size = self.size - self.offset
		self.rect = (self.rect_x, self.rect_y, self.rect_size, self.rect_size)
		
		self.debug = False

	def __str__(self):
		# props = vars(self)
		# return f'Slot Object ({props})'
		return f'Slot Object (x: {self.x}, y: {self.y})'

	def __repr__(self):
		# props = vars(self)
		# return f'Slot Object ({props})'
		return f'Slot Object (x: {self.x}, y: {self.y})'
		
	def initiate_debug(self):
		self.debug = True

	def insert_bomb(self):
		self.is_bomb = True

	def get_is_hover(self):
		Mouse_x, Mouse_y = pygame.mouse.get_pos()
		mouse_pos = (Mouse_x, Mouse_y)
		if pygame.Rect(self.rect).collidepoint(mouse_pos):
			return True
		else:
			return False

	def update_color(self):
		if self.is_bomb:
			self.color = colors.get('bomb')
		else:
			self.color = colors.get('empty')

	def check_pressed(self):
		mousex, mousey = pygame.mouse.get_pos()
		click = pygame.mouse.get_pressed()

		if (
			click != (0, 0, 0) and
			mousex >= self.rect_x and
			mousex <= self.rect_x + self.rect_size and
			mousey >= self.rect_y and
			mousey <= self.rect_y + self.rect_size
		):
			self.handle_pressed()

	def handle_pressed(self):
		if self.is_bomb:
			self.on_clicked_bomb()

	def display_neighbors(self):
		middle = self.size // 2 - 10
		text_pos = (self.rect_x + middle, self.rect_y + middle)
		txt = f'x:{self.x},y:{self.y},{self.neighbors_count}'
		# txt = str(self.neighbors_count)
		self.display_text(text_pos, txt, (0, 0, 0))

	def display_text(self, text_pos, text, color):
		self.win.blit(
			self.font.render(
				text,
				True,
				color
			),
			text_pos
		)

	def show(self):
		self.check_pressed()
		if self.debug:
			self.color = colors.get('debug')
		elif self.get_is_hover():
			self.color = colors.get('hover')
		else:
			self.update_color()

		pygame.draw.rect(self.win, self.color, self.rect)
		self.display_neighbors()
		pygame.display.update()
