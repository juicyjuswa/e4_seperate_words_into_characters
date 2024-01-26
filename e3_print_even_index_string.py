
user_input = (input("Original String is "))
user_input_1 = len(user_input)
print("Printing only even index chars")

for i in range(0, user_input_1, 2):
    print(user_input[i])