#My first python program...again
#This program says hello and asks for your name!

print('Hello Friend!') 
myName = str.lower(input('What is your name?'))  #ask for user's name
if myName == 'liz':
    print('Oh my hot mama!')
else:
    print('It is nice to meet you,', myName)
print('The length of your name is', str(len(myName)), 'characters long!')
myAge = int(input('What is your age? '))
if myAge > 50:
    print("Man, you're old as hell!\nCongrats!")
else:
    age50 = 50 - myAge
    print('In', str(int(age50)), 'years you will be 50!')