print('-------------------------------')
print('      BIRTHDAY APP')
print('-------------------------------')
print()

def get_birthday_from_user():
    print('Tell us when you were born: ')
    year = int(input('Year [YYYY]'))
    month = int(input('Month [MM]'))
    day = int(input('Day [DD]'))

    birthday = datetime.datetime(year, month, day)
    return birthday
