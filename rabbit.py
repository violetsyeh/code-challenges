"""QUESTION
Prompt: Write a function that takes the input, gives the output, and meets the conditions below.

Input: An N x M matrix of a garden. Each cell contains a positive integer representing the number of carrots in that part of the garden.

Output: The number of carrots Bunny eats before falling asleep.

Conditions: Bunny starts in the center of the garden. If there are more than one center cell, Bunny starts in the cell with the largest number of carrots. There will never be a tie for the highest number of carrots in a center cell. Bunny eats all of the carrots in his cell, then looks left, right, up, and down for more carrots. Bunny always moves to the adjacent cell with the highest carrot count. If there are no adjacent cells with carrots, Bunny falls asleep.

original test case
>>> amount_eaten([[5, 7, 8, 6, 3],[0, 0, 7, 0, 4],[4, 6, 3, 4, 9],[3, 1, 0, 5, 8]])
27

oddxodd
>>> amount_eaten([[0, 4, 12, 9, 2], [3, 5, 18, 3, 0], [7, 9, 10, 16, 0]])
96

evenxeven
>>> amount_eaten([[2, 0, 4, 3], [0, 5, 8, 2], [1, 0, 0, 9], [0, 6, 3, 2]])
13

two rows
>>> amount_eaten([[5, 7, 2, 6, 1], [9, 4, 3, 0, 2]])
39

1x1
>>> amount_eaten([[9], [3]])
12

"""
	

def get_center_position(matrix):
	"""Calculates center position of first eaten carrots."""

	row = len(matrix)
	column = len(matrix[0])
	possible_center = {}
	grid_vals = []
	if row % 2 and column % 2:
		center = [row / 2, column / 2]
	if (not (row % 2)) and (not (column % 2)):
		possible_center = {
			0: [row /2, column / 2],
			1: [row / 2 - 1, column / 2],
			2: [row / 2, column / 2 - 1],
			3: [row / 2 - 1, column / 2 - 1],
		}
	   
		grid_vals = [matrix[row /2][column / 2],
					matrix[row / 2 - 1][column / 2],
					matrix[row / 2][column / 2 - 1],
					matrix[row / 2 - 1][column / 2 - 1]]
 	
 	if row % 2 and (not (column % 2)):
		possible_center = {
			0: [row /2, column / 2],
			1: [row / 2, column / 2 - 1],
		}
 
		grid_vals = [matrix[row /2][column / 2],
					matrix[row / 2][column / 2 - 1]]

	if (not (row % 2)) and column % 2:
		possible_center = {
			0: [row /2, column / 2],
			1: [row / 2 - 1, column / 2],
		}
		grid_vals = [matrix[row /2][column / 2],
					matrix[row / 2 - 1][column / 2]]
 	
	if possible_center:
		center_help = grid_vals.index(max(grid_vals))
		center = possible_center[center_help]
	eaten = matrix[center[0]][center[1]]
	matrix[center[0]][center[1]] = 0
	return [matrix, center, eaten]
 
def get_adjacent_carrots(matrix, position):
	"""Get the value of the squares adjacent to current position."""
  
	if position[0] == len(matrix) - 1:
		down = None
	else:
		down = matrix[position[0] + 1][position[1]]
 
	if position[0] == 0:
		up = None
	else:
		up = matrix[position[0] - 1][position[1]]
 
	if position[1] == len(matrix[0]) - 1:
		right = None
	else:
		right = matrix[position[0]][position[1] + 1]
 
	if position[1] == 0:
		left = None
	else:
		left = matrix[position[0]][position[1] - 1]
 
	adjacent_squares = {
		'left': left,
		'right': right,
		'up': up,
		'down': down,
	}
	return adjacent_squares
 
def is_valid_adjacent(matrix, position):
	"""Check if the adjacent squares have valid values, not None and not zero."""

	adjacent = get_adjacent_carrots(matrix, position)
	valid_square = False
	for i in adjacent.values():
		if (i != None and i != 0):
			valid_square = True
			break
	return valid_square
 
def update_position(position, direction):
	"""Update position of bunny based on which direction was chosen"""

	if direction == 'left':
		return [position[0], position[1] - 1]
	if direction == 'right':
		return [position[0], position[1] + 1]
	if direction == 'down':
		return [position[0] + 1, position[1]]
	if direction == 'up':
		return [position[0] - 1, position[1]]
	return [-1, -1]
 
 
def hop_and_eat(matrix, position):
	"""Move rabbit position, update eaten count and garden matrix."""

	
	adjacent = get_adjacent_carrots(matrix, position)

	direction = max(adjacent, key = adjacent.get)
	eaten = adjacent[direction]
	
	new_position = update_position(position, direction)

	matrix[new_position[0]][new_position[1]] = 0
	return [matrix, new_position, eaten]
 
def amount_eaten(matrix):
	"""Main function call that returns amount eaten with helper functions"""

	matrix, position, eaten = get_center_position(matrix)
	while is_valid_adjacent(matrix, position):
		[matrix, position, new_carrots] = hop_and_eat(matrix, position)
		eaten += new_carrots
	return eaten


if __name__ == '__main__':
	import doctest
	if doctest.testmod().failed == 0:
		print "\n*** ALL TESTS PASSED!\n"
