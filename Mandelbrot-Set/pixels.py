from PIL import Image

resolution = 10001

img = Image.new('RGB', (resolution, resolution), color='white')


def CheckComplexNumber(a, b):
    # print(a, b, end=' | ')
    a = a / ((resolution-1)/4) - 2
    b = b / ((resolution-1)/4) - 2
    # print(a, b)
    z = 0
    c = complex(a, b)
    initialAbs = abs(c)
    # Run loop to check recursive function
    for i in range(100):
        z = z * z + c
        if abs(z) > 2: return False
    finalAbs = abs(z)
    # Check if absolute value of complex number tends towards infinity
    if finalAbs > 2:
        return False
    else:
        return True

def CreateMandelbrotSet():
    for y in range(resolution):
        for x in range(resolution):
            if CheckComplexNumber(x, y):
                img.putpixel( (x, y), (0, 0, 0))

CreateMandelbrotSet()
# img.save("Mandelbrot-Set-BW", "png")
img.show()
