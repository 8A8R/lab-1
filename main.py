import csv

with open('books-en.csv') as csvfile:
    table = csv.reader(csvfile, delimiter=';')
    counter = 0
    counter_greater_30 = 0
    counter_years = 0
    i = 0

    for row in table:
        if i == 0:
            i += 1
            continue
        i += 1
        counter += 1
        if len(row[1]) <= 30:
            counter_greater_30 += 1
        if 2016 <= int(row[3]) <= 2018:
            counter_years += 1


# Question 1
    print(f'The number of entries in the file is {counter}')
# Question 2
    print(f'The number of entries with Name greater than 30 is {counter_greater_30}')
# Question 3
print(f'The number of entries with year between 2016 and 2018 is {counter_years}')
