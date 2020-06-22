input_str = input("Enter a text or paragraph")
search_str = input("Enter the word to search")


def count_word(statement):
    count = 0
    for i in range(len(statement)-1):
        if statement[i:i+len(search_str)] == search_str:
            count = count+1
    return count


final_count = count_word(input_str)
print(final_count)

