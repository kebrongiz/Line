def intersect(m1, b1, m2, b2):

    if (m1 == m2 and b1 != b2):
        return 1
    return 0
m1 = int(input("Enter the slope of frist line: "))
b1 = int(input("Enter the y-intersept of frist line: "))
m2 = int(input("Enter the slope of second line: "))
b2 = int(input("Enter the y-intersept of second line: "))

print(intersect(m1, b1, m2,b2))