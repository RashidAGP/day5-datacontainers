import numpy as np
import matplotlib.pyplot as plt
import seaborn 
import scipy.stats as stats

lamda_num = 2
x = np.random.poisson(lamda_num, size = 1000)
plt.hist(x, bins = 1000)



x_2 = np.random.normal(0,1,1000)

plt.hist(x, bins = 1000)

