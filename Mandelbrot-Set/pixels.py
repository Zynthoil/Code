from PIL import Image

resolution = 10001

img = Image.new('RGB', (resolution, resolution), color='white')

def CheckComplexNumber(a, b):
    a = a / ((resolution-1)/4) - 2
    b = b / ((resolution-1)/4) - 2
    z = 0
    c = complex(a, b)
    initialAbs = abs(c)
    for i in range(100):
        z = z * z + c
        if abs(z) > 2: return False
    return True

def CreateMandelbrotSet():
    loops = 0
    for y in range(resolution):
        for x in range(resolution):
            if CheckComplexNumber(x, y):
                img.putpixel( (x, y), (0, 0, 0))
        loops += 1
        print(str(loops / resolution * 100) + '%')

CreateMandelbrotSet()
img.save("Mandelbrot-Set-BW-tmp", "png")
img.show()
