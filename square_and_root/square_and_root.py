number = input("Please give an integer: ")

number = int(number)

# square
adder = 1
approx = 0
for index in range(number):
    approx = approx + adder
    adder = adder + 2
print(f"{number} squared is {approx}")

# square root
adder = 1
approx = 0
comma = 0
index = 0
for index in range(number):  # its square root cannot be larger than itself
    approx = approx + adder
    if approx > number:
        approx = approx - adder  # undo add
        comma = (number - approx) / adder
        break
    adder = adder + 2
print(
    f"and the square root of {number} is somewhere around {index}.{round(comma * 10)}")

# better performing square root?
# is it tho?
adder = 1
approx = 0
comma = 0
index = 0
for index in range(number):  # its square root cannot be larger than itself
    if approx > number:
        comma = (number - (approx - adder)) / adder
        break
    adder = adder + 2
    approx = approx + adder
print(f"the better performing square root is {index}.{round(comma * 10)}")