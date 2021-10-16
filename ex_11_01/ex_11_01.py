import re
count = 0
sum = 0

hand = open('regex.txt')
for line in hand:
    line = line.rstrip()
    x = re.findall('[0-9]+', line)
    #if len(x) > 0:
        #print(x)
    for i in x:
        count = count + 1
        sum = sum + int(i)

print(count, sum)
