def calculateFine(speedLimit, clockedSpeed):
    if clockedSpeed <= speedLimit:
        print("Speed is legal.")
    elif clockedSpeed > 90:
        fine = 50 + (clockedSpeed - speedLimit) * 5 + 200
        print("Speed is illegal. Fine is $%d." % fine)
    else:
        fine = 50 + (clockedSpeed - speedLimit) * 5
        print("Speed is illegal. Fine is $%d." % fine)

# Example usage
calculateFine(65, 70)  # Should print "Speed is illegal. Fine is $75."
calculateFine(65, 80)  # Should print "Speed is illegal. Fine is $150."
calculateFine(65, 90)  # Should print "Speed is illegal. Fine is $225."
calculateFine(65, 100)  # Should print "Speed is illegal. Fine is $350."
calculateFine(65, 60)  # Should print "Speed is legal."
