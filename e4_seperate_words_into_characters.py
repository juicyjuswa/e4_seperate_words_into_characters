def remove_characters(user_input, n):
    return user_input[n:]


user_input = input("Original String is ")
n = int(input("n: "))
final_output = remove_characters(user_input, n)
print(final_output)

