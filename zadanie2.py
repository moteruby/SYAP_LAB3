with open('Государство.txt', 'r', encoding='utf-8') as file:
    for line in file:
        data = line.split()
        if int(data[2]) > 1000000:
            print(data[0])