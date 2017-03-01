import csv
import os.path


def readcsv(filename):
    f = open(filename, 'rt')
    try:
        reader = csv.reader(f)
        for row in reader:
            print(row)
    finally:
        f.close()

if __name__ == '__main__':
    readcsv('existingtest.csv')
    filename = 'newtest.csv'
    f = open(filename, 'w', newline='')   # newline doesn't work in python 2.7
    try:
        writer = csv.writer(f)   # instead of new line put lineterminator='\n' here
        writer.writerow(('date', 'miles', 'gallons'))
        for i in range(10):
            writer.writerow(('today', i + 100, (i / 2) + 3))
    finally:
        f.close()
    print('\n' + filename)
    readcsv(filename)
