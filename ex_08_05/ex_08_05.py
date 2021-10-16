fname = input('Enter file name: ')
fhand = open(fname)
count = 0

for line in fhand :
    line = line.rstrip()
    if not line.startswith('From ') :
        continue
    elif line.startswith('From ') :
        line = line.split()
        new_line = line[1]
        count = count + 1
        print(new_line)

print("There were", count, "lines in the file with From as the first word")
