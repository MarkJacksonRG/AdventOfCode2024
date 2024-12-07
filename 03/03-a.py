import re

def get_input_lines(filename):
    with open(filename, "r") as file:
        lines = file.read()
    return lines

test = "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"

def get_mul(s):
    # Find all the matches of the pattern in the test string and print them
    # and the two numbers inside the brackets (i.e. the groups)
    matches = re.findall(r"mul\([0-9]+,[0-9]+\)", s)
    # matches = re.findall(r"mul", test) # xmul\([0-9]+,[0-9]+\)
    to_return = []
    for match in matches:
        numbers = re.findall(r"[0-9]+", match)
        print(match, numbers)
        to_return.append((int(numbers[0]), int(numbers[1])))
    return to_return

def sum_of_products(input):
    return sum([x*y for x, y in input])

test_mul = get_mul(test)

assert test_mul[0] == (2, 4)
assert test_mul[1] == (5, 5)
assert test_mul[2] == (11, 8)
assert test_mul[3] == (8, 5)

assert sum_of_products(test_mul) == 161

real_lines = get_input_lines("input.txt")
print (real_lines)
real_mul = get_mul(real_lines)
print(len(real_mul))

answer = sum_of_products(real_mul)
print(f"ANSWER IS {answer}")

