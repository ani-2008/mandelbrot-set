
from PIL import Image, ImageDraw

WIDTH = 600
HEIGHT = 400

REAL_START = -2
REAL_END = 1
IMG_START = -1
IMG_END = 1

MAX_ITER = 100

def mandel(c):
    z = 0
    n = 0
    while abs(z) <= 2 and n <= MAX_ITER:
        z = z * z + c
        n += 1
    return n


img = Image.new('RGB',(WIDTH,HEIGHT),(255,255,255))

draw = ImageDraw.Draw(img)

for x in range(0,WIDTH):
    for y in range(0, HEIGHT):
        c = complex(REAL_START + (x / WIDTH) * (REAL_END - REAL_START), IMG_START + (y / HEIGHT) * (IMG_END - IMG_START))
        m = mandel(c)

        color = abs(0 - int(m * 255 / MAX_ITER))
        
        draw.point([x,y],(color, color, color))

img.save("ouput.png",'PNG')



