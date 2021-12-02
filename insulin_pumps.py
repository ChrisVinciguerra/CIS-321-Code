# Created by Chris Vinciguerra
# Creates bar graphs representing the benefits of insulin pumps over manual injection methods
# Data collected from https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4911840/
import numpy
from matplotlib import pyplot as p

x_labels = ["Physical Health Total", "Mental Health Total"]
pump_mean = [92.6, 88.59]
pump_error = [8.87, 6.26]

no_pump_mean = [56.72, 22.55]
no_pump_error = [22.55, 18.14]

fig, ax = p.subplots(2)
ax[0].set_title("Insulin Pump's Effect on Mental and Physical Well Being")
ax[0].bar(0, pump_mean[0], 1,
          yerr=pump_error[0], capsize=10, label="Insulin Pump")
ax[0].bar(1, no_pump_mean[0], 1,
          yerr=no_pump_error[0], capsize=10, label="No Insulin Pump")
ax[0].set_xlabel(x_labels[0])
ax[0].set_ylabel("Score (Relative units)")
ax[0].set_xticklabels([])
ax[0].legend(prop={"size": 8})

ax[1].bar(0, pump_mean[1], 1,
          yerr=pump_error[1], capsize=10, label="Insulin Pump")
ax[1].bar(1, no_pump_mean[1], 1,
          yerr=no_pump_error[1], capsize=10, label="No Insulin Pump")
ax[1].set_xlabel(x_labels[1])
ax[1].set_ylabel("Score (Relative units)")
ax[1].set_xticklabels([])
ax[1].legend(prop={"size": 8})

fig.tight_layout()
p.show()
