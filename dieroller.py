import random

while True:
    choice=input("do you want to roll the dice?(y/n): ").lower()
    if choice=='y':
        num_dice=int(input('how many dice do you wan to roll? '))
        num_roll=int(input("how many times do you want to roll dice? "))
        for i in range(num_roll):
            results=[random.randint(1,6) for i in range(num_dice)]
            print(f'Roll {i+1}:{results}')
    elif choice=='n':
        print("Thanks for playing")
        break
    else:
        print('invalid choice')