#A python program to check for grades based on specific instructions
#CharlesTechy
score = float(input("Enter Score\n"))

if (score >= 0.9):
    grade = 'A'
    print("Grade is %s" %grade)

elif (score >= 0.8 and score <= 0.9):
    grade = 'B'
    print("Grade is %s" %grade)

elif (score >= 0.7 and score <= 0.8):
    grade = 'C'
    print("Grade is %s" %grade)

elif (score >= 0.6 and score <= 0.7):
    grade = 'D'
    print("Grade is %s" %grade)  

elif (score < 0.6):
    grade = 'F'
    print("Grade is %s" %grade)

else:
      print("Score Out of Range") 

        
#   Score                            Grade
#   >= 0.9                             A
#   >= 0.8 and < 0.9                   B
#   >= 0.7 and < 0.8                   C
#   >= 0.6 and < 0.7                   D
#   < 0.6                              F
