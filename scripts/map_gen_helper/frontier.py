from . import constants
from . import debugger
from . import general

# Based on the current path cell, expand the frontier by considering
# the four adjacent cells.
def expandFrontier(grid, frontier, curCell):
  width = general.getGridWidth(grid)
  height = general.getGridHeight(grid)

  curCoord = curCell['curCoord']
  adjCoords = general.getAdjacentCoords(curCoord) 
  for coordA in adjCoords:
    # Discard cell if out of bounds
    # Discard cell if along the map sides
    if general.isOnOrOutOfBounds(coordA, width, height): continue
    # Discard cell if cell is already assigned a type
    if general.getCellType(grid, coordA) != constants.CELL_NONE: continue
    
    cell = {
      'type': constants.CELL_NONE,
      'curCoord': coordA,
      'prevCoord': curCoord,
      'distToEnd': curCell['distToEnd'] + 1,
    }
    frontier.append(cell)

  return