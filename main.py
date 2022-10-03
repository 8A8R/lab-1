import csv
import random


def findByAuthor():
    author = input('enter the name og an author:')
    with open('books-en.csv') as csvfile:
        table = csv.reader(csvfile, delimiter=';')

        i = 0
        results = []
        for row in table:
            if i == 0:
                i += 1
                continue
            i += 1

            if 2016 <= int(row[3]) <= 2018 and row[2] == author:
                results.append(row[1])

        if len(results) == 0:
            print(f'there is no books the auther name {author} and between 2016 and 2018')
        else:
            print(f'The number of entries with year between 2016 and 2018 with the name {author}is {results}')


def countRecords():
    with open('books-en.csv') as csvfile:
        table = csv.reader(csvfile, delimiter=';')
        counter = 0
        for row in table:
            counter += 1
        print(f'The number of entries in the file is {counter}')


def countRecordsMorethan30Let():
    with open('books-en.csv') as csvfile:
        table = csv.reader(csvfile, delimiter=';')

        counter_greater_30 = 0
        i = 0
        for row in table:
            if i == 0:
                i+=1
                continue
            if len(row[1]) <= 30:
                counter_greater_30 += 1
        print(f'The number of entries with Name greater than 30 is {counter_greater_30}')


def writeRandomBooks():
    with open('books-en.csv') as csvfile:
        table = csv.reader(csvfile, delimiter=';')
        list1 = list(table)
        randomValues = []

        for i in range(20):
            randomValues.insert(1, random.choice(list1))

        with open('random-values.txt', 'w') as randomBooks:
            i = 0
            for line in randomValues:
                i += 1
                randomBooks.write(str(i) + "-" + line[1] + " , " + line[2] + " - " + line[3] + "\n")


countRecordsMorethan30Let()
