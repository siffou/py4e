# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
count = 0
countx = 0
try:
    fhand = open(fname)
except:
    print("file not found, ", fname)

for line in fh:
    line = line.rstrip()
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    elif line.startswith("X-DSPAM-Confidence:"):
        length = len(line)
        numpos = line.find('0')
        new_line = line[numpos:]
        fline = float(new_line)
        countx = countx + fline
        count = count + 1


    #print(line[numpos:], count)
print("Average spam confidence:", countx / count)
