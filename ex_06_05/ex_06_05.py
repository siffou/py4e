#6.5 Write code using find() and string slicing
#(see section 6.10) to extract the number at the end
#of the line below. Convert the extracted value to a
#floating point number and print it out.

text = "X-DSPAM-Confidence:    0.8475"
length = len(text)
print(length)
numpos = text.find('0')
print(numpos)

last = text[length-1]
print(last)

print(text[23:90])
