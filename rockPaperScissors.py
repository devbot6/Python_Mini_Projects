from random import randint


def main():
    move = eval(input("What is your move? (1-rock, 2-paper, 3-scissors)"))
    random = randint(1, 3)

    if(move == random):
        print("tie")
    elif(move == 1 & random == 3):
        print("You Win")
    elif(move == 2 & random == 1):
        print("you win")
    elif(move == 3 & random == 1):
        print("you win")
    else:
        print("You lose")


if __name__ == '__main__':
    main()

