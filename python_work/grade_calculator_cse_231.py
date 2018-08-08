exercise = float(input("Overall percentage for exercises: "))
project = float(input("Overall percentage for projects: "))
exam = float(input("What did you get on exam 1: "))

calculation = (exam * 0.20) + (project * 0.45) + (exercise * 0.10)

final_exam = 90 - calculation
print("You need to get: ",final_exam / 25," on the final exam")

#if calculation >= 90.0:
#    print("Congratulations! You got a 4.0!", calculation,"%")
#elif 85.0 <= calculation < 90.0:
#    print("Good job! You got a 3.5!", calculation,"%")
#elif 80.0 <= calculation < 85.0:
#    print("Nice work, you got a 3.0", calculation,"%")
#elif 75.0 <= calculation < 80.0:
#    print("You Tried! 2.5", calculation,"%")
#elif 70.0 <= calculation < 75.0:
#    print("You had all summer, what happened!? 2.0", calculation,"%")
#else:
#    print("yikes", calculation,"%")
#
#
