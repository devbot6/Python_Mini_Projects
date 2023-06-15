def futval():
    print("This program calculates the future value")
    print("of a 10-year investment.")

    principal = float(input("Enter the initial principal: "))
    rate = float(input("Enter the annual interest rate (e.g. 0.05 for 5%): "))
    periods = int(input("Enter the number of times the interest is compounded per year: "))

    for i in range(10 * periods):
        principal = principal * (1 + rate/periods)

    print("The value of the investment after 10 years is:", principal)

futval()