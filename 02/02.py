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

def is_line_safe(line):
    increasing = line[0] < line[1]
    for i in range(len(line)-1):
        a, b = line[i], line[i + 1]
        if a == b:
            return False
        if abs(a - b) > 3:
            return False
        if increasing and (a > b):
            return False
        if not increasing and (a < b):
            return False

    return True

# Tests
split_lines = get_split_input_lines("test.txt")
assert len(split_lines) == 6
for line in split_lines:
    assert len(line)==5
    print(line)

assert is_line_safe(split_lines[0]) == True
assert is_line_safe(split_lines[1]) == False
assert is_line_safe(split_lines[2]) == False
assert is_line_safe(split_lines[3]) == False
assert is_line_safe(split_lines[4]) == False
assert is_line_safe(split_lines[5]) == True
