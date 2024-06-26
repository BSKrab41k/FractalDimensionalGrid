#from Render import CellRender
from Cell import *
from sys import *
grid = [[empty for i in range(10)] for j in range(10)] # init grid
blank = [[cell for i in range(2)] for j in range(2)] # init grid blank # this debug
gridtree = [[]]
setrecursionlimit(1000000)
# this too debug # init blanks in grid
grid[5][5] = blank
grid[2][3] = blank
grid[7][4] = blank
grid[4][9] = blank
#grid[5][5][1][1] = blank
#grid[2][3][0][1] = blank

# func block

def GridChecker(cell): # check cell is grid or not if not return its not chunk go next, else jump in chunk and check of cell in this chunk
	if type(cell) == type([]):
		return True
	return False

# # # # # # # 

def CellDirection(dirname): # direction library by direction name
	directions = {'down' : (0, 1),
	  			'up' : (0, -1),
	  			'right' : (1, 0),
	  			'left' : (-1, 0)}
	find = dirname.find('-')

	if find != -1:
		if firstdir in directions and seconddir in directions:
			firstdir = dirname[:find]
			seconddir = dirname[find+1:]
			dx, dy = directions[firstdir][0] + directions[seconddir][0], directions[firstdir][1] + directions[seconddir][1]	
			return dx, dy
		else:
			dx, dy = directions['down'][0], directions['down'][1]
			return dx, dy 
	else:
		dx, dy = directions[dirname][0], directions[dirname][1]
		return dx, dy

# # # # # # #    
	
def CellCalculate(grid, x, y, prevx, prevy):	# cell in another chunk position calculate
	xline = len(grid) - 1
	yline = len(grid[0]) - 1
	dx, dy = x - prevx, y - prevy
	if dx != 0:
		xline = xline // 2
		return xline, 0
	if dy != 0:
		yline = yline // 2
		return 0, yline

# # # # # # # 

def CellCanMove(grid, x, y, dirname): # check: cell can move or no, if no return no move oOps sory... 
	dx, dy = CellDirection(dirname)
	xborder = len(grid) 
	yborder = len(grid[x])
	print(grid, grid[0], f'x - {x}')
	if ((x+dx != xborder or x+dx != 0) and (y+dy != yborder or y+dy != 0)) and grid[x+dx][y+dy] == empty:
		return True
	return False

# # # # # # # 
		
def CellMove(grid, x, y, dirname): # move cells in chunks
    
	if CellCanMove(grid, x, y, dirname) and grid[x][y] == cell:
		dx, dy = CellDirection(dirname)
		grid[x][y] = empty
		x, y = CellCalculate(grid, x, y, x-dx, y-dy)
		grid[x][y] = 1
	print(grid[x][y])
		


# # # # # # # # # # # # # #  

def CellSearcher(grid, depth):	# recursion function, she search all cell and use upper func & she move all cell to direction
	for x in range(len(grid)):
		for y, cell in enumerate(grid):
			if GridChecker(cell):
				if GridChecker(cell[x]):
					subgrid = cell
					depth += 1
					CellSearcher(subgrid[x], depth)
			else:
				CellMove(grid, x, y, 'down')
	

		




							