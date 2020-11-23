

wire_path_coordinates = open("C:/Users/brend/Downloads/Advent of Code/2019/Day_03/mh_distance_coordinates.txt", "r")

total_w_path = wire_path_coordinates.read().splitlines()#.split(",")

first_w_path = total_w_path[0].split(",")
second_w_path = total_w_path[1].split(",")

intersection_coords = []

#First path coorinate list [X, Y]
f_x = 0
f_y = 0
f_steps = 0
first_w_path_coord = [[f_x, f_y, f_steps]]
i = 0
while i < len(first_w_path):
    c = list(first_w_path[i])
    if c[0] == 'U':
        v = int(''.join(c[1:]))
        j = 1
        while j <= v:
            f_y+=1
            f_steps+=1
            first_w_path_coord.append([f_x, f_y, f_steps])
            j+=1
    elif c[0] == 'D':
        v = int(''.join(c[1:]))
        j = 1
        while j <= v:
            f_y-=1
            f_steps+=1
            first_w_path_coord.append([f_x, f_y, f_steps])
            j+=1
    elif c[0] == 'L':
        v = int(''.join(c[1:]))
        j = 1
        while j <= v:
            f_x-=1
            f_steps+=1
            first_w_path_coord.append([f_x, f_y, f_steps])
            j+=1
    elif c[0] == 'R':
        v = int(''.join(c[1:]))
        j = 1
        while j <= v:
            f_x+=1
            f_steps+=1
            first_w_path_coord.append([f_x, f_y, f_steps])
            j+=1
    i+=1


first_w_path_coord_dict = {}
i = 0
while i < len(first_w_path_coord):
    if str(first_w_path_coord[i][0])+"_"+str(first_w_path_coord[i][1]) not in first_w_path_coord_dict:
        first_w_path_coord_dict[str(first_w_path_coord[i][0])+"_"+str(first_w_path_coord[i][1])] = first_w_path_coord[i][2]
    i+=1
#print(first_w_path_coord_dict)
#print(len(first_w_path_coord_dict))
#print(len(first_w_path_coord))

#As you'll notice from the output, a path can intersect with itself. We want to preserve the lowest steps at that point.

#Second path coorinate list [X, Y]
s_x = 0
s_y = 0
s_steps = 0
second_w_path_coord = [[s_x, s_y, s_steps]]
i = 0
while i < len(second_w_path):
    c = list(second_w_path[i])
    if c[0] == 'U':
        v = int(''.join(c[1:]))
        j = 1
        while j <= v:
            s_y+=1
            s_steps+=1
            second_w_path_coord.append([s_x, s_y, s_steps])
            if str(s_x)+"_"+str(s_y) in first_w_path_coord_dict:
                intersection_coords.append([s_x, s_y, s_steps+first_w_path_coord_dict[str(s_x)+"_"+str(s_y)]])
            j+=1
    elif c[0] == 'D':
        v = int(''.join(c[1:]))
        j = 1
        while j <= v:
            s_y-=1
            s_steps+=1
            second_w_path_coord.append([s_x, s_y, s_steps])
            if str(s_x)+"_"+str(s_y) in first_w_path_coord_dict:
                intersection_coords.append([s_x, s_y, s_steps+first_w_path_coord_dict[str(s_x)+"_"+str(s_y)]])
            j+=1
    elif c[0] == 'L':
        v = int(''.join(c[1:]))
        j = 1
        while j <= v:
            s_x-=1
            s_steps+=1
            second_w_path_coord.append([s_x, s_y, s_steps])
            if str(s_x)+"_"+str(s_y) in first_w_path_coord_dict:
                intersection_coords.append([s_x, s_y, s_steps+first_w_path_coord_dict[str(s_x)+"_"+str(s_y)]])
            j+=1
    elif c[0] == 'R':
        v = int(''.join(c[1:]))
        j = 1
        while j <= v:
            s_x+=1
            s_steps+=1
            second_w_path_coord.append([s_x, s_y, s_steps])
            if str(s_x)+"_"+str(s_y) in first_w_path_coord_dict:
                intersection_coords.append([s_x, s_y, s_steps+first_w_path_coord_dict[str(s_x)+"_"+str(s_y)]])
            j+=1
    i+=1
#print(len(second_w_path_coord))

min_steps = intersection_coords[0][2]
i = 1
while i < len(intersection_coords):
    if intersection_coords[i][2] < min_steps:
        min_steps = intersection_coords[i][2]
    i+=1
print(min_steps)



#intersection = intersection(first_w_path_coord, second_w_path_coord)
#print(intersection_coords)

# sol = abs(intersection_coords[0][0]) + abs(intersection_coords[0][1])
# i = 1
# while i < len(intersection_coords):
#     t = abs(intersection_coords[i][0])+abs(intersection_coords[i][1])
#     if t < sol:
#         sol = t
#     i+=1
#
# print(sol)

# j = 0
# while j < len(second_w_path_coord):
#     i = 0
#     while i < len(first_w_path_coord):
#         if second_w_path_coord[j][:2] == first_w_path_coord[i][:2]:
#             intersection_coords.append([second_w_path_coord[j][0], second_w_path_coord[j][1], second_w_path_coord[j][2]+first_w_path_coord[i][2]])
#         i+=1
#     j+=1
