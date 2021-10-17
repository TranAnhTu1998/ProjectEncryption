from PIL import Image
import numpy as np

str = "I love you"
len_str_pixel = len(str)

if len_str_pixel % 3 == 1:
    str += '  '
elif len_str_pixel % 3 == 2:
    str += ' '
print("len(str) = ", len(str))

i = 0
pixels = []
while i <= len(str)-1:

    num_acsii_red = ord(str[i])
    if num_acsii_red % 2 == 1:
        num_acsii_red += 1
    num_acsii_greed = ord(str[i+1])
    if num_acsii_greed % 2 == 1:
        num_acsii_greed += 1
    num_acsii_blue = ord(str[i+2])
    if num_acsii_blue % 2 == 1:
        num_acsii_blue += 1
    a_pixel = (num_acsii_red, num_acsii_greed, num_acsii_blue)
    pixels.append(a_pixel)
    i += 3
    #print(num_acsii, ' ')
print(pixels) #test

# Convert the pixels into an array using numpy
array_pixel = np.array(pixels, dtype=np.uint8)

#Using PIL to create an image from the new array of pixels
new_image = Image.fromarray(array_pixel)
new_image.save('new.png')
