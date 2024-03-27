from csv import reader
from re import findall


class Test:
    def __init__(self, full_name: str, mark: float, time_spent: str):
        self.full_name = full_name
        self.mark = mark

        try:
            matches = findall(r'\d+', time_spent)
            time_spent = (int(matches[0]), int(matches[1]))
            self.time_spent = time_spent
        except:
            self.time_spent = ()

    def __str__(self):
        return f'{self.full_name}; {self.mark}; {self.time_spent}'


tests = []


with open('12 - 1.csv', 'r', newline='', encoding='utf-8') as csvf:
    csvr = [row for row in reader(csvf)][1:]
    for row in csvr:
        test = Test(' '.join([row[0], row[1]]), float(row[9].replace(',', '.')), row[8])
        tests.append(test)

tests = filter(lambda test: test.mark >= 6 and test.time_spent, tests)
tests = sorted(tests, key=lambda test: test.full_name)

for test in tests:
    print(test)
