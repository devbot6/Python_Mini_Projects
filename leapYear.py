def main():
    leapInput = eval(input("Enter a year:"))

    if (leapInput % 4 == 0) & (leapInput % 100 != 0):
        print("Yes its a leapyear")
    else:
        print("No its not a leap year.")



main()
