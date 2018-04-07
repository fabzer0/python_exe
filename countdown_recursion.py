def countdown(number):
    if number == 0:
        print('completed')

    else:
        print(number)
        countdown(number-1)

countdown(20)
