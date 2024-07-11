import random

def equal_split():
    people = int(input('Enter the number of friends joining (including you): '))
    if people <= 0:
        print('No one is joining for the party')
        return None
    else:
        print('Enter the name of every friend (including you), each on a new line: ')
        friends = []
        for i in range(people):
            friends.append(input())
        value = int(input("Enter the total bill value: "))
        each_bill = divise(value, people)
        to_pay = dict.fromkeys(friends, each_bill)
        name = lucky_one(friends)
        if name:
            new = divise(value, people-1)
            for key in to_pay:
                if key == name:
                    to_pay[key] = 0
                else:
                    to_pay[key] = new
        print(to_pay)
        return to_pay

def divise(bill, people):
    topay = bill / people
    decimal = str(topay - int(topay))[1:]
    if decimal == '.0':
        return int(topay)
    else:
        return round(topay, 2) 

def lucky_one(friends: list):
    print('Do you want to use the "Who is lucky?" feature? Write Yes/No:')
    answer = input()
    if answer not in ('Yes', 'No'):
        return None
    elif answer == 'Yes':
        name = random.choice(friends)
        print(f'{name} is the lucky one!')
        return name
    elif answer == 'No':
        print('No one is going to be lucky')

equal_split()