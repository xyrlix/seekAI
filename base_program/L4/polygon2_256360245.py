from polygon import Point3D, Point

if __name__ == "__main__":
    stdid = '045'
    print(f"stdid: {stdid}")
    a = int(stdid[2])
    b = int(stdid[1])
    pt1 = Point(1, a)
    pt2 = Point(0, 0)
    pt3 = Point3D(1, 2, 0)
    pt4 = Point3D(-1, 0, b)
    gen_obj = (x for x in [pt1, pt2, pt3, pt4])
    print(f'{"".join([str(y)+".-." for y in gen_obj])}')