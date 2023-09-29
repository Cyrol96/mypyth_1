#1 
subjects = ["physics", "calculus", "poetry", "history"]

#2
grades = [98, 97, 85, 88]

#3
gradebook = [
    [subjects[0], grades[0]],
    [subjects[1], grades[1]],
    [subjects[2], grades[2]],
    [subjects[3], grades[3]]
]

#4
print(gradebook)

#5
gradebook.append(["computer science", 100])
print(gradebook)

#6
gradebook.append(["visual arts", 93])
print(gradebook)

#7
gradebook[-1][-1] +=5
print(gradebook)

#8
gradebook[2].remove(85)
print(gradebook)

#9
gradebook[2].append("Pass")
print(gradebook)

# 10

last_semester_gradebook = [["politics", 80], ["latin", 96], ["dance", 97],  ["architecture", 65]]

full_gradebook = last_semester_gradebook + gradebook

print(full_gradebook)