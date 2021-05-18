import sys

narcissist=input('Check whether a number is armstrong or not(without commas): ')
if int(narcissist)<0:
    print("The program doesn't consider negative values as armstrong numbers.")
    exit()
digits=len(narcissist)
index=0
numsum=0
while index<digits:
    for dino in (narcissist[index]):
        #print(dino)
        numsum+=int(dino)**digits
        #print(numsum)
        index+=1
if numsum==int(narcissist):
    print('It is an armstrong number.')
else:
    print('It is not an armstrong number.')