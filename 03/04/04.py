# test.txt
# XMAS occurs 18 times

def get_input_lines(filename):
    with open(filename, "r") as file:
        lines = file.read()

    # split into separate lines
    return lines.split("\n")

test_lines = get_input_lines("03/04/test.txt")
assert len(test_lines) == 10

def xmas_or_dot(lines):
    to_return = []
    for l in lines:
        s = [c if c in "XMAS" else "." for c in l]
        to_return.append(s)
    return to_return

test_ret = xmas_or_dot(["ZXMASZ", "XMAS"])
print(test_ret)
assert test_ret[0] == list(".XMAS.")
assert test_ret[1] == list("XMAS")
