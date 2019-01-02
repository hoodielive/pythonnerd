my_student = {
        'name': 'Cool dude',
        'grades': [70, 88, 90, 99]
}

def average_grade(student):
    return sum(student['grades']) / len(student['grades'])

print(average_grade(my_student))
