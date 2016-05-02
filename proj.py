# coding=utf-8
from PIL import Image, ImageDraw

im1 = Image.open("merou.jpg")
draw = ImageDraw.Draw(im1)

(width, height) = im1.size
im2 = Image.new("RGB", (width + 2, height + 2), (0, 0, 0))

d = ImageDraw.Draw(im2)

for x in range(width):
    for y in range(height):
        print "Processing pixel im1 (%d %d)" % (x, y)
        (r, g, b) = im1.getpixel((x, y))
        if 100 <= r <= 154 and 20 <= g <= 75 and 100 <= b <= 175:
            d.point((x, y), (200, 0, 0))


def s1(x, y, n):
    c = n // 2
    if x - c > 0 and x + c < width and y - c > 0 and y + c < height:
        for z in range(x - c, x + c):
            for j in range(y - c, y + c):
                im2.putpixel((z, j), (100, 100, 100))


def s2(x, y):
    if x + 1 < width and y + 1 < height:
        (r, g, b) = im2.getpixel((x + 1, y))
        if (r, g, b) == (100, 100, 100):
            im2.putpixel((x + 1, y), (250, 250, 250))
        (r, g, b) = im2.getpixel((x, y + 1))
        if (r, g, b) == (100, 100, 100):
            im2.putpixel((x, y + 1), (250, 250, 250))
        (r, g, b) = im2.getpixel((x + 1, y + 1))
        if (r, g, b) == (100, 100, 100):
            im2.putpixel((x + 1, y + 1), (250, 250, 250))

for x in range(width):
    for y in range(height):
        (r, g, b) = im2.getpixel((x, y))
        if (r, g, b) == (200, 0, 0):
            s1(x, y, 20)

cpt = 0
for x in range(width):
    for y in range(height):
        (rouge, vert, bleu) = im2.getpixel((x, y))
        if (rouge, vert, bleu) == (100, 100, 100):
            cpt += 1
            print(x, y)
            s2(x, y)
        if (rouge, vert, bleu) == (250, 250, 250):
            s2(x, y)
im2.save("merou3.jpg")

print(cpt)
