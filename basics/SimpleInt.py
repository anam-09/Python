principle = float(input("Enter principle amount"))
rate = float(input("Enter rate of interest"))
Time = float(input("Enter Time in years"))

simple_interest = (principle * rate * Time) / 100
total_amount = principle + simple_interest
print(simple_interest)
print(total_amount)
