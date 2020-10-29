# Caroline Davis (cnd7cy)
# factorial.py

def factorial(n):
    f_list = []
    f = 1
    for i in range(1, n + 1):
        f_list.append(i)
    for num in f_list:
        f = f * num
    return f
