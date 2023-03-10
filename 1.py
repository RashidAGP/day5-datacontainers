import numpy as np
from scipy import linalg
a = np.array([[1,2,3],[4,5,6],[7,8,9]])
'''
b = np.array([1,2,3])
x = []
x = np.linalg.solve(a,b)

print(x)
'''
'''
Create the 3D vecror for B

B = np.random.randInt(0,100, size (3,3,3))

'''

'''
f = np.linalg.eigvals(a)
print(f)
'''

'''
g = np.linalg.inv(a)
print(g)
'''



h = linalg.norm(a, np.inf)
print(h)



h1 = linalg.norm(a, 'fro')
print(h1)



h2 = linalg.norm(a, 1)
print(h2)
