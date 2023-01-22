hrs = input("enter hours worked ")
h = float(hrs)
rate = input("enter hourly rate ")
r = float(rate)
if h > 40:
    pay = ((40 * r) + ((h-40)*0.5))
else:
    pay = h * r
print(pay)
