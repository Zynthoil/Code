# Resolution of mandelbrot set, must be set to multiple of 5
resolution = 20
resolutionX = resolution
resolutionY = int(resolution)

# Create complex plane
complexPlane = [[' ' for y in range(resolutionY)] for x in range(resolutionX)]

# Given two floats from the complex plane, check if the corresponding complex number is in the mandelbrot set
# Not perfect, but good enough!
def CheckComplexNumber(a, b):
    print(a, b, end=' | ')
    a = (a / ((resolutionX - 1) / 2)) - 1.5
    b = (b / ((resolutionY - 1) / 2)) - 1
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
