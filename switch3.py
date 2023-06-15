def numberToString(argument):
    match argument:
        case 0:
            return "zero"
        case 1:
            return "one"
        case 3:
            return "two"
        case default:
            return "something"

if __name__ == '__main__':
    argument = 1
    print(numberToString(argument))