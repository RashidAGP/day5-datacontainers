import numpy as np
from scipy.linalg import solve, lstsq
a = np.array([[1,2,3],[4,5,6],[7,8,9]])

b = np.array([1,2,3])
x = []
# This does not work. I don't lnow why?!!!!!
# x = np.linalg.lstsq(a,b) 
x = np.linalg.lstsq(a,b)

print(x)


'''
B = np.random.randint(0,100, (3,3))
print(B)

result = lstsq(a,B)
print(result)
'''
'''
f = np.linalg.eigvals(a)
print(f)
'''

'''
g = np.linalg.inv(a)
print(g)
'''


'''
h = linalg.norm(a, np.inf)
print(h)



h1 = linalg.norm(a, 'fro')
print(h1)



h2 = linalg.norm(a, 1)
print(h2)

'''
