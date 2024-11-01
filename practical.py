
grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
students_sort = sorted(students)

def calculate_average(grades, students_sort):
    averages = {}
    for i in range(len(grades)):
        total = sum(grades[i])
        average = total / len(grades[i])
        averages[students_sort[i]] = average
    return averages

averages = calculate_average(grades, students_sort)
print(averages)

for students_sort, average in averages.items():
    print(f'{students_sort}: {average}')


