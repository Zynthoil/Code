# resolution of mandelbrot set
resolution = 10

# Create complex plane
complexPlane = [[' ' for x in range(resolution)] for y in range(resolution)]

# Given two floats from the complex plane, check if the corresponding complex number is in the mandelbrot set
# Not perfect, but good enough!
def CheckComplexNumber(a, b):
    a = ((a - resolution / 2) + 0.5) / ((resolution - 1) / 2)
    b = ((b - resolution / 2) + 0.5) / ((resolution - 1) / 2)
    print(a, b)
    z = 0
    c = complex(a, b)
    initialAbs = abs(c)
    # Run loop to check recursive function
    for i in range(10):
        z = z * z + c
    finalAbs = abs(z)
    # Check if absolute value of complex number tends towards infinity
    if finalAbs > initialAbs:
        return False
    else:
        return True

# Prints the plane
def PrintPlane(plane):
    for y in range(len(plane) - 1, -1, -1):
        for x in range(len(plane)):
            print(plane[x][y], end='')
        print()

# Assigns each ascii value depending on the CheckComplexNumber function
def CreateMandelbrotSet():
    for y in range(len(complexPlane)):
        for x in range(len(complexPlane)):
            if CheckComplexNumber(x, y):
                complexPlane[x][y] = '#'
            # complexPlane[x][y] = '|x' + str(x) + 'y' + str(y) + '|'

CreateMandelbrotSet()
PrintPlane(complexPlane)
