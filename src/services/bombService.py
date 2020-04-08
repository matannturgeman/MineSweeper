import random

def generate_bombs_location(table_data, bombs_count):
	bombs_pos = []
	for _ in range(bombs_count):
		x = get_random_int(0, len(table_data))
		y = get_random_int(0, len(table_data[0]))
		bomb_pos = (x, y)
		bombs_pos.append(bomb_pos)
		
	return bombs_pos


def initialize_bombs(table_data, bombs_count):
	bombs = generate_bombs_location(table_data, bombs_count)
	for x in range(len(table_data)):
		for y in range(len(table_data[x])):
			slot = table_data[x][y]
			if (x, y) in bombs:
				slot.insert_bomb()

	return table_data


def get_random_int(min, max):
	return random.randrange(min, max)
