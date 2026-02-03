"""
Platform: Hackerrank
Language: Python
Subdomain: Basic Data Types
Problem: Finding the average of students marks and printing the output in 2 decimal places

"""


if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    
    marks = student_marks[query_name]
    average = sum(marks)/len(marks)
   
    print(f"{average:.2f}")