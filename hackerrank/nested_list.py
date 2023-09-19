student_data = []  # List to store student data (name, score)
scores = []  # List to store unique scores

for _ in range(int(input())):
    name = input()
    score = float(input())
    student_data.append([name, score])
    scores.append(score)

scores = list(set(scores))  # Remove duplicates and convert back to a list
scores.sort()

if len(scores) > 1:
    second_lowest = scores[1]
else:
    second_lowest = None

second_lowest_students = [se[0] for se in student_data if se[1] == second_lowest]

if second_lowest is not None:
    second_lowest_students.sort()

for name in second_lowest_students:
    print(name)




