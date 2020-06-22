data = input('Enter a name : ')
num = int(input('Enter a number : '))
#Rakesh (4) sh

def data_input():
    if num <= len(data):
        print(data[num:])
    else:
        print('The number mentioned is greater than the character count')

data_input()


