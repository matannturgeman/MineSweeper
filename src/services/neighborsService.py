def count_neighbors(table_data):
	for x, _ in enumerate(table_data):
		for y, _ in enumerate(table_data[x]):
			slot = table_data[x][y]
			if slot.is_bomb:
				continue

			slot.neighbors_count = get_neighbors(slot, table_data)

	return table_data


def get_neighbors(slot, table_data):
	# # remove this comment for debug
	# if not slot.debug:
	# 	return 0

	sizes = {
		'x': len(table_data),
		'y': len(table_data[0])
	}

	neighbors = []
	pos = { 'x': slot.x, 'y': slot.y }

	new_neighbor = {'x': pos['x'] - 1, 'y': pos['y'] - 1}
	if(new_neighbor['x'] >= 0 and new_neighbor['y'] >= 0):
		neg = table_data[new_neighbor['y']][new_neighbor['x']]
		# print(1, new_neighbor, f'x: {neg.x}, y: {neg.y}, is_bomb: {neg.is_bomb}')

		if neg.is_bomb:
			neighbors.append(new_neighbor)

	new_neighbor = {'x': pos['x'], 'y': pos['y'] - 1}
	if(new_neighbor['y'] >= 0):
		neg = table_data[new_neighbor['y']][new_neighbor['x']]
		# print(2, new_neighbor, f'x: {neg.x}, y: {neg.y}, is_bomb: {neg.is_bomb}')

		if neg.is_bomb:
			neighbors.append(new_neighbor)

	new_neighbor = {'x': pos['x'] + 1, 'y': pos['y'] - 1}
	if(new_neighbor['x'] <= sizes['x'] - 1 and new_neighbor['y'] >= 0):
		neg = table_data[new_neighbor['y']][new_neighbor['x']]
		# print(3, new_neighbor, f'x: {neg.x}, y: {neg.y}, is_bomb: {neg.is_bomb}')

		if neg.is_bomb:
			neighbors.append(new_neighbor)

	new_neighbor = {'x': pos['x'] + 1, 'y': pos['y']}
	if(new_neighbor['x'] <= sizes['x'] - 1):
		neg = table_data[new_neighbor['y']][new_neighbor['x']]
		# print(4, new_neighbor, f'x: {neg.x}, y: {neg.y}, is_bomb: {neg.is_bomb}')

		if neg.is_bomb:
			neighbors.append(new_neighbor)

	new_neighbor = {'x': pos['x'] + 1, 'y': pos['y'] + 1}
	if(
		new_neighbor['x'] <= sizes['x'] - 1 and
		new_neighbor['y'] <= sizes['y'] - 1
	):
		neg = table_data[new_neighbor['y']][new_neighbor['x']]
		# print(5, new_neighbor, f'x: {neg.x}, y: {neg.y}, is_bomb: {neg.is_bomb}')

		if neg.is_bomb:
			neighbors.append(new_neighbor)

	new_neighbor = {'x': pos['x'], 'y': pos['y'] + 1}
	if(new_neighbor['y'] <= sizes['y'] - 1):
		neg = table_data[new_neighbor['y']][new_neighbor['x']]
		# print(6, new_neighbor, f'x: {neg.x}, y: {neg.y}, is_bomb: {neg.is_bomb}')

		if neg.is_bomb:
			neighbors.append(new_neighbor)

	new_neighbor = {'x': pos['x'] - 1, 'y': pos['y'] + 1}
	if(new_neighbor['x'] >= 0 and new_neighbor['y'] <= sizes['y'] - 1):
		neg = table_data[new_neighbor['y']][new_neighbor['x']]
		# print(7, new_neighbor, f'x: {neg.x}, y: {neg.y}, is_bomb: {neg.is_bomb}')

		if neg.is_bomb:
			neighbors.append(new_neighbor)

	new_neighbor = {'x': pos['x'] - 1, 'y': pos['y']}
	if(new_neighbor['x'] >= 0):
		neg = table_data[new_neighbor['y']][new_neighbor['x']]
		# print(8, new_neighbor, f'x: {neg.x}, y: {neg.y}, is_bomb: {neg.is_bomb}')

		if neg.is_bomb:
			neighbors.append(new_neighbor)

	# return len(neighbors)
	# print('pos', pos, 'negs', len(neighbors))
	# print('-------------------------------------')
	return len(neighbors)
