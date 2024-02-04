import numpy as np
arr2 = np.char.array([["1","2","3"],["4","5","6"],["7","8","9"]])
print(arr2)
arr = np.char.array([["-","-","-"],["-","-","-"],["-","-","-"]])
print(arr)
def choi(ele):
  try:
    print(f"{ele}'s turn")
    cho = int(input("Choose which square to choose (1-9):"))
    if 1 <= cho <= 9:
      row = (cho - 1) // 3
      col = (cho - 1) % 3
      r = row
      c = col
      if arr[r,c] == "-":
        arr[row][col] = ele
        print(arr)
        return True
      else:
        print("Alreadly occupied. Try again.")
        return False
    else:
      print("Please choose a number between 1 and 9. Try again.")
      return False
  except ValueError:
    print("Please choose a number between 1 and 9. Try again.")
    return False
def wc():
  for peei in range(3):
    if arr[peei, 0] == arr[peei, 1] == arr[peei, 2] != '-':
        return True
    if arr[0, peei] == arr[1, peei] == arr[2, peei] != '-':
      return True
  if arr[0, 0] == arr[1, 1] == arr[2, 2] != '-':
      return True
  if arr[0, 2] == arr[1, 1] == arr[2, 0] != '-':
      return True
def tie():
  return not np.any(arr == '-')
while True:
  choi(ele="X")
  if wc():
    print("X Wins")
    break
  elif tie():
    print("It's a tie")
    break
  choi(ele="O")
  if wc():
    print("O Wins")
    break
  elif tie():
    print("It's a tie")
    break
