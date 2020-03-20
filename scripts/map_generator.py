import os
import random 
from map_gen_helper import general
from map_gen_helper import frontier as frontierHelper
from map_gen_helper import constants

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
    gridRow.append(constants.CELL_NONE)
  grid.append(gridRow)

# Randomise a ending position along the side walls
# but not the corners
endCoord = general.generateRandomEnd(width, height)
general.setCell(grid, endCoord, constants.CELL_END)

# Stores a list of possible path cells that stems from a previous
# path cell or end cell
frontier = []
frontierHelper.expandFrontier(grid, frontier, endCoord)
while frontier:
  # Expand strategy: Take randomly from the currently expanded frontier
  i = random.randrange(0, len(frontier))
  coord = frontier[i]
  frontier.pop(i)
  if general.getCell(grid, coord) == constants.CELL_NONE:
    general.setCell(grid, coord, constants.CELL_PATH)
    frontierHelper.expandFrontier(grid, frontier, coord)
  
# Write grid to file
general.fillGridWalls(grid)
general.setRandomPlayerCoord(grid)
outFile = open(os.path.join("src", "maps", "generated_map.ts"), "w")
general.writeToTSFile(grid, outFile)
outFile.close()
# general.printGrid(grid)
