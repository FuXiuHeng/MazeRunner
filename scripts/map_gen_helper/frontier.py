from . import general
from . import constants

# Based on the current path cell, expand the frontier by considering
# the four adjacent cells.
def expandFrontier(grid, frontier, curCoord):
  adjCoords = general.getAdjacentCoords(curCoord)

  height = general.getGridHeight(grid)
  width = general.getGridWidth(grid)

  for coordA in adjCoords:
    # Discard cell if out of bounds
    # Discard cell if along the map sides
    if general.isOnOrOutOfBounds(coordA, width, height): continue
    # Discard cell if cell is already assigned a value
    if general.getCell(grid, coordA) != constants.CELL_NONE: continue
    # Discard cell if adjacent to another path (that is not the current cell)
    adjAdjCoords = general.getAdjacentCoords(coordA)
    addToFrontier = True

    for coordB in adjAdjCoords:
      if coordB == curCoord or general.isOnOrOutOfBounds(coordB, width, height):
        continue
      elif general.getCell(grid, coordB) == constants.CELL_PATH:
        general.setCell(grid, coordA, constants.CELL_WALL)
        addToFrontier = False
        break
    
    if addToFrontier: frontier.append(coordA)

  return