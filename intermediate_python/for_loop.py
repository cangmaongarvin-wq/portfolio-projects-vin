
import numpy as np

offset = -6

while offset != 0:
    print("correcting...")
    if offset > 0:
        offset = offset -1
    else:
        offset = offset + 1
        print(offset)
print()

areas = [11.25, 18.0, 20.0, 10.75, 9.50]

for index, a in enumerate(areas):
    print("room " 
          + str(index +1) # to start the index at 1 instead of 0
          + ": " 
          + str(a))
print()

house = [["hallway", 11.25], 
         ["kitchen", 18.0], 
         ["living room", 20.0], 
         ["bedroom", 10.75], 
         ["bathroom", 9.50]]

for room, area in house:
    print("The "
          + room
          + " is "
          + str(area)
          + " sqm")