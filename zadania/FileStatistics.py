

with open("A", "r") as f:
    lines = f.readlines()

for i in range(len(lines)):
    lines[i] = (lines[i].strip())


print(lines)

print("Number of lines: ", len(lines))

now = 0 # number of words
for line in lines:
    splitline = line.split(" ")
    for word in splitline:
        now += 1

noc = 0 # number of chars
for line in lines:
    noc += len(line)

print("Number of words: ", now)
print("Number of characters: ", noc)


