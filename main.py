'''
Remake the conversion to Hex. Goal to make a tuple with 3 int in range of [0..255]
'''

import numpy as np
from PIL import Image, ImageColor

file_path = "testTest.txt"
with open(file_path, 'r') as file:
    originalStr = file.read()
# originalStr = "Hello world!"


# transform HEX to RGB tuple 

def hex_to_rgb(hex):
  return tuple(int(hex[i:i+2], 16) for i in (0, 2, 4))


# transform STR to HEX

a = ""
b = []
k = 0
for i in originalStr:
    if k % 1000 == 0:
        print(k)
    if len(a) != 6:
        if len(format(ord(i), "x")) == 1:
            a += "0" + format(ord(i), "x")
        else:
            a += format(ord(i), "x")
        k += 1
    else:
        b.append(a)
        a = ''
        if len(format(ord(i), "x")) == 1:
            a += "0" + format(ord(i), "x")
        else:
            a += format(ord(i), "x")
        k += 1

print(a, b)
if a:
    while len(a) != 6:
        a += "0"
    b.append(a)
    


# divide HEX STR to HEX array

sizeDif = int(np.sqrt(len(originalStr)/3))
pixels = []
d = []
j = 0
k = 0
for i in range(len(b)):
    if k % 1000 == 0:
        print(k)
    if j < sizeDif:
        d.append(b[i])
        j += 1
        k += 1
    else:
        pixels.append(d)
        d = []
        d.append(b[i])
        j = 1
        k += 1

if d:
    while len(d) != sizeDif:
        d.append("ffffff")
    pixels.append(d)

# transform HEX to RGB tuple

newPixels = []
temp = []
for i in pixels:
    for j in i:
        e = hex_to_rgb(j)
        temp.append(e)
    newPixels.append(temp)
    temp = []

for i in newPixels:
    print(len(i))
print(newPixels)
array = np.array(newPixels, dtype=np.uint8)

# Use PIL to create an image from the new array of pixels

new_image = Image.fromarray(array)
new_image.save('dostNew.png')

# new_image = Image.fromarray(newPixels)
# new_image.save('beeNew.png')

