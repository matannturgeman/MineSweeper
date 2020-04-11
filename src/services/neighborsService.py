def count_neighbors(table_data):
	sizes = {
		'x': len(table_data),
		'y': len(table_data[0])
	}

	for x, _ in enumerate(table_data):
		for y, _ in enumerate(table_data[x]):
			slot = table_data[x][y]
			if slot.is_bomb:
				continue

			slot.neighbors_count = get_neighbors(slot, sizes)
			
	table_data[1][2].initiate_debug()

	return table_data


def get_neighbors(slot, sizes):
	pos = { 'x': slot.x, 'y': slot.y }
	neighbors = []
	
	new_neighbor = {'x': pos['x'] - 1, 'y': pos['y'] - 1}
	if(new_neighbor['x'] >= 0 and new_neighbor['y'] >= 0):
		neighbors.append(new_neighbor)

	new_neighbor = {'x': pos['x'], 'y': pos['y'] - 1}
	if(new_neighbor['y'] >= 0):
		neighbors.append(new_neighbor)

	new_neighbor = {'x': pos['x'] + 1, 'y': pos['y'] - 1}
	if(new_neighbor['x'] <= sizes['x'] - 1 and new_neighbor['y'] >= 0):
		neighbors.append(new_neighbor)

	new_neighbor = {'x': pos['x'] + 1, 'y': pos['y']}
	if(new_neighbor['x'] <= sizes['x'] - 1):
		neighbors.append(new_neighbor)

	new_neighbor = {'x': pos['x'], 'y': pos['y'] + 1}
	if(new_neighbor['y'] <= sizes['y'] - 1):
		neighbors.append(new_neighbor)

	new_neighbor = {'x': pos['x'] - 1, 'y': pos['y'] + 1}
	if(new_neighbor['x'] >= 0 or new_neighbor['y'] <= sizes['y'] - 1):
		neighbors.append(new_neighbor)

	# return len(neighbors)
	print('pos', pos, 'negs', len(neighbors), neighbors)
	
	return len(neighbors)
