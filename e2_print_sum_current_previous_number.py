print("Printing current and previous number sum in a range(10)")
start_num = 0
for i in range(0, 10):
    current_num = i
    previous_num = i-1
    if previous_num < 0:
        previous_num = 0
    sum = i + previous_num
    print("Current Number ", current_num, "Previous Number", previous_num, "Sum: ", sum)