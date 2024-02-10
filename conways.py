
# A Conway's life game
import random
import time

LIFE='@'
DEATH=' '
SPEED=5 # betewen 1 and 10
DENSITY=75  # between 1 and 1000
WIDTH=80
HEIGHT=40

grid = []
def createConwaysGrid():
  global grid
  density = 1 - DENSITY/1000
  grid = [[LIFE if random.random() > density else DEATH for j in range(WIDTH)] for i in range(HEIGHT)]
  #print(grid)
    
def displayConwaysGrid():
  global grid
  # Display the grid.
  print()
  try:
    for i in range(HEIGHT):
      print (''.join(grid[i]))
  except Exception as e:
    print(f"error sur i={i}, {e}")
  # go back to top
  print("\033[F"*(HEIGHT+2))

def life(i, j):
  global grid
  try:
    neighbours = 0
    if i>0 and j>0 and grid[i-1][j-1] == LIFE: neighbours += 1
    if i>0 and grid[i-1][j] == LIFE: neighbours += 1
    if i>0 and j<WIDTH-1 and grid[i-1][j+1] == LIFE: neighbours += 1
    if j>0 and grid[i][j-1] == LIFE: neighbours += 1
    if j<WIDTH-1 and grid[i][j+1] == LIFE: neighbours += 1
    if i<HEIGHT-1 and j>0 and grid[i+1][j-1] == LIFE: neighbours += 1
    if i<HEIGHT-1 and grid[i+1][j] == LIFE: neighbours += 1
    if i<HEIGHT-1 and j<WIDTH-1 and grid[i+1][j+1] == LIFE: neighbours += 1
    if grid[i][j] == LIFE:
      if neighbours < 2 or neighbours > 3 :
        grid[i][j] = DEATH
    else:
      if neighbours == 3:
        grid[i][j] = LIFE
  except Exception:
    print(f"Exception on i,j: {i},{j}")
    
def nextConwaysGrid():
  global grid
  changed=False
  for i in range(HEIGHT):
    for j in range(WIDTH):
      try:
        res = life(i, j)
        if (res != grid[i][j]):
          changed = True
          grid[i][j] = res
      except Exception as e:
        print(f"Exception on i,j: {i},{j}, {e}")
        raise e
  return changed

def conwayLifeGame():
    createConwaysGrid()
    count = 0
    while True:
      displayConwaysGrid()
      changed = nextConwaysGrid()
      if not changed:
        count += 1
        createConwaysGrid()
        print (f"New grid! ({count})")
        time.sleep(3)
      else:
        time.sleep(2/SPEED)
     
conwayLifeGame()