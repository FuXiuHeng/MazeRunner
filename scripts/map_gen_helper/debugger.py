def printGrid(grid):
  gridValues = list(map(
      lambda row: list(map(
        lambda cell: cell['value'], row
      )), grid
    ))
  for row in gridValues:
    print(row)