"""
Write a program to return the correct letter grade
"""
from tkinter import messagebox, simpledialog, Tk

# The teacher wants you to write a program that converts the score on 2
# 100 point tests to a letter grade. The teacher wants you to average the
# score from the 2 tests and print out the letter grade back to the user.
# The letter grades are assigned as follows:
#   A = 89.5 to 100
#   B = 79.5 to less than 89.5
#   C = 69.5 to less than 79.5
#   D = 59.5 to less than 69.5
#   F = less than 59.5
if __name__ == '__main__':
    window = Tk()
    window.withdraw()
    # TODO) Ask the user for their score on the FIRST test and store their
    #  score in a variable
    T1 = simpledialog.askinteger(None, prompt="1st Test Score")
    # TODO) Ask the user for their score on the SECOND test and store their
    #  score in a variable
    T2 = simpledialog.askinteger(None, prompt="2nd Test Score")
    # TODO) Take the average score of both tests (total score / 2)
    sum = T1 + T2
    ave = sum/2
    if ave > 100:
        print("Don't lie.")
    elif ave >= 89.5:
        print("Good job!")
    elif ave >= 79.5:
        print("Average.")
    elif ave >= 69.5:
        print("You passed, but try harder next time.")
    elif ave >= 59.5:
        print("You barely passed.")
    elif ave <59.5:
        print("You failed.")
    # TODO) Use if statements to check the average score and print the
    #  corresponding letter grade back to the user. Also, give a different
    #  message according to their grade. Example, for an 'A' grade:
    #  "Wow! You must have studied really hard for those tests!"
    pass
