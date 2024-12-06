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

split_lines = get_split_input_lines("input.txt")

for line in split_lines:
    print(f"{line[0]} ---- {line[1]}")

print(len(split_lines))


