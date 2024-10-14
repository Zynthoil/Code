from PIL import Image
img = Image.new('RGB', (100, 100), color='purple')
for x in range(0, 100, 2):
    for y in range(0, 100, 2):
        img.putpixel( (x, y), (255, 0, 0))
img.show()
