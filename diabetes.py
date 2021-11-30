import numpy
from matplotlib import pyplot as pl
import csv

years = []
percents = []
numbers = []
with open("Data.csv") as file:
    reader = csv.reader(file)
    for row in reader:
        (year, percent, number) = row
        years.append(int(year))
        percents.append(float(percent))
        numbers.append(float(number))

z = numpy.polynomial.polynomial.polyfit(years, percents, 2)
regression = [z[2]*i**2 + z[1]*i + z[0] for i in range(1958, 2030)]

pl.title("Percentage of US population with diabetes\n1958-2030")
pl.xlabel("Year")
pl.ylabel("Percentage with diabetes")
pl.plot(years, percents)
pl.plot(range(1958, 2030), regression, "--k")
pl.show()