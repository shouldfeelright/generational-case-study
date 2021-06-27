import numpy as np
import matplotlib.pyplot as plt

# Define data set (answers given to Idiom Comprehension int. soc. skill question)
# [0] = Baby Boomer, [1] = Gen X, [2] = Millennials, [3] = Gen Z
ans_cor = np.array((7, 6, 16, 18))
ans_inc = np.array((10, 13, 5, 3))
ans_idk = np.array((7, 5, 3, 3))

# Define x-axis categories
generations = ['Baby Boomers', 'Gen X', 'Millennials', 'Gen Z']

# Define graph parameters
N = 4
ind = np.arange(N)    # the x locations for the groups
width = 0.35       # the width of the bars: can also be len(x) sequence

# Define bars
b1 = plt.bar(ind, ans_cor, width, color="g",
             label="Correct", bottom=0)
b2 = plt.bar(ind, ans_inc, width, color="crimson",
             label="Incorrect", bottom=ans_cor)
b3 = plt.bar(ind, ans_idk, width, color="b",
             label="IDK", bottom=ans_cor+ans_inc)

# Set graph title and axis labels
plt.title("Answers to 'Idiom Comprehension' Questions by Generation")
plt.ylabel("# of People")
plt.xlabel("Generations")

# Position bars
plt.xticks(ind, generations)
plt.yticks(np.arange(0, 25, 2))

# Define graph legend
plt.legend((b1[0], b2[0], b3[0]), ("Correct", "Incorrect", "I Don't Know"))

# Annotate every bar with the amount that it corresponds to
for r1, r2, r3 in zip(b1, b2, b3):

    h1 = r1.get_height()
    h2 = r2.get_height()
    h3 = r3.get_height()

    plt.text(r1.get_x() + r1.get_width() / 3, h1 / 3, "%d" % h1,
            ha="left", va="center", color="white", fontsize=12,
            fontweight="bold")

    plt.text(r2.get_x() + r2.get_width() / 3, h1 + h2 / 3, "%d" % h2,
             ha="left", va="center", color="white", fontsize=12,
             fontweight="bold")

    plt.text(r3.get_x() + r3.get_width() / 3, h1 + h2 + h3 / 3, "%d" % h3,
             ha="left", va="center", color="white", fontsize=12,
            fontweight="bold")

# Add grid to bar chart
axes = plt.gca()
axes.yaxis.grid(linestyle='-', linewidth='0.5', color='lightgrey')

plt.show()