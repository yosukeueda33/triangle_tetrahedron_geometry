import sys
import datetime
import numpy as np
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d.axes3d as p3
import matplotlib.animation as animation

np.random.seed(0)

# Ref:https://stackoverflow.com/a/61703017
def tetraCoord_Dorian(A,B,C,D):
    v1 = B-A ; v2 = C-A ; v3 = D-A
    # mat defines an affine transform from the tetrahedron to the orthogonal system
    mat = np.array((v1,v2,v3)).T
    # The inverse matrix does the opposite (from orthogonal to tetrahedron)
    M1 = np.linalg.inv(mat)
    return(M1) 

def pointInside_Dorian(v1,v2,v3,v4,p):
    # Find the transform matrix from orthogonal to tetrahedron system
    M1=tetraCoord_Dorian(v1,v2,v3,v4)
    # apply the transform to P
    newp = M1.dot(p-v1)
    # perform test
    return (np.all(newp>=0) and np.all(newp <=1) and np.sum(newp)<=1)

fig = plt.figure()
ax = p3.Axes3D(fig)

# Define points.
# a = np.matrix([[2], [2], [0]])
# b = np.matrix([[9], [5], [0]])
# c = np.matrix([[3], [9], [1]])
# d = np.matrix([[3], [4], [9]])
a = np.matrix([[1], [1], [1]])
b = np.matrix([[1], [10], [1]])
c = np.matrix([[1], [1], [10]])
d = np.matrix([[10], [1], [1]])
a = np.squeeze(np.asarray(a))
b = np.squeeze(np.asarray(b))
c = np.squeeze(np.asarray(c))
d = np.squeeze(np.asarray(d))

point_num = 20
p_l = []
for _ in range(0,point_num):
    p_array = np.random.uniform(low=0.0, high=10.0, size=(3,))
    p = p_array
    p_l.append(p)
# p_l = [np.matrix([[0.3], [5], [1]])]

# Process points.
tic = datetime.datetime.now()
result_l = []
for p in p_l:
    r = pointInside_Dorian(a, b, c, d, p)
    result_l.append(r)
tac = datetime.datetime.now()
print(f"time(ms):{tac-tic}")

# sys.exit(0)

# Show results.
def put_scatter(v, color='k'):
    ax.scatter(v[0], v[1], v[2], color=color)

def put_line(v, w, color='k'):
    ax.plot(
        [v[0], w[0]],
        [v[1], w[1]],
        [v[2], w[2]],
        color=color
    )

put_scatter(a)
put_scatter(b)
put_scatter(c)
put_scatter(d)
put_line(a,b)
put_line(a,c)
put_line(a,d)
put_line(b,c)
put_line(b,d)
put_line(c,d)


for p,r in zip(p_l, result_l):
    color = None
    if r:
        color = 'r'
    else:
        color = 'b'
    put_scatter(p, color=color)

plt.show()
sys.exit(0)

def update(i):
    ax.view_init(elev=10., azim=i*10)

def draw():
    ani = animation.FuncAnimation(fig, update, interval = 200, frames = 30)
    ani.save("test.gif")

draw()