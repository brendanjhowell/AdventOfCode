

wire_path_coordinates = open("C:/Users/brend/Downloads/Advent of Code/2019/Day_03/mh_distance_coordinates.txt", "r")

total_w_path = wire_path_coordinates.read().splitlines()#.split(",")

first_w_path = total_w_path[0].split(",")
second_w_path = total_w_path[1].split(",")

intersection_coords = []

#First path coorinate list [U, D, L, R]
f_u = 0
f_d = 0
f_l = 0
f_r = 0
first_w_path_coord = [[f_u, f_d, f_l, f_r]]
i = 0
while i < len(first_w_path):
    c = list(first_w_path[i])
    if c[0] == 'U':
        v = int(''.join(c[1:]))
        j = 1
        while j <= v:
            f_u+=1
            first_w_path_coord.append([f_u, f_d, f_l, f_r])
            j+=1
    elif c[0] == 'D':
        v = int(''.join(c[1:]))
        j = 1
        while j <= v:
            f_d+=1
            first_w_path_coord.append([f_u, f_d, f_l, f_r])
            j+=1
    elif c[0] == 'L':
        v = int(''.join(c[1:]))
        j = 1
        while j <= v:
            f_l+=1
            first_w_path_coord.append([f_u, f_d, f_l, f_r])
            j+=1
    elif c[0] == 'R':
        v = int(''.join(c[1:]))
        j = 1
        while j <= v:
            f_r+=1
            first_w_path_coord.append([f_u, f_d, f_l, f_r])
            j+=1
    i+=1

#Second path coorinate list [U, D, L, R]
s_u = 0
s_d = 0
s_l = 0
s_r = 0
second_w_path_coord = [[s_u, s_d, s_l, s_r]]
i = 0
while i < len(second_w_path):
    c = list(second_w_path[i])
    if c[0] == 'U':
        v = int(''.join(c[1:]))
        j = 1
        while j <= v:
            s_u+=1
            second_w_path_coord.append([s_u, s_d, s_l, s_r])
            if [s_u, s_d, s_l, s_r] in first_w_path_coord:
                intersection.append([s_u, s_d, s_l, s_r])
            j+=1
    elif c[0] == 'D':
        v = int(''.join(c[1:]))
        j = 1
        while j <= v:
            s_d+=1
            second_w_path_coord.append([s_u, s_d, s_l, s_r])
            if [s_u, s_d, s_l, s_r] in first_w_path_coord:
                intersection.append([s_u, s_d, s_l, s_r])
            j+=1
    elif c[0] == 'L':
        v = int(''.join(c[1:]))
        j = 1
        while j <= v:
            s_l+=1
            second_w_path_coord.append([s_u, s_d, s_l, s_r])
            if [s_u, s_d, s_l, s_r] in first_w_path_coord:
                intersection.append([s_u, s_d, s_l, s_r])
            j+=1
    elif c[0] == 'R':
        v = int(''.join(c[1:]))
        j = 1
        while j <= v:
            s_r+=1
            second_w_path_coord.append([s_u, s_d, s_l, s_r])
            if [s_u, s_d, s_l, s_r] in first_w_path_coord:
                intersection.append([s_u, s_d, s_l, s_r])
            j+=1
    i+=1

def intersection(lst1, lst2):
    lst3 = [value for value in lst1 if value in lst2]
    return lst3

#intersection = intersection(first_w_path_coord, second_w_path_coord)
print(intersection)

print(len(first_w_path_coord))
print(len(second_w_path_coord))
