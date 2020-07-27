# mortgage.py
#
# Exercise 1.7

principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
months = 0.0

extra_payment = 1000.0
extra_payment_start = 61
extra_payment_end = 108

while principal > 0:
    principal = principal * (1 + rate / 12) - payment
    total_paid = total_paid + payment
    months = months + 1

    if extra_payment_start <= months <= extra_payment_end:
        principal = principal - extra_payment
        total_paid = total_paid + extra_payment

    if principal <= 0:
        principal = 0

    print(round(months), round(total_paid, 2), round(principal, 2))

print('Total paid:', round(total_paid, 2), 'Months', round(months))
