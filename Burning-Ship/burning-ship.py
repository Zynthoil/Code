from PIL import Image
from numpy import array
import colorsys
import time

resolution = 20000
iterations = 100
point = (0.975, -1.175)
bounds = 0.25
upperBoundX = point[0] + bounds
lowerBoundX = point[0] - bounds
upperBoundY = point[1] + bounds
lowerBoundY = point[1] - bounds

img = Image.new('RGB', (resolution, resolution), color='white')

def GenerateColour(n):
    colour = 255 * array(colorsys.hsv_to_rgb(n / 255, 1, 0.5))
    return tuple(colour.astype(int))

def ScaleRange(x, minInput, maxInput, minScale, maxScale):
    inputRange = maxInput - minInput
    scaleRange = maxScale - minScale
    scaledNum = (scaleRange*((x-minInput)/inputRange))-(scaleRange/2)
    return scaledNum

def CheckComplexNumber(a, b):
    a = ScaleRange(a-0.5, 0, resolution-1, lowerBoundX, upperBoundX)
    a += point[0]
    b = ScaleRange(b-0.5, 0, resolution-1, lowerBoundY, upperBoundY)
    b += point[1]
    za = a
    zb = b
    for i in range(iterations):
        z = za ** 2 - zb ** 2 + a
        xtmp = z
        zb = abs(2*za*zb) + b
        za = xtmp
        if za ** 2 + zb ** 2 > 4: return GenerateColour(i)
    return (0, 0, 0)

def CreateMandelbrotSet():
    loops = 0
    for y in range(int(resolution)):
        for x in range(resolution):
            colour = CheckComplexNumber(x, y)
            img.putpixel( (x, y), colour)
        loops += 1
        percentage = loops / resolution * 100
        print(str(round(percentage, 2)) + '%')

startTime = time.perf_counter()
CreateMandelbrotSet()
endTime = time.perf_counter()
timeTaken = endTime - startTime
print(timeTaken)
img.save("Burning-Ship-tmp.png", "png")
img.show()
