"""
Platform = Hackerrank
Language = Python
Subdomain = Basic data types
Problem = Nested lists

"""

#Print the name(s) of any student(s) with the second lowest grade. order names alphabetically and print each on a new line



if __name__ == '__main__':
    students = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append([name, score])

    unique_scores = sorted(list(set([s[1] for s in students])))
    second_lowest_score = unique_scores[1]

    result_names = [s[0] for s in students if s[1] == second_lowest_score]

    result_names.sort()
    for name in result_names:
        print(name)


