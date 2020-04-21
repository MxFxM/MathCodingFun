if __name__ == '__main__':
    import timeit
    print(timeit.timeit("math.sqrt(1000)", setup="import math"))
