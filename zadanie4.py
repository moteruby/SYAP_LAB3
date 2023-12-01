with open('фирмы.txt', 'w', encoding='utf-8') as file:
    file.write('firm_1 ООО 10000 5000\n')
    file.write('firm_2 ЗАО 15000 8000\n')
    file.write('firm_3 ИП 8000 10000\n')
    file.write('firm_4 АО 20000 15000\n')

with open('фирмы.txt', 'r', encoding='utf-8') as file:
    firms_profit = {}
    total_profit = 0
    firms_count = 0
    for line in file:
        name, ownership, revenue, costs = line.split()
        profit = int(revenue) - int(costs)
        firms_profit[name] = profit
        if profit > 0:
            total_profit += profit
            firms_count += 1

    average_profit = total_profit / firms_count

    result_list = [firms_profit, {"average_profit": average_profit}]

import json
with open('фирмы.json', 'w', encoding='utf-8') as json_file:
    json.dump(result_list, json_file)
