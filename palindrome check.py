text=input('Enter and check if your input is a palindrome or not: ')
ltext=text.lower()
rtext="".join((reversed(ltext)))
if rtext==ltext:
    print('Your input is a palindrome.')
else:
    print('Your input is not a palindrome.')