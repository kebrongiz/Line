def line(m, b, x):
    return (m * x) + b
m = float(input("Enter the slope of the line: "))
b = float(input("Enter the y-intersept of the line: "))
x = float(input("Enter the x-coordinate of the line: "))
print("The y-coordinate of line x-coordinate {}, y-intersept {} and slope {} is : {}".format(x, b, m, line(m, b, x) ))