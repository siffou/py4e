fname = input("Enter file name: ")
fh = open(fname)
lst = list()

for line in fh:
    sline = line.split()
    for word in sline :
        if word in lst :
            continue
        else :
            lst.append(word)
lst.sort()
print(lst)
