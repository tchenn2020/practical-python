# mortgage.py
#
# Exercise 1.7

principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
month = 1
extra_payment_start_month = 61
extra_payment_end_month = 108
extra_payment = 1000

while principal > 0:
    if extra_payment_start_month <= month <= extra_payment_end_month:
        if principal < (payment + extra_payment):
            total_paid += principal
            principal = 0
            print(f'{month} ${total_paid} ${principal}')
            break
        else:
            principal = principal * (1 + rate / 12) - payment - extra_payment
            total_paid = total_paid + payment + extra_payment
            print(f'{month} ${total_paid} ${principal}')
            month += 1
    else:
        if principal < payment:
            total_paid += principal
            principal = 0
            print(f'{month} ${total_paid} ${principal}')
            break
        else:
            principal = principal * (1 + rate / 12) - payment
            total_paid = total_paid + payment
            print(f'{month} ${total_paid} ${principal}')
            month += 1

print('Total paid', total_paid)
print('Months', month)
