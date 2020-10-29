# Caroline Davis (cnd7cy)
# farmProblem.py
# adapted from:
# https://edabit.com/challenge/QzXtDnSZL6y4ZcEvT
# given the number of animals, count the number of legs
def farmProblem(chickens, cows, pigs):
    chicken_legs = chickens * 2
    cow_legs = cows * 4
    pig_legs = pigs * 4
    legs = chicken_legs + cow_legs + pig_legs
    return legs
