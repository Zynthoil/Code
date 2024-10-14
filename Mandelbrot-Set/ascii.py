resolution = 101

# Create complex plane
complexPlane = [[' ' for y in range(resolution)] for x in range(resolution)]

# Given two floats from the complex plane, check if the corresponding complex number is in the mandelbrot set
# Not perfect, but good enough!
def CheckComplexNumber(a, b):
    # print(a, b, end=' | ')
    a = a / ((resolution-1)/4) - 2
    b = b / ((resolution-1)/4) - 2
    # print(a, b)
    z = 0
    c = complex(a, b)
    initialAbs = abs(c)
    # Run loop to check recursive function
    for i in range(10):
        z = z * z + c
    finalAbs = abs(z)
    # Check if absolute value of complex number tends towards infinity
    if finalAbs > 2:
        return False
    else:
        return True

# Prints the plane
def PrintPlane(plane):
    for y in range(resolution - 1, -1, -1):
        for x in range(resolution):
            print(plane[x][y], end='')
        print()

# Assigns each ascii value depending on the CheckComplexNumber function
def CreateMandelbrotSet():
    for y in range(resolution):
        for x in range(resolution):
            if CheckComplexNumber(x, y):
                complexPlane[x][y] = '■'
            # complexPlane[x][y] = '|x' + str(x) + 'y' + str(y) + '|'

CreateMandelbrotSet()
PrintPlane(complexPlane)
