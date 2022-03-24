import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats

# load data
data_random = []
with open('./random_boarding/1-3_bags_5_not_following/data_1000_2022-03-24 20:56:33.539028.csv', 'r') as f:
    for line in f.readlines()[1:]:
        data_random.append(float(line))

data_random_3 = []
with open('./random_boarding/3-4_bags_5_not_following/data_1000_2022-03-24 21:06:37.786369.csv', 'r') as f:
    for line in f.readlines()[1:]:
        data_random_3.append(float(line))

data_back_to_front = []
with open('./grouped_random_back_first/1-3_bags_5_not_following/data_1000_2022-03-24 22:17:18.462396.csv', 'r') as f:
    for line in f.readlines()[1:]:
        data_back_to_front.append(float(line))

data_back_to_front_3 = []
with open('./grouped_random_back_first/3-4_bags_5_not_following/data_1000_2022-03-24 22:29:54.505524.csv', 'r') as f:
    for line in f.readlines()[1:]:
        data_back_to_front_3.append(float(line))

data_outer_first = []
with open('./outer_first_boarding/1-3_bags_5_not_following/data_1000_2022-03-24 21:23:52.120121.csv', 'r') as f:
    for line in f.readlines()[1:]:
        data_outer_first.append(float(line))

data_outer_first_3 = []
with open('./outer_first_boarding/3-4_bags_5_not_following/data_1000_2022-03-24 21:28:16.467792.csv', 'r') as f:
    for line in f.readlines()[1:]:
        data_outer_first_3.append(float(line))

plt.hist(data_random, bins=50, histtype=u'step', label="Unstructured (1-3 bags)", color='blue')
plt.hist(data_random_3, bins=50, histtype=u'step', linestyle='dashed', label="Unstructured (3-4 bags)", color='blue')

plt.hist(data_outer_first, bins=50, histtype=u'step', label="Grouped by seat (1-3 bags)", color='orange')
plt.hist(data_outer_first_3, bins=50, histtype=u'step', linestyle='dashed', label="Grouped by seat (3-4 bags)", color='orange')

plt.hist(data_back_to_front, bins=50, histtype=u'step', label="Grouped aft to front (1-3 bags)", color='green')
plt.hist(data_back_to_front_3, bins=50, histtype=u'step', linestyle='dashed', label="Grouped aft to front (3-4 bags)", color='green')

plt.title("Comparison of distributions of different boarding methods")
plt.ylabel('Frequency')
plt.xlabel('Mean Boarding Time (seconds)')
plt.legend()
plt.savefig('dist.png')
plt.show()