'''
Remake the conversion to Hex. Goal to make a tuple with 3 int in range of [0..255]
'''

import numpy as np
from PIL import Image, ImageColor
import codecs

filePath = "readingTest.txt"

# The first open is for txt files without Cyrillic

# with open(file_path, 'r', ) as file:
#    originalStr = file.read()


file = codecs.open(filePath, "r", "utf_8_sig")
originalStr = file.read()



# transform HEX to RGB tuple 

def hex_to_rgb(hex):
    if typeEncoding == 2:
        a = int(hex[0:2], 16)
        b = (0, 0, 0, a)
        return b
    else:
        return tuple(int(hex[i:i+2], 16) for i in (0, 2, 4, 6))

'''
# transform STR to HEX STR

def str_to_hex(symbol):
    a += format(ord(symbol), "x")
'''

"""
This part sets the type of encoding

select 6 for RGB
select 8 for RGB + alpha
select 2 for alpha
"""

typeEncoding = 2


beeMage = Image.open("beemage.png")
width, height = beeMage.size


# transform STR to HEX

a = ""
b = []
k = 0
lenOrStr = len(originalStr)


# for i in originalStr:
#     if k % 50000 == 0:
#         print((k / lenOrStr)* 100)
#     a += format(ord(i), "x")
#     k += 1


# This is decode/encode section

a = []
with open(filePath, "rb") as f:
    byteStr = f.read()

byteToStr = byteStr.decode()
with open("testTest.txt", "w", encoding="utf-8") as f:
    f.write(byteToStr)



while len(a) % typeEncoding != 0:
    a += "0"

# Divide into equal parts
chunks, chunkSize = len(a), typeEncoding
b = [a[i:i+chunkSize] for i in range(0, chunks, typeEncoding)]

# divide HEX STR to HEX array

#sizeDif = int(np.sqrt(len(originalStr)/ (typeEncoding / 2)))

# Ye olde 

if b:
    while len(b) % width != 0:
        emptyPixels = typeEncoding * "7"
        b.append(emptyPixels)

pixels = []

chunks, chunkSize = len(b), width
pixels.append([b[i:i+chunkSize] for i in range(0, chunks, width)])

# transform HEX to RGB tuple

newPixels = []
temp = []
for i in pixels[0]:
    for j in i:
        e = hex_to_rgb(j)
        temp.append(e)
    newPixels.append(temp)
    temp = []

'''
for i in newPixels:
    print(len(i))
print(newPixels)
'''


print(len(newPixels), len(newPixels[0]), height)

d = (0, 0, 0, 120)
temp = [d] * width

'''while len(newPixels) != height:
    newPixels.append(temp)'''

while len(newPixels) != height and len(newPixels) < height - len(newPixels):
    print(1)
    a = len(newPixels)
    for i in range(a):
        newPixels.append(newPixels[i])
    print(len(newPixels), len(newPixels[0]), height)
else:
    while len(newPixels) != height:
        newPixels.append(temp)

print(len(newPixels), len(newPixels[0]), height)

array = np.array(newPixels, dtype=np.uint8)

# Use PIL to create an image from the new array of pixels

new_image = Image.fromarray(array)
new_image.save('roundTest'+ str(typeEncoding) +'.png')

print(new_image.size, beeMage.size )

newBeeMage = Image.alpha_composite(beeMage, new_image)
newBeeMage.save(('roundBeeTest1'+ str(typeEncoding) +'.png'))
