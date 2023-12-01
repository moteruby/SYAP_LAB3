# Задание 1
with open('F1.txt', 'w') as f1:
    while True:
        data = input("Введите данные для файла F1: ")
        if data == "":
            break
        f1.write(data + "\n")

N1 = int(input("Введите номер строки N1: "))
N2 = int(input("Введите номер строки N2: "))
with open('F1.txt', 'r') as f1, open('F2.txt', 'w') as f2:
    lines = f1.readlines()
    for i in range(N1-1, N2):
        if lines[i][0] == "A":
            f2.write(lines[i])

with open('F2.txt', 'r') as f2:
    first_line = f2.readline()
    word_count = len(first_line.split())
    print("Количество слов в первой строке файла F2:", word_count)
