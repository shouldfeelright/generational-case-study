import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Set seaborn options
sns.set(style="whitegrid", color_codes=True)

# Define data set (% out of max score for each phys. social skill)
# First line Baby Boomers, last line Gen Z
data = [[.81, .91, .56],
        [.62, 1, .66],
        [.7, .8, .55],
        [.66, .95, .64]]

# Define dataframe
df = pd.DataFrame({'Generations': ['Baby Boomers', 'Gen X', 'Millennials', 'Gen Z'],
                   '% of Max Achievable Score': [.56, .66, .55, .64]})

# Define graph legend
data_mng = [.56, .66, .55, .64]
df["Percentages"] = df["Generations"].map(dict(zip(range(1, 5), data_mng)))

# Define color options
pal = sns.color_palette("GnBu_d", len(data_mng))

# Define bar graph
vis = sns.barplot(
    data=df,
    x='Generations',
    y='% of Max Achievable Score',
    palette=np.array(pal[::1]))

# Use newly created dataframe column as legends colors
leg = sns.barplot(data=df, x='Generations', estimator=len, y='% of Max Achievable Score',
                 hue='Percentages', hue_order=data_mng, palette="GnBu_d")

# Set graph title
plt.title("% of Max Achievable 'Meaningful Discussion' Score by Generation")

# Set y-axis max to 1
plt.ylim(0, 1)

plt.show()
