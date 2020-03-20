import random
from . import constants

addToFrontier = True

# Randomise a ending position along the side walls
# but not the corners
def generateRandomEnd(width, height): 
  side = random.randrange(0, 4)
  if side == 0: # Top
    endCoord = { 'row': 0, 'col': random.randrange(1, width - 1) }
  elif side == 1: # Bottom
    endCoord = { 'row': height - 1, 'col': random.randrange(1, width - 1) }
  elif side == 2: # Left
    endCoord = { 'row': random.randrange(1, height - 1), 'col': 0 }
  else: # Right
    endCoord = { 'row': random.randrange(1, height - 1), 'col': width - 1 }
  return endCoord

def getGridHeight(grid):
  return len(grid)

def getGridWidth(grid):
  return len(grid[0])

def isOnOrOutOfBounds(curCoord, width, height):
  if curCoord['row'] <= 0 or curCoord['row'] >= height - 1 \
      or curCoord['col'] <= 0 or curCoord['col'] >= width - 1:
    return True
  else:
    return False

def isOutOfBounds(curCoord, width, height):
  if curCoord['row'] < 0 or curCoord['row'] >= height \
      or curCoord['col'] < 0 or curCoord['col'] >= width:
    return True
  else:
    return False

def getAdjacentCoords(curCoord):
  adjCoords = [
    { 'row': curCoord['row'] - 1, 'col': curCoord['col'] },
    { 'row': curCoord['row'] + 1, 'col': curCoord['col'] },
    { 'row': curCoord['row'], 'col': curCoord['col'] - 1 },
    { 'row': curCoord['row'], 'col': curCoord['col'] + 1 },
  ]
  return adjCoords

def getCell(grid, coord):
  return grid[coord['row']][coord['col']]

def setCell(grid, coord, cellValue):
  grid[coord['row']][coord['col']] = cellValue

def printGrid(grid):
  for row in grid:
    print(row)

# Replaces all the CELL_NONE values in the grid with CELL_WALL
def fillGridWalls(grid):
  height = getGridHeight(grid)
  width = getGridWidth(grid)
  for row in range(height):
    for col in range(width):
      if grid[row][col] == constants.CELL_NONE:
        grid[row][col] = constants.CELL_WALL

def setRandomPlayerCoord(grid):
  height = getGridHeight(grid)
  width = getGridWidth(grid)
  for row in range(height):
    for col in range(width):
      if grid[row][col] == constants.CELL_PATH:
        grid[row][col] = constants.CELL_START
        return

tsTemplate = """
import {{ Map }} from 'src/maps/map_types';

export const map: Map = {{
  width: {},
  height: {},
  grid: {},
}}
"""

def writeToTSFile(grid, outFile):
  height = getGridHeight(grid)
  width = getGridWidth(grid)
  
  outFile.write(tsTemplate.format(width, height, grid))