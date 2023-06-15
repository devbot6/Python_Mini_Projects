def numbersToStrings(argument):
    if argument == 0:
        return "zero"
    elif argument == 1:
        return "one"
    elif argument == 2:
        return "two"
    else:
        return "something"

if __name__ == '__main__':
    argument = 1
    print(numbersToStrings(argument))