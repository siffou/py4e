fname = input("Enter file:")
fhand = open(fname)

counts = dict()
for line in fhand :
    line = line.rstrip()
    if not line.startswith("From "):
        continue
    elif line.startswith("From "):
        line = line.split()
        emails = line[1]
        emails = emails.split()
        #print(emails)
    for email in emails:
        counts[email] = counts.get(email,0) + 1

bigcount = None
bigword = None

for email,count in counts.items():
    if bigcount is None or count > bigcount:
        bigword = email
        bigcount = count

print(bigword, bigcount)
