# Caroline Davis (cnd7cy)
# fib.py
# Calculates the nth Fibonacci number


def fib(n):
    fibList = [0, 1, 1]
    next = 0
    f = 0;
    for i in range(n + 1):
        if i >= 3:
            next = fibList[i - 1] + fibList[i - 2]
            fibList.append(next)
    f = fibList[n - 1]
    return f

