t = int(input())
op = [' + ',' - ',' // ',' * ']
ans_str = []
ans_calc = []

for i in op:
    for j in op:
        for k in op:
            eq_str = '4'+ i + '4' + j + '4' + k + '4'
            calc_str = eval(eq_str)
            ans_calc.append(calc_str)
            ans_str.append(eq_str.replace('//','/') + " = " + str(calc_str))

for _ in range(t):
    n = int(input())
    if n > 256 or n < -60 or n not in ans_calc:
        print('no solution')
    else:
        print(ans_str[ans_calc.index(n)])
        