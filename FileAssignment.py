with open('div.txt') as fp:
    qs = fp.readlines()

total = 0

for lines in qs:
    a, b = lines.split("/")
    quotient = int(a) / int(b)
    newTotal = quotient + total

print(newTotal)















