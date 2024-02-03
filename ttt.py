import numpy as np
arr = np.char.array([["-","-","-"],["-","-","-"],["-","-","-"]])
print(arr)
def choi(ele):
  cho = int(input("Choose which square to choose (1-9)"))
  if 1 <= cho <= 9:
    row = (cho - 1) // 3
    col = (cho - 1) % 3
    arr[row][col] = ele
  else:
    print("Please choose a number between 1 and 9.")
  if ele
  print(arr)
while True:
  choi(ele="X")
  choi(ele="O")
