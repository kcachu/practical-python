# mortgage.py
#
# Exercise 1.7

principal = 500_000.0
rate = 0.05
payment =  2684.11
extra_payment_start_month =int(input('extra_payment_start_month = '))
extra_payment_end_month =int(input('extra_payment_end_month = '))
extra_payment = int(input('Extra payment of = '))
total_paid = 0.0
month = 0

while principal > 0:

   if principal < payment:
       payment = principal * (1+rate/12) #could use a walrus but i won't

   principal = principal * (1+rate/12) - payment
   total_paid = total_paid + payment
   month += 1

   if month >= extra_payment_start_month and month <= extra_payment_end_month:
       principal -= extra_payment
       total_paid += extra_payment


   print(f'{month} {total_paid:02f} {principal:02f}') 

print(f'Total paid: {total_paid:02f} over {month} months')
