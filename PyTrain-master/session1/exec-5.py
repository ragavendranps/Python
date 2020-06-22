# a = [1, 2, 3, 4, 5, 6]
#
# #return true if the first and last numbers are same
#
# if a[0] == a[5]:
#     print("True")
# else:
#     print("False")

######### Next approach
# creating an empty list
lst = []
# number of elemetns as input
n = int(input("Enter number of elements : "))

# iterating till the range
for i in range(0, n):
    ele = int(input())

    lst.append(ele)  # adding the element

if lst[0]==lst[n-1]:
    print("True")
else:
    print("False")


if lst[0]==lst[-1]:
    print("True")
else:
    print("False")
