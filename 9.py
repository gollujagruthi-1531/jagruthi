score1 = input("ENTER FIRST EXAM SCORE (0-100):")
score2 = input("ENTER SECOND EXAM SCORE(0-100):")
score1 = int(score1)
score2 = int(score2)
if score1 >= 50 and score2 >= 50:
    print("YOUR PASSED!")
else:
    print("YOU NEED TO RETAKE SOME EXAMS")
