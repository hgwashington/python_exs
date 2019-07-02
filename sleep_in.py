day = int(input('Day (0-6)? '))

if day == 0:
    print("Its Sunday")
elif day == 1:
        print("Its Monday")
elif day == 2:
        print("Its Tuesday")
elif day == 3:
        print("Its Wednesday")
elif day == 4:
        print("Its Thursday")
elif day == 5:
        print("Its Friday")
elif day == 6:
        print("Its Saturday")
else:
        print("USER ERROR: INVALID INPUT")

if day == 6 or day == 0:
    print('sleep in')
else:
    print('go to work')