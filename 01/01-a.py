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
        line = line.split("   ")
        assert len(line) == 2
        # Check the entries are numbers
        assert line[0].isdigit()
        assert line[1].isdigit()

        split_lines.append(line)
    return split_lines

def split_lines_to_two_lists(split_lines):
    list1 = []
    list2 = []
    for line in split_lines:
        list1.append(line[0])
        list2.append(line[1])
    return list1, list2

def calculate_difference(sorted_pairs):
    sum_diffs = 0
    for pair in sorted_pairs:
        diff = abs(int(pair[0]) - abs(int(pair[1])))
        sum_diffs += diff
    return sum_diffs

real_split_lines = get_split_input_lines("input.txt")
real_list1, real_list2 = split_lines_to_two_lists(real_split_lines)

real_sorted_pairs = list(zip(sorted(real_list1), sorted(real_list2)))

print()
print("About to calc")
difference = calculate_difference(real_sorted_pairs)
assert difference == 1660292
print (f"DIFFERENCE={difference}")




