import math
pos = [0,0]
while True:
    s = input("Enter U/D/L/R as prefix for the movement: ")
    if not s:
        break
    movement = s.split(" ")
    direction = movement[0]
    steps = int(movement[1])
    if direction=="U":
        pos[1]+=steps
    elif direction=="D":
        pos[1]-=steps
    elif direction=="L":
        pos[0]-=steps
    elif direction=="R":
        pos[0]+=steps
    else:
        pass

print (int(round(math.sqrt(pos[1]**2+pos[0]**2)))) # Euclidean Formula