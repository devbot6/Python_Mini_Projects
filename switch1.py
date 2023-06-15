def numbersToStrings(argument):
    switcher = {
        0: "zero",
        1: "one",
        2: "two"
    }

    return switcher.get(argument, "nothing")

if __name__ == '__main__':
    argument = 1
    print(numbersToStrings(argument))