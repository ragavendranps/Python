input_str = "Emma is developer. Emma is a writer"
search_str = "Emma"

#Search for the string in input and display the count

count1 = input_str.count(search_str)

#Other method

def count_words(statement):
    print("Given string is ", statement)
    count_2 = 0
    for i in range(len(statement)-1):
        if statement[i:i+4] == search_str:
            count_2=count_2+1
        #count_2 += statement[i:i+4] == search_str
    return count_2

count = count_words(input_str)

print(count)