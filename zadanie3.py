lessons_dict = {}

with open('учебные_предметы.txt', 'r', encoding='utf-8') as file:
    for line in file:
        subject, lessons = line.split(':')
        total_lessons = sum(int(x.split('(')[0]) for x in lessons.split() if '(' in x)
        lessons_dict[subject] = total_lessons

print(lessons_dict)
