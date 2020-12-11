#My first python program...again
#This program says hello and asks for your name!

print('Hello Friend!') 
myName = str.lower(input('What is your name?'))  #ask for user's name
if myName == 'liz':
    print('Oh my hot mama!')
else:
    print('It is nice to meet you,', myName) 
print('The length of your name is', str(len(myName)), 'characters long!')
myAge = int(input('What is your age? '))  #ask for user's age
if myAge >= 99:
    print("Man, you're old as hell!\nCongrats!")
elif myAge == 100
    print('You are 100. Awesome')
elif myAge > 100
    print('You have to be a vampire or something')
else:
    age50 = 50 - myAge
    print('In', str(int(age50)), 'years you will be 50!')