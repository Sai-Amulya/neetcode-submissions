def add_two_numbers() -> int:
    line_int = input()
    str_int = line_int.split(",")
    sum = 0 
    for i in str_int:
        sum += int(i)
    return sum


# do not modify below this line
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())
