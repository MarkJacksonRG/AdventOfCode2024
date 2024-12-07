import re

test = "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"

# Find all the matches of the pattern in the test string and print them
# and the two numbers inside the brackets (i.e. the groups)
matches = re.findall(r"mul\([0-9]+,[0-9]+\)", test)
# matches = re.findall(r"mul", test) # xmul\([0-9]+,[0-9]+\)
mul = []
for match in matches:
    numbers = re.findall(r"[0-9]+", match)
    print(match, numbers)
    mul.append((int(numbers[0]), int(numbers[1])))

assert mul[0] == (2, 4)
assert mul[1] == (5, 5)
assert mul[2] == (11, 8)
assert mul[3] == (8, 5)
