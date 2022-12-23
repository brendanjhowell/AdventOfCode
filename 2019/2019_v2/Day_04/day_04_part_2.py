min_password = 256310
max_password = 732736
sol_set = []
n = min_password

while n <= max_password:
    p = list(str(n))
    monotonic_flag = 1
    double_digit_flag = 0
    i = 0
    while i + 1 < len(p):
        if p[i+1]<p[i]:
            monotonic_flag = 0
        if p[i] == p[i+1]:
            e = 1
            double_find = 1
            while i + 1 + e < len(p) and double_find == 1:
                if p[i] == p[i+1+e]:
                    e+=1
                else:
                    double_find = 0
            if e == 1:
                double_digit_flag = 1
            i+=e
        else:
            i+=1
    if monotonic_flag == 1 and double_digit_flag == 1:
        sol_set.append(n)
    else:
        fail_set.append(n)
    n+=1

print(sol_set)
print(len(sol_set))
