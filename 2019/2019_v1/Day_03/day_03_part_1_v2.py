

wire_path_coordinates = open("C:/Users/brend/Downloads/Advent of Code/2019/Day_03/mh_distance_coordinates.txt", "r")

total_w_path = wire_path_coordinates.read().splitlines()#.split(",")

first_w_path = total_w_path[0].split(",")
second_w_path = total_w_path[1].split(",")

intersection_coords = []

#First path coorinate list [X, Y]
f_x = 0
f_y = 0
first_w_path_coord = [[f_x, f_y]]
i = 0
while i < len(first_w_path):
    c = list(first_w_path[i])
    if c[0] == 'U':
        v = int(''.join(c[1:]))
        j = 1
        while j <= v:
            f_y+=1
            first_w_path_coord.append([f_x, f_y])
            j+=1
    elif c[0] == 'D':
        v = int(''.join(c[1:]))
        j = 1
        while j <= v:
            f_y-=1
            first_w_path_coord.append([f_x, f_y])
            j+=1
    elif c[0] == 'L':
        v = int(''.join(c[1:]))
        j = 1
        while j <= v:
            f_x-=1
            first_w_path_coord.append([f_x, f_y])
            j+=1
    elif c[0] == 'R':
        v = int(''.join(c[1:]))
        j = 1
        while j <= v:
            f_x+=1
            first_w_path_coord.append([f_x, f_y])
            j+=1
    i+=1

#print(len(first_w_path_coord))

#Second path coorinate list [X, Y]
s_x = 0
s_y = 0
second_w_path_coord = [[s_x, s_y]]
i = 0
while i < len(second_w_path):
    c = list(second_w_path[i])
    if c[0] == 'U':
        v = int(''.join(c[1:]))
        j = 1
        while j <= v:
            s_y+=1
            second_w_path_coord.append([s_x, s_y])
            if [s_x, s_y] in first_w_path_coord:
                intersection_coords.append([s_x, s_y])
            j+=1
    elif c[0] == 'D':
        v = int(''.join(c[1:]))
        j = 1
        while j <= v:
            s_y-=1
            second_w_path_coord.append([s_x, s_y])
            if [s_x, s_y] in first_w_path_coord:
                intersection_coords.append([s_x, s_y])
            j+=1
    elif c[0] == 'L':
        v = int(''.join(c[1:]))
        j = 1
        while j <= v:
            s_x-=1
            second_w_path_coord.append([s_x, s_y])
            if [s_x, s_y] in first_w_path_coord:
                intersection_coords.append([s_x, s_y])
            j+=1
    elif c[0] == 'R':
        v = int(''.join(c[1:]))
        j = 1
        while j <= v:
            s_x+=1
            second_w_path_coord.append([s_x, s_y])
            if [s_x, s_y] in first_w_path_coord:
                intersection_coords.append([s_x, s_y])
            j+=1
    i+=1
#print(len(second_w_path_coord))

def intersection(lst1, lst2):
    lst3 = [value for value in lst1 if value in lst2]
    return lst3

#intersection = intersection(first_w_path_coord, second_w_path_coord)
#print(intersection_coords)

sol = abs(intersection_coords[0][0]) + abs(intersection_coords[0][1])
i = 1
while i < len(intersection_coords):
    t = abs(intersection_coords[i][0])+abs(intersection_coords[i][1])
    if t < sol:
        sol = t
    i+=1

print(sol)
