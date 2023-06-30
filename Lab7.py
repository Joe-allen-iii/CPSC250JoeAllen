# Lab 7

# 30.8 LAB: Average exam scores (NumPy arrays basic)

# TODO: Import NumPy
import numpy as np


# TODO: Read two sets of exam scores of five students from user input
#       and store the scores into two NumPy arrays
exam1 = input().split()
exam2 = input().split()

exam1 = [float(i) for i in exam1]
exam2 = [float(i) for i in exam2]


exam1arr = np.array(exam1)
exam2arr = np.array(exam2)

# TODO: Compute the average scores for each of the five students

meanarr = (exam1arr + exam2arr) / 2


# TODO: Output "Average scores: " followed by the NumPy array of the average scores

print("Average scores:", meanarr)

# TODO: Count the number of average scores that are >= 80

abv80 = meanarr[meanarr >= 80]

c = len(abv80)

# TODO: Output "Number of students who received 80 and above: " followed by the count

print("Number of students who received 80 and above:", c)

# 30.10.1: LAB: Course grade statistics (pandas)
import pandas as pd

file_name = input()

# TODO: Read in file_name as a dataframe
data = pd.read_csv(file_name, delimiter='\t')
# TODO: Output rows by descending Final scores
sorted_data = data.sort_values(by='Final', ascending=False)
print(sorted_data)


max_scores = data.max(numeric_only=True).to_string()

print("\nMax Scores:")

print(max_scores)

# TODO: Output the max scores of each assignment
med_scores = data.median(numeric_only=True).to_string()
print("\nMedian Scores:")
print(med_scores)

# TODO: Output the median scores of each assignment
mean_scores = data.mean(numeric_only=True).to_string()

print("\nAverage Scores:")
print(mean_scores)

# TODO: Output the average scores of each assignment.
std_scores = data.std(numeric_only=True).to_string()
print("\nStandard Deviation:")
print(std_scores)
# TODO: Output the standard devation of each assignment.

# 30.11.1: LAB: Flight status (line plot)

import matplotlib.pyplot as plt
import pandas as pd

file = input()

# TODO: Read in the CSV file as a dataframe
data = pd.read_csv(file)


# TODO: Print the average of flight delays and flight cancellations

# Calculate the average flight delays and cancellations
avg_delayed = data['Delayed'].mean()
avg_cancelled = data['Cancelled'].mean()

# Output the average flight delays and cancellations
print(f"Average delays: {avg_delayed:.2f}")
print(f"Average cancellations: {avg_cancelled:.2f}")
# TODO: Create a lineplot of flight delays vs months

plt.plot(data['Month'], data['Delayed'], label='Delays')
plt.plot(data['Month'], data['Cancelled'], label='Cancellations')

# TODO: In the same figure, create a lineplot of flight cancellations vs months

plt.xlabel("Months", fontsize=10)
plt.ylabel("Number of flights", fontsize=10)
plt.title("Flight status at LAX", fontsize=14)
# TODO: Add axis labels, title, and legend

plt.legend()
# Save figure as output_fig.png
plt.savefig('output_fig.png')

# 30.12.1: LAB: Broadway show scatter plot

import matplotlib.pyplot as plt
import pandas as pd

file = input()

# TODO: Read in CSV file as a dataframe
df = pd.read_csv(file)


# TODO: Insert a column to the dataframe as the last column
#       Label the column "Size", which contains half the values in column "Gross Potential"

df['Size'] = df['Gross Potential'] / 2


# TODO: Output dataframe

print(df)

# TODO: Create scatter plot
plt.scatter(df['Capacity'], df['Gross Potential'], marker='x', color='orange', s=df['Size'])


# TODO: Add axis labels and title

plt.xlabel("Capacity", fontsize=10)
plt.ylabel("Gross Potential", fontsize=10)
plt.title("Gross Potential vs Capacity", fontsize=16)

# TODO: Add gridlines

plt.grid(linestyle='--')

# TODO: Save figure as output_fig.png
plt.savefig("output_fig.png")