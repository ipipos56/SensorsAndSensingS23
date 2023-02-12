import matplotlib.pyplot as plt
import numpy as np

# Define the two-modal distribution
def two_modal_distribution(size):
    return np.concatenate([np.random.normal(0, 1, int(size/2)), np.random.normal(10, 1, int(size/2))])

# Generate 1000 samples of 150 points each
num_samples = 1000
sample_size = 150
sample_means = [np.mean(two_modal_distribution(sample_size)) for _ in range(num_samples)]

# Plot the distribution of sample means
plt.hist(sample_means, bins=20, edgecolor='black')
plt.xlabel('Sample Mean')
plt.ylabel('Frequency')
plt.title('Distribution of Sample Means')
plt.show()


