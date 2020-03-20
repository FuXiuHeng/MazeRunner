import random
from . import constants

def initialiseGrid(width, height):
  grid = []
  for row in range(width):
    gridRow = []
    for col in range(height):
      gridRow.append(createCell(
        constants.CELL_NONE,
        { 'row': -1, 'col': -1 },
        -1,
      ))
    grid.append(gridRow)
  return grid

def createCell(value, prevCoord, distToEnd):
  return {
    'value': value,
    'prevCoord': prevCoord,
    'distToEnd': distToEnd,
  }

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

# Note: curCoord and prevCoord must be adjacent to each other!!
def getForwardAdjacentCoords(curCoord, prevCoord):
  if curCoord['row'] == prevCoord['row']: # Same row
    colDiff = curCoord['col'] - prevCoord['col']
    adjCoords = [
      { 'row': curCoord['row'] - 1, 'col': curCoord['col'] },
      { 'row': curCoord['row'] + 1, 'col': curCoord['col'] },
      { 'row': curCoord['row'], 'col': curCoord['col'] + colDiff },
    ]
  else: # Same col
    rowDiff = curCoord['row'] - prevCoord['row']
    adjCoords = [
      { 'row': curCoord['row'], 'col': curCoord['col'] - 1 },
      { 'row': curCoord['row'], 'col': curCoord['col'] + 1 },
      { 'row': curCoord['row'] + rowDiff, 'col': curCoord['col'] },
    ]

  return adjCoords

# Note: curCoord and prevCoord must be adjacent to each other!!
def getForwardSurroundingCoords(curCoord, prevCoord):
  if curCoord['row'] == prevCoord['row']: # Same row
    colDiff = curCoord['col'] - prevCoord['col']
    surrCoords = [
      { 'row': curCoord['row'] - 1, 'col': curCoord['col'] },
      { 'row': curCoord['row'] + 1, 'col': curCoord['col'] },
      { 'row': curCoord['row'] - 1, 'col': curCoord['col'] + colDiff },
      { 'row': curCoord['row'] + 1, 'col': curCoord['col'] + colDiff },
      { 'row': curCoord['row'], 'col': curCoord['col'] + colDiff },
    ]
  else: # Same col
    rowDiff = curCoord['row'] - prevCoord['row']
    surrCoords = [
      { 'row': curCoord['row'], 'col': curCoord['col'] - 1 },
      { 'row': curCoord['row'], 'col': curCoord['col'] + 1 },
      { 'row': curCoord['row'] + rowDiff, 'col': curCoord['col'] - 1 },
      { 'row': curCoord['row'] + rowDiff, 'col': curCoord['col'] + 1 },
      { 'row': curCoord['row'] + rowDiff, 'col': curCoord['col'] },
    ]

  return surrCoords


def getCell(grid, coord):
  return grid[coord['row']][coord['col']]

def getCellValue(grid, coord):
  return grid[coord['row']][coord['col']]['value']

def setCellValue(grid, coord, cellValue):
  grid[coord['row']][coord['col']]['value'] = cellValue

# Replaces all the CELL_NONE values in the grid with CELL_WALL
def fillGridWalls(grid):
  height = getGridHeight(grid)
  width = getGridWidth(grid)
  for row in range(height):
    for col in range(width):
      if grid[row][col]['value'] == constants.CELL_NONE:
        grid[row][col]['value'] = constants.CELL_WALL

def setRandomPlayerCoord(grid):
  height = getGridHeight(grid)
  width = getGridWidth(grid)
  for row in range(height):
    for col in range(width):
      if grid[row][col]['value'] == constants.CELL_PATH:
        grid[row][col]['value'] = constants.CELL_START
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
  gridValues = list(map(
      lambda row: list(map(
        lambda cell: cell['value'], row
      )), grid
    ))
  outFile.write(tsTemplate.format(width, height, gridValues))
