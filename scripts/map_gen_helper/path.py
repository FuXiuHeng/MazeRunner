from enum import Enum
from . import constants
from . import general

class PathStrategy(Enum):
  NO_SURR_PATHS = 0
  NO_ADJ_PATHS = 1

# Determines whether the current cell should be set as a path
def shouldSetPath(grid, curCell, strategy):
  width = general.getGridWidth(grid)
  height = general.getGridHeight(grid)
  curCoord = curCell['curCoord']
  prevCoord = curCell['prevCoord']
  
  # Always set cell if it is the first cell (i.e. no preceding path cells)
  if prevCoord['row'] == -1: return True

  # Strategy: No surrounding (adjacent/cornering) paths
  if strategy == PathStrategy.NO_SURR_PATHS:
    forwardCoords = general.getForwardSurroundingCoords(curCoord, prevCoord)
  # Strategy: No adjacent paths
  else:
    forwardCoords = general.getForwardAdjacentCoords(curCoord, prevCoord)

  for coord in forwardCoords:
    if general.isOnOrOutOfBounds(coord, width, height):
      continue
    elif general.getCellType(grid, coord) == constants.CELL_PATH:
      return False

  return True
