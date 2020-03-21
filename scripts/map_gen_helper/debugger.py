def printGrid(grid):
  gridTypes = list(map(
      lambda row: list(map(
        lambda cell: cell['type'], row
      )), grid
    ))
  for row in gridTypes:
    print(row)

def printFrontier(frontier):
  print("   Frontier   ")
  print("--------------")
  for cell in frontier:
    print(cell)
  print("--------------")
