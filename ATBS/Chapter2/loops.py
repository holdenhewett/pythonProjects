loopYes = 1

while loopYes != 0:
    loopType = input('Enter the number of the desired loop\n1 - for\n2 - while\n')

    if loopType == 1:
        for i in range(5, 25, 5):
            print(i)
        loopYes = 0
    elif loopType == 2:
        data = 0
        while data < 5:
            print('The data is ', data)
            data = data + 1
        loopYes = 0
    else:
        print("You didn't enter a valid option.\nPlease try again.")
        loopYes = 1
    