def computepay(hrs, rate):
    if hrs > 40:
        regular = 40 * rate
        overtime = (hrs - 40) * (rate * 1.5)
        return regular + overtime
    else:
        return hrs * rate

hrs = input("Enter Hours: ")
rate = input("Enter Rate: ")

hrs = float(hrs)
rate = float(rate)

p = computepay(hrs, rate)
print("Pay", p)
