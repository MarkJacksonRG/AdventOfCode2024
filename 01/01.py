# open the file input.txt and read the content
# and print the content of the file
# if the file does not exist, print "File not found"

with open("input.txt", "r") as file:
    lines = file.read()

    # split into separate lines
    lines = lines.split("\n")

    for line in lines:
        print(line)
    print (len(lines))



