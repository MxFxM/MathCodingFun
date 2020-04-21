import sys

print(
    f"After testing, use sys.setrecursionlimit({sys.getrecursionlimit()}) to reset to default")
print("It might reset by itself.")
print("Change limit at your own risk!")

# sys.setrecursionlimit(100000)

lookUpTable = {}


# use only with positive integers
def ack(m, n):
    global lookUpTable
    ans = 0

    if (m, n) in lookUpTable:
        ans = lookUpTable[(m, n)]
    else:
        if m == 0:
            ans = n+1
        elif n == 0:
            ans = ack(m-1, 1)
        else:
            ans = ack(m-1, ack(m, n-1))
        lookUpTable[(m, n)] = ans
    return ans


for i in range(6):
    for j in range(1):
        print(f"Ackerman({i}, {j}) = {ack(i, j)}")
print(lookUpTable)

# (0, n) ist genau n + 1
# (m, 0) ist das selbe wie (m-1, 1)
# (1, 1) ist (0, (1, 0)) ist (0, 2) ist 3
# (2, 1) ist (1, (2, 0)) ist (1, (1, 1)) ist (1, (0, (1, 0))) ist (1, (0, 2)) ist (1, 3) ist (0, (1, 2)) ist (0, ...)