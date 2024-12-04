def check_report(report, tolerate_level=0):
    if tolerate_level < 0:
        return False

    if report[0] == report[1]:
        return check_report(report[1:], tolerate_level - 1)

    increasing = None
    i = 0
    while i < len(report) - 1:
        reporti = report[i]
        if increasing is None:
            increasing = report[i] < report[i + 1]

        if increasing:
            if 3 >= report[i + 1] - report[i] > 0:
                i += 1
                continue
        else:
            if 3 >= report[i] - report[i + 1] > 0:
                i += 1
                continue

        if i == len(report) - 2 and tolerate_level > 0:
            return True

        tolerate_level -= 1
        if tolerate_level < 0:
            return False

        if i == 0 or i == 1:
            if check_report(report[1:], tolerate_level) or check_report([report[0]] + report[2:], tolerate_level):
                return True

        if increasing:
            if 3 >= report[i + 2] - report[i] > 0:
                i += 2
                continue
            if 3 >= report[i + 1] - report[i - 1] > 0:
                i += 1
                continue
        else:
            if 3 >= report[i] - report[i + 2] > 0:
                i += 2
                continue
            if 3 >= report[i - 1] - report[i + 1] > 0:
                i += 1
                continue
        return False
    return True


with open('input.txt', 'r') as file:
    summ = 0

    for line in file:
        report = [int(x) for x in line.strip().split()]
        if check_report(report):
            summ += 1

    print(f'1. There are "{summ}" safe reports.')


with open('input.txt', 'r') as file:
    summ = 0
    for line in file:
        report = [int(x) for x in line.strip().split()]
        if check_report(report, 1):
            summ += 1

    print(f'2. There are "{summ}" safe reports.')
