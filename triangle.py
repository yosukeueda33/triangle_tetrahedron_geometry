import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon

point_a = np.array([2,2])
point_b = np.array([6,5])
point_c = np.array([3,9])
arrow_a = point_b - point_a
arrow_b = point_c - point_a

def is_in_triangle(x, y):
    point_p = np.array([x,y])
    arrow_p = point_p - point_a
    v_a = np.transpose(np.asmatrix(arrow_a))
    v_b = np.transpose(np.asmatrix(arrow_b))
    v_p = np.transpose(np.asmatrix(arrow_p))
    A = np.concatenate([v_a, v_b], axis=1)
    w = np.linalg.inv(A) * v_p
    if w[0] >= 0.0 and w[1] >= 0.0 and w.sum() <= 1.0:
        return True
    else:
        return False

# is_in_triangle(5, 3.5)

def motion(event):  
    x = event.xdata
    y = event.ydata

    if not(x is None or y is None):
        ln.set_data(x,y)
        ln.set_marker('o')

        if is_in_triangle(x, y):
            ln.set_color('r')
        else:
            ln.set_color('b')
    plt.draw()

def draw():
    pts = np.array([point_a, point_b, point_c])
    p = Polygon(pts, closed=True, fill=False)
    ax = plt.gca()
    ax.add_patch(p)
    plt.scatter(point_a[0], point_a[1], color='b')
    plt.annotate('A', point_a+np.array([-.1,-.1]))
    plt.scatter(point_b[0], point_b[1], color='b')
    plt.annotate('B', point_b+np.array([-.2,-.1]))
    plt.scatter(point_c[0], point_c[1], color='b')
    plt.annotate('C', point_c+np.array([-.2,-.1]))
    plt.arrow(
        x=point_a[0], y=point_a[1],
        dx=arrow_a[0], dy=arrow_a[1],
        width=0.05, length_includes_head=True
    )
    plt.arrow(
        x=point_a[0], y=point_a[1],
        dx=arrow_b[0], dy=arrow_b[1],
        width=0.05, length_includes_head=True
    )
    pass

fig = plt.figure()
draw()
ln, = plt.plot(
    [],[],marker='x')

plt.connect('motion_notify_event', motion)
plt.show()