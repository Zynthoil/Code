# Size of Mandelbrot set
width = 100
height = 100

# Create complex plane
complexPlane = [[' ' for x in range(width)] for y in range(height)]

# Given two floats from the complex plane, check if the corresponding complex number is in the mandelbrot set
# Not perfect, but good enough!
def CheckComplexNumber(a, b):
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
    for x in range(len(plane)):
        for y in range(len(plane)):
            print(plane[x][y], end = '')
        print()

# Assigns each ascii value depending on the CheckComplexNumber function
def CreateMandelbrotSet():
    for x in range(len(complexPlane)):
        for y in range(len(complexPlane)):
            if CheckComplexNumber(x, y):
                complexPlane[x][y] = '#'

CreateMandelbrotSet()
PrintPlane(complexPlane)
