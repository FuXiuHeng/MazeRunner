import os
import random 
from map_gen_helper import constants
from map_gen_helper import debugger
from map_gen_helper import frontier as frontierHelper
from map_gen_helper import general

# Parsing inputs and input validation
print('-------------------------')
print('     Map Generator!!     ')
print('-------------------------')
width = int(input('Please enter grid width: '))
height = int(input('Please enter grid height: '))

if width < 3 or height < 3:
  raise Exception('width and height must be greater than 3!')

# Initialising grid
grid = general.initialiseGrid(width, height)

# Randomise a ending position along the side walls
# but not the corners
endCoord = general.generateRandomEnd(width, height)
endCell = {
  'type': constants.CELL_END,
  'curCoord': endCoord,
  'prevCoord': { 'row': -1, 'col': -1 },
  'distToEnd': 0,
}
general.setCell(grid, endCoord, endCell)

# Stores a list of possible path cells that stems from a previous
# path cell or end cell
frontier = []
frontierHelper.expandFrontier(grid, frontier, endCell)
while frontier:
  # Selection strategy: Take randomly from the currently expanded frontier
  i = random.randrange(0, len(frontier))
  cell = frontier[i]
  coord = cell['curCoord']
  frontier.pop(i)

  if cell['type'] != constants.CELL_NONE: continue

  # Path set strategy
  prevCoord = cell['prevCoord']
  if prevCoord['row'] != -1:
    surrCoords = general.getForwardSurroundingCoords(coord, prevCoord)
    discard = False
    for coordA in surrCoords:
      if general.isOnOrOutOfBounds(coordA, width, height):
        continue
      elif general.getCellType(grid, coordA) == constants.CELL_PATH:
        discard = True
        break

    if discard: continue
    general.setCellType(grid, coord, constants.CELL_PATH)

  # Expand strategy
  frontierHelper.expandFrontier(grid, frontier, cell)

# Write grid to file
general.fillGridWalls(grid)
general.setRandomPlayerCoord(grid)
outFile = open(os.path.join("src", "maps", "generated_map.ts"), "w")
general.writeToTSFile(grid, outFile)
outFile.close()

# debugger.printGrid(grid)
