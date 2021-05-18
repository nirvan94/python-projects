print('Please enter numerical values only. For months, January = 1, February = 2 and so on...')
year=input('Year? ')
month=input('Month? ')
if int(month)<4:
    print(2021-int(year))
elif int(month)==4:
    day=input('Day?')
    if int(day)<30:
        print(2021-int(year))
    else:
        print(2020-int(year))
else:
    print(2020-int(year))