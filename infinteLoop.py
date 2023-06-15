def main():
    sum = 0.0
    count = 0
    moreData = "yes"

    while moreData[0] == "y":
        x = float(input("Enter a number: "))
        sum = sum + x
        count = count + 1
        moreData = input("Do you have more numbers yes or no ")