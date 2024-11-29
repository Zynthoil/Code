from PIL import Image
import random
import math

res = 20000
iterations = 1000000000

img = Image.new('RGB', (res, res), color='white')
frames = []

topY = res - int(math.sqrt(3 / 4 * res ** 2))
cornerPoints = [
        (res / 2, topY), # Top middle
        (0, res), # Bottom left
        (res, res) # Bottom right
        ]

def GenerateNextPoint(point):
    point = (point[0] + 0.5, point[1] + 0.5)
    cornerPoint = random.choice(cornerPoints)
    distance = (cornerPoint[0] - point[0], cornerPoint[1] - point[1])
    newPoint = (int(point[0] + (distance[0] / 2)), int(point[1] + (distance[1] / 2)))
    return newPoint

def CreateTriangle():
    point = (res / 2, res / 2)
    for i in range(iterations):
        point = GenerateNextPoint(point)
        img.putpixel(point, (0, 0, 0))
        # imgTmp = img.copy()
        # frames.append(imgTmp)
        if i % (iterations / 1000) == 0:
            print(i / iterations * 100)

CreateTriangle()
img.save("Sierpinski-Triangle.png", "png")
# frames[0].save("Sierpinski-Triangle-GIF.gif", format="GIF", append_images = frames[1:], save_all = True, duration = 10, loop=0)
img.show()
