# Created by Chris Vinciguerra
# Creates a variable regression calculator with a graph showing percentage of US population with diabetes 1958-2030
import csv

import numpy
from matplotlib import pyplot as p

# Degree for regression. Note a degree above 2 may overfit for this data
degree = 2

years = []
percents = []
numbers = []
# Open data from csv file
with open("diabetes_data.csv") as file:
    reader = csv.reader(file)
    for row in reader:
        (year, percent, number) = row
        years.append(int(year))
        percents.append(float(percent))
        numbers.append(float(number))
# Create quadratic regression
coefficients = numpy.polynomial.polynomial.polyfit(years, percents, degree)
regression = [sum([coefficients[i] * pow(x, i)
                   for i in range(len(coefficients))]) for x in range(1958, 2031)]
# Create graph
p.title("Percentage of US population with diabetes\n1958-2030")
p.xlabel("Year")
p.ylabel("Percentage with diabetes")
p.plot(years, percents)
p.plot(range(1958, 2031), regression, "--k")
p.show()
