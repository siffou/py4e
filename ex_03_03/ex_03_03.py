score = input("Enter Score between 0.0 and 1.0: ")
fscore = float(score)

if fscore > 1.0 or fscore <= 0.0 :
    print ("You're grade is out of scope")
elif fscore == 0.9 :
    print ("A")
elif fscore == 0.8 :
    print ("B")
elif fscore == 0.7 :
    print ("C")
elif fscore == 0.6 :
    print ("D")
else :
    print ("It's not even a grade")
