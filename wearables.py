# Created by Chris Vinciguerra
# Creates a variable regression calculator with a graph showing projections for wearable device market growth
import csv

import numpy
from matplotlib import pyplot as p

# Degree for regression. Note a degree above 2 may overfit for this data
degree = 2

years = []
shipments = []
# Open data from csv file
with open("wearables_data.csv") as file:
    reader = csv.reader(file)
    for row in reader:
        (year, units) = row
        years.append(int(year))
        shipments.append(float(units))
# Create quadratic regression
coefficients = numpy.polynomial.polynomial.polyfit(years, shipments, degree)
regression = [sum([coefficients[i] * pow(x, i)
                   for i in range(len(coefficients))]) for x in range(2014, 2026)]

# Create graph
p.title("Wearables unit shipments worldwide\n2014-2025")
p.xlabel("Year")
p.ylabel("Units shipped (Millions)")
p.plot(years, shipments)
p.plot(range(2014, 2026), regression, "--k")
p.show()
