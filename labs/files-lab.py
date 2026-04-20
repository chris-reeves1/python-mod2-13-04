import csv

companies = []
sales = []

with open("output.csv") as csvfile:
    reader = csv.reader(csvfile)
    next(reader)
    for row in reader:
       companies.append(row[0])
       sales.append([int(x.replace(",", "" )) for x in row[1: ]])

total_monthly_sales = [sum(x) for x in zip(*sales)]
print(total_monthly_sales)

yearly_sales = {}

for item in range(len(companies)):
    yearly_sales[companies[item]] = sum(sales[item])

for k, v in yearly_sales.items():
    print(k, v)