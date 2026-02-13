hours = int(input())
rate = float(input())

if hours <= 40:
    pay = hours * rate
    print(pay)
else:
    overtime_hours = hours - 40
    pay = (40 * rate) + (overtime_hours * rate * 1.5)
    print(pay)
