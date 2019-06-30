import csv

class SLCSP_Search(object):

    def __init__(self, zips, plans, sl):
        self.zips = zips

plans = csv.DictReader(open('plans.csv'))
zips = csv.DictReader(open('zips.csv'))
prices = csv.DictReader(open('slcsp.csv'))
search = {}

for row in plans:
    if row['metal_level'] == 'Silver':
        for i in zips:
            if i['rate_area'] == row['rate_area']:
                if i['zipcode'] not in search:
                    search[i['zipcode']] = [row['rate']]
                else:
                    search[i['zipcode']].append(row['rate'])


with open('zips.csv', mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        line_count += 1
    print(f'Processed {line_count} lines.')


with open('plans.csv', mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        line_count += 1
    print(f'Processed {line_count} lines.')
