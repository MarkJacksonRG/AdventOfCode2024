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

split_lines = get_split_input_lines("test.txt")
list1, list2 = split_lines_to_two_lists(split_lines)

def get_num_occurrences(some_list):
    num_occurrences = {}
    for item in some_list:
        if item in num_occurrences:
            num_occurrences[item] += 1
        else:
            num_occurrences[item] = 1
    return num_occurrences

num_occurrences2 = (get_num_occurrences(list2))

similarity_score = 0
for next in list1:
    similarity_score += int(next) * num_occurrences2.get(next, 0)
print(f"SIMILARITY = {similarity_score}")
