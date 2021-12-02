#Information gathered from https://pubmed.ncbi.nlm.nih.gov/23711262/
import numpy
from matplotlib import pyplot as p

x_labels = ["Length of stay", "Marginal Surgery Cost", "Mortality rate"]
y_labels = ["Days", "Dollars", "Percent"]
conventional = [6.1, 34537, .48]
robotic = [4.9, 30540, .097]
y_max = [10, 40000, 1]


fig, ax = p.subplots(3)
ax[0].set_title("Conventional vs Robotic General Surgery")
for i in range(len(ax)):
    ax[i].bar(0, conventional[i], .5, label="Conventional Sugery")
    ax[i].bar(.5, robotic[i], .5, label="Robotic Surgery")
    ax[i].set_ylim(0, y_max[i])

    ax[i].set_xlabel(x_labels[i])
    ax[i].set_ylabel(y_labels[i])
    ax[i].set_xticklabels([])
ax[0].legend(prop={"size": 8})

fig.tight_layout()
p.show()
