import numpy
from matplotlib import pyplot as pl
import csv


outcomes = ["Length of stay", "Marginal Surgery Cost", "Mortality rate"]
conventional = [6.1, 34537, .48]
robotic = [4.9, 30540, .097]

outcomes = ["Marginal Surgery Cost"]
conventional = [34537]
robotic = [30540]

x = numpy.arange(len(outcomes))
width = .1

fig, ax = pl.subplots(3)
rects1 = ax[0].bar(x - width/2, conventional, width, label="Conventional Sugery")
rects2 = ax[0].bar(x + width/2, robotic, width, label="Robotic Surgery")

for chart in ax:
    chart.set_title("Conventional vs Robotic Surgery")
    chart.set_ylabel("Cost of surgery")
    chart.set_xlabel("")
    chart.set_xticklabels([])
    chart.legend()

fig.tight_layout()
pl.show()
