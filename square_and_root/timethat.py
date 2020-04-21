def sqrt(number):
    adder = 1
    approx = 0
    comma = 0
    for index in range(number):  # its square root cannot be larger than itself
        approx = approx + adder
        if approx > number:
            approx = approx - adder  # undo add
            comma = (number - approx) / adder
            break
        adder = adder + 2


if __name__ == '__main__':
    import timeit
    print(timeit.timeit("sqrt(1000)", setup="from __main__ import sqrt"))
