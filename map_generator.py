import os
import random 
from scripts import map_generator_helper as helper

# Map type constants
CELL_NONE = 'X' # Not yet decided what cell value to take on
CELL_START = 'S'
CELL_END = 'E'
CELL_WALL = 'W'
CELL_PATH = ' '

# Parsing inputs and input validation
print('-------------------------')
print('     Map Generator!!     ')
print('-------------------------')
width = int(input('Please enter grid width: '))
height = int(input('Please enter grid height: '))

if width < 3 or height < 3:
  raise Exception('width and height must be greater than 3!')

# Initialising grid
grid = []
for row in range(width):
  gridRow = []
  for col in range(height):
    gridRow.append(CELL_NONE)
  grid.append(gridRow)

# Randomise a ending position along the side walls
# but not the corners
endCoord = helper.generateRandomEnd(width, height)
helper.setCell(grid, endCoord, CELL_END)

# Stores a list of possible path cells that stems from a previous
# path cell or end cell
frontier = []
helper.expandFrontier(grid, frontier, endCoord)
while frontier:
  i = random.randrange(0, len(frontier))
  coord = frontier[i]
  frontier.pop(i)
  if helper.getCell(grid, coord) == CELL_NONE:
    helper.setCell(grid, coord, CELL_PATH)
    helper.expandFrontier(grid, frontier, coord)
  
# Write grid to file
helper.fillGridWalls(grid)
helper.setRandomPlayerCoord(grid)
outFile = open(os.path.join("src", "maps", "generated_map.ts"), "w")
helper.writeToTSFile(grid, outFile)
outFile.close()
# helper.printGrid(grid)
