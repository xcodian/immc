import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats

# load data
# data_random_1_5 = []
# with open('./random_boarding/1-3_bags_5_not_following/data_1000_2022-03-24 20:56:33.539028.csv', 'r') as f:
#     for line in f.readlines()[1:]:
#         data_random_1_5.append(float(line))

# data_random_3_5 = []
# with open('./random_boarding/3-4_bags_5_not_following/data_1000_2022-03-24 21:06:37.786369.csv', 'r') as f:
#     for line in f.readlines()[1:]:
#         data_random_3_5.append(float(line))

# data_random_1_20 = []
# with open('./random_boarding/1-3_bags_5_not_following/data_1000_2022-03-24 20:56:33.539028.csv', 'r') as f:
#     for line in f.readlines()[1:]:
#         data_random_1_20.append(float(line))

# data_random_3_20 = []
# with open('./random_boarding/', 'r') as f:
#     for line in f.readlines()[1:]:
#         data_random_3_20.append(float(line))


# data_back_to_front_1_5 = []
# with open('./grouped_random_back_first/1-3_bags_5_not_following/data_1000_2022-03-24 22:17:18.462396.csv', 'r') as f:
#     for line in f.readlines()[1:]:
#         data_back_to_front_1_5.append(float(line))

# data_back_to_front_3_5 = []
# with open('./grouped_random_back_first/3-4_bags_5_not_following/data_1000_2022-03-24 22:29:54.505524.csv', 'r') as f:
#     for line in f.readlines()[1:]:
#         data_back_to_front_3_5.append(float(line))


# data_outer_first_1_5 = []
# with open('./outer_first_boarding/1-3_bags_5_not_following/data_1000_2022-03-24 21:23:52.120121.csv', 'r') as f:
#     for line in f.readlines()[1:]:
#         data_outer_first_1_5.append(float(line))

# data_outer_first_3_5 = []
# with open('./outer_first_boarding/3-4_bags_5_not_following/data_1000_2022-03-24 21:28:16.467792.csv', 'r') as f:
#     for line in f.readlines()[1:]:
#         data_outer_first_3_5.append(float(line))

# data_outer_first_1_20 = []
# with open('./outer_first_boarding/1-3_bags_20_not_following/data_1000_2022-03-24 21:26:12.463010.csv', 'r') as f:
#     for line in f.readlines()[1:]:
#         data_outer_first_1_20.append(float(line))


# data_outer_first_3_20 = []
# with open('./outer_first_boarding/3-4_bags_20_not_following/data_1000_2022-03-24 21:27:06.819719.csv', 'r') as f:
#     for line in f.readlines()[1:]:
#         data_outer_first_3_20.append(float(line))


# plt.hist(data_random_1_5, bins=50, histtype=u'step', label="Unstructured (1-3 bags, 5% dev)", color='blue')
# plt.hist(data_random_3_5, bins=50, histtype=u'step', linestyle='dashed', label="Unstructured (3-4 bags, 5% dev)", color='blue')

# plt.hist(data_random_1_20, bins=50, histtype=u'step', label="Unstructured (1-3 bags, 20% dev)", color='blue')
# plt.hist(data_random_3_20, bins=50, histtype=u'step', linestyle='dashed', label="Unstructured (3-4 bags, 20% dev)", color='blue')



# plt.hist(data_outer_first_1_5, bins=50, histtype=u'step', label="Grouped by seat (1-3 bags, 5% dev)", color='orange')
# plt.hist(data_outer_first_3_5, bins=50, histtype=u'step', linestyle='dashed', label="Grouped by seat (3-4 bags, 5% dev)", color='orange')

# plt.hist(data_outer_first_1_20, bins=50, histtype=u'step', label="Grouped by seat (1-3 bags, 20% dev)", color='red')
# plt.hist(data_outer_first_3_20, bins=50, histtype=u'step', linestyle='dashed', label="Grouped by seat (3-4 bags, 20% dev)", color='red')

# plt.hist(data_back_to_front_1_5, bins=50, histtype=u'step', label="Grouped aft to front (1-3 bags, 5% dev)", color='green')
# plt.hist(data_back_to_front_3_5, bins=50, histtype=u'step', linestyle='dashed', label="Grouped aft to front (3-4 bags)", color='green')


d_1_3_5 = []
with open('./outer_first_boarding/1-3_5/data_1000_2022-03-24 21:23:52.120121.csv', 'r') as f:
    for line in f.readlines()[1:]:
        d_1_3_5.append(float(line))

d_1_3_10 = []
with open('./outer_first_boarding/1-3_10/data_1000_2022-03-25 11:55:02.430362.csv', 'r') as f:
    for line in f.readlines()[1:]:
        d_1_3_10.append(float(line))

d_1_3_20 = []
with open('./outer_first_boarding/1-3_20/data_1000_2022-03-24 21:26:12.463010.csv', 'r') as f:
    for line in f.readlines()[1:]:
        d_1_3_20.append(float(line))

d_3_4_5 = []
with open('./outer_first_boarding/3-4_5/data_1000_2022-03-24 21:28:16.467792.csv', 'r') as f:
    for line in f.readlines()[1:]:
        d_3_4_5.append(float(line))

d_3_4_10 = []
with open('./outer_first_boarding/3-4_10/data_1000_2022-03-25 11:56:19.872239.csv', 'r') as f:
    for line in f.readlines()[1:]:
        d_3_4_10.append(float(line))

d_3_4_20 = []
with open('./outer_first_boarding/3-4_20/data_1000_2022-03-24 21:27:06.819719.csv', 'r') as f:
    for line in f.readlines()[1:]:
        d_3_4_20.append(float(line))

# plt.hist(data_outer_first_1_5, bins=50, histtype=u'step', label="Grouped by seat (1-3 bags, 5% dev)", color='orange')
# plt.hist(data_outer_first_3_5, bins=50, histtype=u'step', linestyle='dashed', label="Grouped by seat (3-4 bags, 5% dev)", color='orange')

# plt.hist(data_outer_first_1_20, bins=50, histtype=u'step', label="Grouped by seat (1-3 bags, 20% dev)", color='red')
# plt.hist(data_outer_first_3_20, bins=50, histtype=u'step', linestyle='dashed', label="Grouped by seat (3-4 bags, 20% dev)", color='red')

# plt.hist(data_back_to_front_1_5, bins=50, histtype=u'step', label="Grouped aft to front (1-3 bags, 5% dev)", color='green')
# plt.hist(data_back_to_front_3_5, bins=50, histtype=u'step', linestyle='dashed', label="Grouped aft to front (3-4 bags)", color='green')

# plt.hist(d_1_3_5,  bins=50, label="5% disobedience",  color='red')
# plt.hist(d_1_3_10, bins=50, label="10% disobedience", color='orange')
# plt.hist(d_1_3_20, bins=50, label="20% disobedience", color='gold')

plt.hist(d_3_4_5,  bins=50, label="5% disobedience",  color='tab:green')
plt.hist(d_3_4_10, bins=50, label="10% disobedience", color='tab:blue')
plt.hist(d_3_4_20, bins=50, label="20% disobedience", color='tab:purple')

plt.title("Comparison of Outer-First Boarding Methods across Bag Count & Disobedience - 3-4 bags")
plt.ylabel('Frequency')
plt.xlabel('Mean Boarding Time (seconds)')
plt.legend()
plt.savefig('dist.png')
plt.show()