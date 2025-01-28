


with open("A", "r") as f:
    vals = f.readlines()

for i in range(len(vals)):
    vals[i] = int(vals[i].strip())


print("Max: ", max(vals))
print("Min: ", min(vals))

print("Average: ", sum(vals)/len(vals))