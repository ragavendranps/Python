#within bracket the function - argument
def sum_of_numbers(sam):
    prenum = 0
    for num in range(sam):
        sum = prenum + num
        print("currentnum={} , previous num = {} , Sum = {}".format(num, prenum, sum))
        prenum = num

sample=int(input('Enter a number : '))
sum_of_numbers(sample)
