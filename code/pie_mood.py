import matplotlib.pyplot as plt

# Define category labels
labels = "Positive", "Negative", "Neutral"

# Define data (number of people per mood)
# [0] = Positive, [1] = Negative, [2] = Neutral
mood_data = [50, 4, 42]

# Define pie chart
colors = ['greenyellow', 'tomato', 'deepskyblue']
plt.pie(mood_data, colors=colors, startangle=90, autopct='%1.1f%%')
plt.title('Overall Mood of Focus Group')

# Define chart legend
plt.legend(labels, loc="best")

plt.show()