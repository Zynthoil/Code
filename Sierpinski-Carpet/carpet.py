from PIL import Image
import random
import math

res = 20000
iterations = 100000000000

img = Image.new('RGB', (res, res), color='white')

edgePoints = [
        (0, 0), # Top left
        (res * 0.5, 0), # Top middle
        (res, 0), # Top right
        (0, res * 0.5), # Left middle
        (res, res * 0.5), # Right middle
        (0, res), # Bottom left
        (res * 0.5, res), # Bottom middle
        (res, res) # Bottom right
        ]

def GenerateNextPoint(point):
    point = (point[0] + 0.5, point[1] + 0.5)
    edgePoint = random.choice(edgePoints)
    # print(edgePoint, end='  ')
    distance = (edgePoint[0] - point[0], edgePoint[1] - point[1])
    newPoint = (int(point[0] + (distance[0] / 3 * 2)), int(point[1] + (distance[1] / 3 * 2)))
    return newPoint

def CreateCarpet():
    point = (random.randint(0, res), random.randint(0, res))
    for i in range(iterations):
        # print(point, end='  ')
        point = GenerateNextPoint(point)
        # print(point)
        img.putpixel(point, (0, 0, 0))
        if i % (iterations / 1000) == 0:
            print(i / iterations * 100)

CreateCarpet()
img.save("Sierpinski-Carpet.png", "png")
img.show()
