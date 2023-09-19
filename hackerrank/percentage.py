n = int(input())
student_marks = {}
for _ in range(n):
    name, *line = input().split()
    scores = list(map(float, line))
    student_marks[name] = scores
query_name = input()
  # Input the name of the student you want to query

if query_name in student_marks:
    scores = student_marks[query_name]
    percentage = sum(scores) / len(scores)
    print(f"{percentage:.2f}")  # Format the output to two decimal places
else:
    print(f"Student {query_name} not found.")
