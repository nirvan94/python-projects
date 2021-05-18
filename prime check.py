number=int(input('What is your number? '))
prime=True
for fac in range(2, number):
    if int(number)%fac==0 and not number==2:
        prime=False
if prime==True and not number<2:
    print('The number is prime.')
else:
    print('The number is not prime.')