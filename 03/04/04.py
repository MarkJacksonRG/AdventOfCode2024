# test.txt
# XMAX occurs 18 times

def get_input_lines(filename):
    with open(filename, "r") as file:
        lines = file.read()

    # split into separate lines
    return lines.split("\n")

test_lines = get_input_lines("03/04/test.txt")
assert len(test_lines) == 10
