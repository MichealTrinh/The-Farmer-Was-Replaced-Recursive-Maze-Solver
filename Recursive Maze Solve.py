def main():
	reset()
	treasure_coords = None
	maze_structure = {}
	iteration = 1
	while iteration <= 300:
		quick_print(iteration)
		direction = 0
		path = []
		curr_coords = (get_pos_x(), get_pos_y())
		if treasure_coords == None:
			while(size(maze_structure) != get_world_size() * get_world_size() or get_entity_type() != Entities.Treasure):
				
				direction = simple_pathing(direction)
				curr_coords = (get_pos_x(), get_pos_y())
				if curr_coords not in maze_structure:
					maze_structure[curr_coords] = record_maze_coord()
					#quick_print(curr_coords)
					#quick_print(maze_structure[curr_coords])
		else:
			path = []
			pathing(treasure_coords, maze_structure, False, path, curr_coords, curr_coords)
			quick_print(path)
			follow_path(path)
		#quick_print(get_world_size() * get_world_size())
		#quick_print(size(maze_structure))
		#toString(maze_structure)
		if get_entity_type() == Entities.Treasure:
			treasure_coords = measure()
		if iteration != 300:
			use_item(Items.Weird_Substance, get_world_size() * num_unlocked(Unlocks.Mazes))
		else:
			harvest()
		iteration += 1
		
	
def reset():
	clear()
	plant(Entities.Bush)
	use_item(Items.Weird_Substance, get_world_size() * num_unlocked(Unlocks.Mazes))
	
def simple_pathing(direction):
		
	if(direction == 0):
		if(move(East)):
			return 1
		else:
			if(move(North)):
				return 0
			else:
				return 3

	if(direction == 1):
		if(move(South)):
			return 2
		else:
			if(move(East)):
				return 1
			else:
				return 0
		
	if(direction == 2):
		if(move(West)):
			return 3
		else:
			if(move(South)):
				return 2
			else:
				return 1
	
	if(direction == 3):
		if(move(North)):
			return 0
		else:
			if(move(West)):
				return 3
			else:
				return 2

# Record the given point's available paths in a set
def record_maze_coord():
	no_wall = set()
	if move(North):
		move(South)
		no_wall.add(North)
	if move(East):
		move(West)
		no_wall.add(East)
	if move(South):
		move(North)
		no_wall.add(South)
	if move(West):
		move(East)
		no_wall.add(West)
	return no_wall



# Dict maze_structure[Key: Tuple coords(0, 0), Value: Set no_wall(North, East, South, West)]
# recursive function to map a path to treasure based on initial maze structure
def pathing(treasure_coords, maze_structure, dest_reached, path, prev, next):
	curr = next
	# Wall structure of current point in maze
	curr_no_wall = maze_structure[curr]
	# Check if destination is reached
	if curr == treasure_coords:
		path.append(treasure_coords)
		path.append(curr)
		return True
	else:
	# Continue pathing if no treasure
		for cardinal in curr_no_wall:
			if(not dest_reached):
				if(cardinal == North and (curr[0], curr[1] + 1) != prev):
					dest_reached = pathing(treasure_coords, maze_structure, dest_reached, path, curr, (curr[0], curr[1] + 1))
				if(cardinal == East and (curr[0] + 1, curr[1]) != prev):
					dest_reached = pathing(treasure_coords, maze_structure, dest_reached, path, curr, (curr[0] + 1, curr[1]))
				if(cardinal == South and (curr[0], curr[1] - 1) != prev):
					dest_reached = pathing(treasure_coords, maze_structure, dest_reached, path, curr, (curr[0], curr[1] - 1))
				if(cardinal == West and (curr[0] - 1, curr[1]) != prev):
					dest_reached = pathing(treasure_coords, maze_structure, dest_reached, path, curr, (curr[0] - 1, curr[1]))
	# Add coords to path when treasure is found
		if(dest_reached):
			path.append(curr)
			return True
	# End pathing if no treasure
	return False

def follow_path(path):
	for i in range(len(path) - 1):
		next_coord = path.pop()
		diffX = next_coord[0] - get_pos_x()
		diffY = next_coord[1] - get_pos_y()
		if diffX == 1:
			move(East)
		if diffX == -1:
			move(West)
		if diffY == 1:
			move(North)
		if diffY == -1:
			move(South)
	
def size(dict):
	i = 0
	for key in dict:
		i += 1
	return i

def toString(dict):
	for key in dict:
		quick_print(str(key) + str(dict[key]))
	
if __name__ == "__main__":
	main()