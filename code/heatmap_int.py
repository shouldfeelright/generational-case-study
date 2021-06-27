# Import libraries
import pandas as pd
import numpy as np
import seaborn as sn
import matplotlib.pyplot as plt

# Define data set (% of questions correct for each int. social skill out of 24)
# First line Baby Boomers, last line Gen Z
data = [[.05, .3, .59,],
        [.05, .25, .63],
        [.25, .67, .92],
        [.55, .75, .75]]

# Define axis labels
generations = ['Baby Boomers', 'Gen X', 'Millennials', 'Gen Z']
soc_skills = ['Prec. Comm.','Idiom Comp.', 'Cult. Lit.']

# Define data frame
df = pd.DataFrame(data)

# Define heatmap using correlation matrix data
vis = sn.heatmap(
    df,
    annot=True,
    vmin=0, vmax=1, center=.5,
    cmap="BuPu",
    square=True,
    linewidths=.5,
    xticklabels=soc_skills,
    yticklabels=generations
    )

# Rotate heatmap's x-axis labels
vis.set_xticklabels(
    vis.get_xticklabels(),
    rotation=45,
    horizontalalignment='right'
    )

# Add title to heatmap
vis.set_title('% of Correct Identifications (Int. Soc. Skills)')

plt.show()