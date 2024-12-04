with open('input.txt', 'r') as file:
    column1 = []
    column2 = []

    for line in file:
        numbers = line.strip().split()
        column1.append(int(numbers[0]))
        column2.append(int(numbers[1]))

        column1.sort()
        column2.sort()

    summ = sum([abs(a - b) for a, b in zip(column1, column2)])

    print(f'1. Total distance between the left list and the right list - {summ}')


from collections import Counter

with open('input.txt', 'r') as file:
    column1 = []
    column2 = []

    for line in file:
        numbers = line.strip().split()
        column1.append(int(numbers[0]))
        column2.append(int(numbers[1]))

        column2_counter = Counter(column2)

    summ = sum([a * column2_counter[a] for a in column1])

    print(f'2. Their similarity score for both lists - {summ}')
