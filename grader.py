thingsIDid = """
EXTRA CREDIT:
Final output table
student names
dictionary usage to store data
"""
print(thingsIDid)
print("Welcome to the grader!")
print("At the end, all the scores will be displayed for all of your students.")
maxPoints = int(input("What is the maximum amount of points? ")) # get max points
studentCount = int(input("How many students do you have? ")) # get number of students

studentScores = {}
for i in range(studentCount): # for each student
    name = input("What is the student's name? ") # get the name
    score = float(input("How many points did " + name + " earn? ")) # get the total points
    letter = ""
    percent = score/maxPoints*100
    if (percent < 51):
        letter = "F"
    elif (percent < 61):
        letter = "D"
    elif (percent < 76):
        letter = "C"
    elif (percent < 89):
        letter = "B"
    elif (percent >= 89):
        letter = "A"
    print(name, "earned a", letter + "!")# Tell them the score of the student
    studentScores[name] = letter # record to a dictionary

#-- when all done, print everything out

# get the column widths
namesWidth = 0
scoresWidth = 0
for i in range(len(studentScores)):
    namesWidth = max(namesWidth, len(list(studentScores.keys())[i]) + 1)
    scoresWidth = max(scoresWidth, len(str(studentScores[list(studentScores.keys())[i]])))

# Print
print()
print("Here are the final scores: ")
for i in range(len(studentScores)):
    print(str(list(studentScores.keys())[i]).ljust(namesWidth), str(studentScores.get(list(studentScores.keys())[i])).rjust(scoresWidth))