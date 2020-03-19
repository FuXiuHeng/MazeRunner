import random

addToFrontier = True
# Map type constants
CELL_NONE = 'X' # Not yet decided what cell value to take on
CELL_START = 'S'
CELL_END = 'E'
CELL_WALL = 'W'
CELL_PATH = ' '

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

# Based on the current path cell, expand the frontier by considering
# the four adjacent cells.
def expandFrontier(grid, frontier, curCoord):
  adjCoords = getAdjacentCoords(curCoord)

  height = getGridHeight(grid)
  width = getGridWidth(grid)

  for coordA in adjCoords:
    # Discard cell if out of bounds
    # Discard cell if along the map sides
    if isOnOrOutOfBounds(coordA, width, height): continue
    # Discard cell if cell is already assigned a value
    if getCell(grid, coordA) != CELL_NONE: continue
    # Discard cell if adjacent to another path (that is not the current cell)
    adjAdjCoords = getAdjacentCoords(coordA)
    addToFrontier = True

    for coordB in adjAdjCoords:
      if coordB == curCoord or isOnOrOutOfBounds(coordB, width, height):
        continue
      elif getCell(grid, coordB) == CELL_PATH:
        setCell(grid, coordA, CELL_WALL)
        addToFrontier = False
        break
    
    if addToFrontier: frontier.append(coordA)

  return

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

def fillGridWalls(grid):
  height = getGridHeight(grid)
  width = getGridWidth(grid)
  for row in range(height):
    for col in range(width):
      if grid[row][col] == CELL_NONE:
        grid[row][col] = CELL_WALL

tsTemplate = """
import {{ Map }} from 'src/maps/map_types';

export const map: Map = {{
  width: {},
  height: {},
  grid: {},
}}
"""

def setRandomPlayerCoord(grid):
  height = getGridHeight(grid)
  width = getGridWidth(grid)
  for row in range(height):
    for col in range(width):
      if grid[row][col] == CELL_PATH:
        grid[row][col] = CELL_START
        return

def writeToTSFile(grid, outFile):
  height = getGridHeight(grid)
  width = getGridWidth(grid)
  
  outFile.write(tsTemplate.format(width, height, grid))