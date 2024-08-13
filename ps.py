import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import mode

data = [90, 83, 80, 73, 70, 51, 68, 79, 70, 71, 72, 74, 67, 54, 81, 66, 62, 63, 68, 57, 66, 96, 78, 55, 60, 66, 57, 71, 60, 85, 76, 98, 77, 88, 78, 81, 64, 66, 77, 70]
# Sort the data in ascending order for creating ogive
sum=np.sum(data)
sorted_data = sorted(data)
cumulative_freq = []
total = len(sorted_data)
mean = sum/total
#median = np.median(data)
median=(70+71)/2
mode=mode(data)[0]
std_deviation = np.std(data)
std_deviation = np.std(data)
pearson_skewness = 3 * (mean - median) / std_deviation
print("Mean:", mean)
print("Median:", median)
print("Mode:",mode)
print("Standard Deviation:", std_deviation)
print("Karl Pearson's Coefficient of Skewness:", pearson_skewness)
print('Skewness=Approximate symmetry')


# Calculate cumulative frequencies for ogive
cumulative_sum = 0
for i, value in enumerate(sorted_data):
    cumulative_sum += 1
    cumulative_freq.append(cumulative_sum)

# Create a histogram
plt.plot(data)
plt.title('Line graph')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.show()

plt.subplot(2, 1, 1)  # Create two subplots, first one for histogram
plt.hist(data, bins=10, edgecolor='k')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.title('Histogram')

# Create an ogive curve
plt.subplot(2, 1, 2)  # Second subplot for ogive curve
plt.plot(sorted_data, cumulative_freq, marker='o')
plt.xlabel('Value')
plt.ylabel('Cumulative Frequency')
plt.title('Ogive Curve')

plt.tight_layout()  # To ensure subplots don't overlap
plt.show()
