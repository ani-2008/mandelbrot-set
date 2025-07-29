from PIL import Image, ImageDraw

WIDTH = 600
HEIGHT = 400

RE_START = -2
RE_END = 1
IM_START = -1
IM_END = 1

MAX_ITER = 100

def mandel(c):
    z = 0
    n = 0
    while abs(z) <= 2 and n <= MAX_ITER:
        z = z * z + c
        n += 1
    return n


im = Image.new('RGB',(WIDTH,HEIGHT),(0,0,0))

draw = ImageDraw.Draw(im)

for x in range(0,WIDTH):
    for y in range(0, HEIGHT):
        c = complex(RE_START + (x / WIDTH) * (RE_END - RE_START), IM_START + (y / HEIGHT) * (IM_END - IM_START))
        m = mandel(c)

        color = 255 - int(m * 255 / MAX_ITER)
        
        draw.point([x,y],(color, color, color))

im.save("ouput.png",'PNG')


