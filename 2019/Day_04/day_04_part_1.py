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
            double_digit_flag = 1
        i+=1
    if monotonic_flag == 1 and double_digit_flag == 1:
        sol_set.append(n)
    n+=1

print(len(sol_set))
