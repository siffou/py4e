largest = None
smallest = None

while True :
    num = input('Enter a number: ')

    if num == "done" :
        break

    try:
        i_num = int(num)
    except:
        print('Invalid input')
        continue

    if largest is None :
        largest = i_num
    elif i_num > largest:
        largest = i_num
    #print(largest)

    if smallest is None :
        smallest = i_num
    elif i_num < smallest :
        smallest = i_num
    #print(smallest)

print("Maximum is", largest)
print("Minimum is", smallest)
