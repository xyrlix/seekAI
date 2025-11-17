from polygon import Point

if __name__ == "__main__":
    print(Point.__doc__)
    pt1 = Point(1, 5)
    pt2 = Point(0, 0)
    print(f"{pt1}-{pt2}")
    for element in pt1:
        print(f"<{element}>")