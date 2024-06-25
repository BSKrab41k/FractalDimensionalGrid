grid = [[0 for i in range(10)] for j in range(10)]
blank = [[0 for i in range(2)] for j in range(2)]
blank2 = [[0 for i in range(2)] for j in range(2)]

grid[5][5] = blank
grid[2][3] = blank
grid[7][4] = blank
grid[4][9] = blank
grid[5][5][1][1] = blank2
grid[2][3][0][1] = blank2


 
 
 
    
def GridChecker(cell):
	if type(cell) == type([]):
		return True
	else:
		return False

def CellDirection(dirname):
	directions = {'down' : (0, 1),
	  			'up' : (0, -1),
	  			'right' : (1, 0),
	  			'left' : (-1, 0)}
	dx, dy = directions[dirname][0], directions[dirname][1]
	return dx, dy
	
 
 
 
def Cell_IACP_Calculate(grid, x, y, gridx, gridy):	# cell in another chunk position calculate
	xline = len(grid)
	yline = len(grid[0])
	
 
	
def CellCanMove(grid, x, y, dirname):
	dx, dy = CellDirection(dirname)
	xline = len(grid) 
	yline = len(grid[0]) 
	if x < xline and y < yline:
		return True
	else:
		return False
		
def CellMove(grid, x, y, dirname):
	dx, dy = CellDirection(dirname)
	grid[x][y] = 0
	x = x+dx
	y = y+dy
	cell = grid[x][y]
	if CellCanMove(x, y):
		if GridChecker(cell):
			pass
			
	
def CellSearcher(grid):
	for i in range(len(grid)):
		for j, cell in enumerate(grid):
			if GridChecker(cell):
				subgrid = cell
				CellSearcher(subgrid)
CellSearcher(grid)


							