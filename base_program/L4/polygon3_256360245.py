import matplotlib.pyplot as plt
import numpy as np
from polygon import Point3D, Polygon

if __name__ == "__main__":
    stdid = '045'
    a = int(stdid[2])
    b = int(stdid[1])
    c = int(stdid[0])
    pt1 = Point3D(0, 0, 0)
    pt2 = Point3D(0, 1, a)
    pt3 = Point3D(-5, 2, b)
    pt4 = Point3D(-3, 0, c)
    poly1 = Polygon([pt1, pt2, pt3, pt4])
    print(f"stdid: {stdid}")
    print(poly1)

    #Plot
    plt.style.use('_mpl-gallery')
    xs = np.array([pts.point[0] for pts in poly1.points])
    ys = np.array([pts.point[1] for pts in poly1.points])
    zs = np.array([pts.point[2] for pts in poly1.points])
    fig = plt.figure(figsize=(20, 15))
    ax = fig.add_subplot(projection='3d')
    ax.scatter(xs, ys, zs)
    ax.plot(xs, ys, zs)
    plt.show()