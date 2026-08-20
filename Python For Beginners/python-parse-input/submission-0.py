from typing import List

def read_integers() -> List[int]:
    line_integers = input()
    string_integers = line_integers.split(",")
    int_list = []

    for s in string_integers:
        int_list.append(int(s))

    return int_list
# do not modify the code below
print(read_integers())
print(read_integers())
print(read_integers())
