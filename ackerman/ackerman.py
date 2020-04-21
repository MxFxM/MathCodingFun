import sys

print(
    f"After testing, use sys.setrecursionlimit({sys.getrecursionlimit()}) to reset to default")
print("It might reset by itself.")
print("Change limit at your own risk!")

# sys.setrecursionlimit(100000)


# use only with positive integers
def ack(m, n):
    ans = 0
    if m == 0:
        ans = n+1
    elif n == 0:
        ans = ack(m-1, 1)
    else:
        ans = ack(m-1, ack(m, n-1))
    return ans


for i in range(6):
    for j in range(6):
        print(f"Ackerman({i}, {j}) = {ack(i, j)}")
