#My first python program...again
#This program says hello and asks for your name and age then provides a funny response.

print('Hello Friend!') 
myName = str.lower(input('What is your name?'))  #ask for user's name
if myName == 'liz':
    print('Oh my hot mama!')
else:
    print('It is nice to meet you,', myName) 
print('The length of your name is', str(len(myName)), 'characters long!')
myAge = int(input('What is your age? '))  #ask for user's age
if myAge <= 99:
    age50 = 50 - myAge
    print(f'In {age50} years you will be 50!')
elif myAge >= 100:
    print('You lived to be over 100! Awesome!')
elif myAge > 150:
    print('You have to be a vampire or something')