import os

myFile = open('./myFile.txt', 'a')

newLine = input('What do you want to add to this file?') #add new line to file

myFile.write(f'{newLine}\n')

myFile.close()

myFile = open('./myFile.txt')

myFileContent = myFile.readlines()

print(f'{myFileContent}')

print(f'{myFileContent[2]}')