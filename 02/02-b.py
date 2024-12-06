# open the file input.txt and read the content
# and print the content of the file
# if the file does not exist, print "File not found"

def get_input_lines(filename):
    with open(filename, "r") as file:
        lines = file.read()

    # split into separate lines
    return lines.split("\n")


def get_split_input_lines(filename):
    lines = get_input_lines(filename)
    split_lines = []
    for line in lines:
        # Split by spaces
        line = line.split(" ")
        # Check the entries are numbers
        for entry in line:
            assert entry.isdigit()
        # Convert to integers
        line = [int(entry) for entry in line]

        split_lines.append(line)
    return split_lines

def find_problem_level(line):
    increasing = line[0] < line[1]
    for i in range(len(line)-1):
        a, b = line[i], line[i + 1]
        if a == b:
            return i+1
        if abs(a - b) > 3:
            return i+1
        if increasing and (a > b):
            return i+1
        if not increasing and (a < b):
            return i+1

    return None

def is_safe_report(line):
    problem_level = find_problem_level(line)
    if problem_level is None:
        return True
    without_problem_level = line[:problem_level] + line[problem_level+1:]
    return find_problem_level(without_problem_level) is None

# Tests
split_lines = get_split_input_lines("test.txt")
assert len(split_lines) == 6
for line in split_lines:
    assert len(line)==5
    print(line)

assert find_problem_level(split_lines[0]) is None
assert find_problem_level(split_lines[1]) == 2
assert find_problem_level(split_lines[2]) == 3
assert find_problem_level(split_lines[3]) == 2
assert find_problem_level(split_lines[4]) == 3
assert find_problem_level(split_lines[5]) is None

assert is_safe_report(split_lines[0]) == True
assert is_safe_report(split_lines[1]) == False
assert is_safe_report(split_lines[2]) == False
assert is_safe_report(split_lines[3]) == True
assert is_safe_report(split_lines[4]) == True
assert is_safe_report(split_lines[5]) == True

# # Actual
# split_lines = get_split_input_lines("input.txt")
# number = 0
# for line in split_lines:
#     if is_line_safe(line):
#         number+=1
# print(f"NUMBER OF SAFE REPORTS = {number}")
