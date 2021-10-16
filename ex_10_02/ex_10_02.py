file_name = input("Enter file:")
if len(file_name) < 1 :
    file_name = "mbox-short.txt"
file_handle = open(file_name)

counts = dict()

for line in file_handle:
    line = line.rstrip()
    if not line.startswith("From "):
        continue
    elif line.startswith("From "):
        line = line.split()
        hour = line[5]
        hour = hour.split(":")
        hour = hour[0]
        #can also be written in one line:
        #hour = line.split()[5].split(':')[0]
        counts[hour] = counts.get(hour, 0) + 1

for k, v in sorted(counts.items()):
    print(k, v)
