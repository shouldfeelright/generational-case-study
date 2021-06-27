# Import libraries
import pandas as pd
import numpy as np
import seaborn as sn
import matplotlib.pyplot as plt

# Define data set (% out of max score for each phys. social skill)
# First line Baby Boomers, last line Gen Z
data = [[.81, .91, .56,],
        [.62, 1, .66],
        [.7, .8, .55],
        [.66, .95, .64]]

# Define axis labels
generations = ['Baby Boomers', 'Gen X', 'Millennials', 'Gen Z']
soc_skills = ['Directness','Empathy', 'Mean. Discussion']

# Define data frame
df = pd.DataFrame(data)

# Define heatmap using correlation matrix data
vis = sn.heatmap(
    df,
    annot=True,
    vmin=.5, vmax=1, center=.75,
    cmap="Blues",
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
vis.set_title('% Out of Max Score (Phys. Soc. Skills)')

plt.show()