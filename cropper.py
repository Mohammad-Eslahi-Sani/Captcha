from PIL import Image
import Image

im = Image.open("randimg(18).jpg")

box1 = [5,0,13,15]
box2 = [14,0,22,15]
box3 = [24,0,31,15]

ex1 = im.crop(box1)
ex2 = im.crop(box2)
ex3 = im.crop(box3)

#ex1.save("first 7.jpeg")
#ex2.save("second 4.jpeg")
#ex3.save("third 1.jpeg")


