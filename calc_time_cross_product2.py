import sys
import datetime
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon

# Ref: https://blog.goo.ne.jp/field_light/e/9692d20174a8045b674d14a260a244a5
#2点のベクトルを求める
def vec(a, b):
    return (a[0] - b[0], a[1] - b[1])

#点 a,b,cの三角形内にpが入っていれば Trueを返す
def tri_in(a, b, c, p): 

    ab = b - a
    bp = p - b

    bc = c - b
    cp = p - c

    ca = a - c
    ap = p - a

    #外積を求める
    c1 = np.cross(np.squeeze(np.asarray(ab)), np.squeeze(np.asarray(bp)))
    c2 = np.cross(np.squeeze(np.asarray(bc)), np.squeeze(np.asarray(cp)))
    c3 = np.cross(np.squeeze(np.asarray(ca)), np.squeeze(np.asarray(ap)))

    #外積の向き　正負がそろっていれば内側
    #return (c1 > 0 and c2 > 0 and c3 > 0)or(c1 < 0 and c2 < 0 and c3 < 0)
    return (c1 >= 0 and c2 >= 0 and c3 >= 0)or(c1 <= 0 and c2 <= 0 and c3 <= 0) #追記　頂点　辺上も内側とする場合はこちらを使う


# Define points.
a = np.matrix([[2],[2]])
b = np.matrix([[6],[5]])
c = np.matrix([[3],[9]])
a = np.squeeze(np.asarray(a))
b = np.squeeze(np.asarray(b))
c = np.squeeze(np.asarray(c))

point_num = 20
p_l = []
for _ in range(0,point_num):
    # p_array = np.random.rand(1,2)
    p_array = np.random.uniform(low=0.0, high=10.0, size=(2,))
    # p = np.transpose(np.asmatrix(p_array))
    p = p_array
    p_l.append(p)

# Process points.

tic = datetime.datetime.now()
result_l = []
for p in p_l:
    r = tri_in(a, b, c, p)
    result_l.append(r)
tac = datetime.datetime.now()
print(f"time(ms):{tac-tic}")

# sys.exit(0)

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
    plt.scatter(p[0], p[1], color=color)

plt.show()