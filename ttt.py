import numpy as np
arr = np.char.array([["-","-","-"],["-","-","-"],["-","-","-"]])
print(arr)
def choi(ele):
  cho = int(input("Choose which square to choose (1-9)"))
  if cho == 1:
    arr[0][0] = ele
  elif cho == 2:
    arr[0][1] = ele
  elif cho == 3:
    arr[0][2] = ele
  elif cho == 4:
    arr[1][0] = ele
  elif cho == 5:
    arr[1][1] = ele
  elif cho == 6:
    arr[1][2] = ele
  elif cho == 7:
    arr[2][0] = ele
  elif cho == 8:
    arr[2][1] = ele
  elif cho == 9:
    arr[2][2] = ele
  else:
    print("Put an input from 0-9")
  print(arr)
while victory := false:
  choi(ele="X")
  choi(ele="O")
