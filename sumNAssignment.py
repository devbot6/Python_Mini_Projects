def sumN(n):
    sum = (n*(n+1))/2
    print(sum)


def sumNCubes(n):
    sum = ((n * (n + 1)) / 2)**3
    print(sum)



def main():
    userN = eval(input("Give me an N value: "))
    sumN(userN)
    sumNCubes(userN)


if __name__ == '__main__':
    main()