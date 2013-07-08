from PIL import Image
import Image

im = Image.open("randimg(7).jpg")
im2 = Image.open("randimg(3).jpg")
##im2 = Image.open("first 3.jpeg")
checker1 = Image.open("first 6.jpeg")
checker2 = Image.open("second 6.jpeg")
checker3 = Image.open("third 6.jpeg")

im.size=[37,15]

box1 = [5,0,13,15]
box2 = [14,0,22,15]
box3 = [24,0,31,15]

##im2.size=[37,15]

checker1.size=[37,15]
checker2.size=[37,15]
checker3.size=[37,15]

##box01 = [5,0,13,15]
##box02 = [14,0,22,15]
##box03 = [23,0,31,15]

ex1 = im.crop(box1)
ex2 = im.crop(box2)
ex3 = im.crop(box3)

firsth=ex1.convert("P")
secondh=ex2.convert("P")
thirdh=ex3.convert("P")
print (im.histogram())
print "\n\n\n"
print (firsth.histogram())
print "\n\n\n"
print (secondh.histogram())
print "\n\n\n"
print (thirdh.histogram())
print "\n\n\n"



ex01 = im2.crop(box1)
ex02 = im2.crop(box2)
ex03 = im2.crop(box3)
##
ex1.save("110.jpeg")
ex2.save("120.jpeg")
ex3.save("130.jpeg")
ch1 = Image.open("11.jpeg")
ch2 = Image.open("12.jpeg")
ch3 = Image.open("13.jpeg")
ch11 = Image.open("110.jpeg")
ch12 = Image.open("120.jpeg")
ch13 = Image.open("130.jpeg")


firstj=ex01.convert("P")
secondj=ex02.convert("P")
thirdj=ex03.convert("P")

print firsth.histogram()
print "\n\n\n\n"
print secondh.histogram()
print "\n\n\n\n"
print ch3.histogram()
print "\n\n\n\n"
print ch13.histogram()
print "\n\n\n\n"
print checker2.histogram()
print "\n\n\n\n"
print checker3.histogram()
print "\n\n\n\n"

##if ch3.histogram()==ch13.histogram():
##    print "is matched"
##else:
##    print "not matched"
##print len(ch3.histogram())
##if secondh.histogram()==im2.histogram():
##    print "second 6 is matched"
##else:
##    print "not matched"
##if thirdh.histogram()==im2.histogram():
##    print "third 6 is matched"
##else:
##    print "not matched"

##pix = ex1.load()
##print ex1.size #Get the width and hight of the image for iterating over
##print pix[0,0] #Get the RGBA Value of the a pixel of an image
##print pix[0,1]," ",pix[0,2]

#################################################################################
# 1 checker
#################################################################################

