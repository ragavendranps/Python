number = input("Enter a number : ")
revers = number[len(number)::-1]
if number == revers:
    print("True")
else:
    print("False")