test = "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"

# .*xmul\([0-9]+,[0-9]+\).*

import re

# Find all the matches of the pattern in the test string and print them
# and the two numbers inside the brackets (i.e. the groups)
matches = re.findall(r"xmul\([0-9]+,[0-9]+\)", test)
print(len(matches))
for match in matches:
    numbers = re.findall(r"[0-9]+", match)
    print(match, numbers)

