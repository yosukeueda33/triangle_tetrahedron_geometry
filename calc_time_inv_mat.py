import sys
import datetime
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon

def is_in_triangle(a, b, c, p):
    v_a = b - a
    v_b = c - a
    v_p = p - a
    A = np.concatenate([v_a, v_b], axis=1)
    w = np.linalg.inv(A) * v_p
    if np.all(w>=0)and np.all(w<=1) and w.sum() <= 1.0:
        return True
    else:
        return False

# Define points.
a = np.matrix([[2],[2]])
b = np.matrix([[6],[5]])
c = np.matrix([[3],[9]])

point_num = 1000
p_l = []
for _ in range(0,point_num):
    p_array = np.random.uniform(low=0.0, high=10.0, size=(2,))
    p = np.transpose(np.asmatrix(p_array))
    p_l.append(p)

# Process points.
tic = datetime.datetime.now()
result_l = []
for p in p_l:
    r = is_in_triangle(a, b, c, p)
    result_l.append(r)
tac = datetime.datetime.now()
print(f"time(ms):{tac-tic}")

sys.exit(0)

# Show points and results.
fig = plt.figure()
point_a = np.squeeze(np.asarray(a))
point_b = np.squeeze(np.asarray(b))
point_c = np.squeeze(np.asarray(c))
pts = np.array([point_a, point_b, point_c])
p = Polygon(pts, closed=True, fill=False)
ax = plt.gca()
ax.add_patch(p)
for p,r in zip(p_l, result_l):
    color = None
    if r:
        color = 'r'
    else:
        color = 'b'
    plt.scatter(p[0,0], p[1,0], color=color)

plt.show()