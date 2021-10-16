largest = None
smallest = None

while True:
    num = input('Enter a number: ')
    if num == "done":
        break
    try:
        fval = float(num)
    except:
        print('Invalid input')
        continue

        if smallest is None :
            smallest = fval
        elif fval < smallest :
            smallest = fval
        #print(smallest, mini_value)

        if largest is None :
        elif fval > largest :
            largest = fval
        #print(largest, big_value)
    #print(fval)

print("Maximum is", largest)
print("Minimum is", smallest)
