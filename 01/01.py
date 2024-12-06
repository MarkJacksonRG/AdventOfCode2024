# open the file input.txt and read the content
# and print the content of the file
# if the file does not exist, print "File not found"

def get_input_lines(filename):
    with open(filename, "r") as file:
        lines = file.read()

    # split into separate lines
    return lines.split("\n")


def get_split_input_lines(filename):
    global split_lines, line
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
        print(f"{pair[0]} ---- {pair[1]}")
        print(f"{abs(int(pair[0]))} ---- {abs(int(pair[1]))}")
        diff = abs(int(pair[0]) - abs(int(pair[1])))
        sum_diffs += diff
    return sum_diffs

split_lines = get_split_input_lines("test.txt")
list1, list2 = split_lines_to_two_lists(split_lines)
for pair in list(zip(list1, list2)):
    print(f"{pair[0]} ---- {pair[1]}")

print()
sorted1 = sorted(list1)
sorted2 = sorted(list2)
sorted_pairs = list(zip(sorted1, sorted2))
for pair in sorted_pairs:
    print(f"{pair[0]} ---- {pair[1]}")

print()
print("About to calc")
print (calculate_difference(sorted_pairs))

# for line in split_lines:
#     print(f"{line[0]} ---- {line[1]}")
#
# print(len(split_lines))



