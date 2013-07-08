from PIL import *
import Image
from math import *
a=input('Please enter the name of the pic in " ":  ')
im = Image.open(a)
f0 = Image.open("first 0.jpeg")
f1 = Image.open("first 1.jpeg")
f2 = Image.open("first 2.jpeg")
f3 = Image.open("first 3.jpeg")
f4 = Image.open("first 4.jpeg")
f5 = Image.open("first 5.jpeg")
f6 = Image.open("first 6.jpeg")
f7 = Image.open("first 7.jpeg")
f8 = Image.open("first 8.jpeg")
f9 = Image.open("first 9.jpeg")
s0 = Image.open("second 0.jpeg")
s1 = Image.open("second 1.jpeg")
s2 = Image.open("second 2.jpeg")
s3 = Image.open("second 3.jpeg")
s4 = Image.open("second 4.jpeg")
s5 = Image.open("second 5.jpeg")
s6 = Image.open("second 6.jpeg")
s7 = Image.open("second 7.jpeg")
s8 = Image.open("second 8.jpeg")
s9 = Image.open("second 9.jpeg")
t0 = Image.open("third 0.jpeg")
t1 = Image.open("third 1.jpeg")
t2 = Image.open("third 2.jpeg")
t3 = Image.open("third 3.jpeg")
t4 = Image.open("third 4.jpeg")
t5 = Image.open("third 5.jpeg")
t6 = Image.open("third 6.jpeg")
t7 = Image.open("third 7.jpeg")
t8 = Image.open("third 8.jpeg")

j0=0
j1=0
j2=0
j3=0
j4=0
j5=0
j6=0
j7=0
j8=0
j9=0
listj=[j0,j1,j2,j3,j4,j5,j6,j7,j8,j9]

ListOfOpens=[f0,f1,f2,f3,f4,f5,f6,f7,f8,f9,s0,s1,s2,s3,s4,s5,s6,s7,s8,s9,t0,t1,t2,t3,t4,t5,t6,t7,t8]
ListOfHistograms=[]
check_histo_first=[]
defrence=[]
defrence0=[]
defrence1=[]
defrence2=[]
defrence3=[]
defrence4=[]
defrence5=[]
defrence6=[]
defrence7=[]
defrence8=[]
defrence9=[]

result=[]
defrences=[defrence0,defrence1,defrence2,defrence3,defrence4,defrence5,defrence6,defrence7,defrence8,defrence9]
for i in range(29):
    ListOfHistograms.append(ListOfOpens[i].histogram())
box1 = [5,0,13,15]
box2 = [14,0,22,15]
box3 = [24,0,31,15]

ex1 = im.crop(box1)
ex2 = im.crop(box2)
ex3 = im.crop(box3)

def first_histo_decreaser(im):
    counter=[0,0,0,0,0,0,0,0,0,0]
    for BigRound in range(10):
        for num_histo in range(768):
            defrence.append(abs(ex1.histogram()[num_histo]-ListOfHistograms[BigRound][num_histo]))
            if (ex2.histogram()[num_histo]==ListOfHistograms[BigRound][num_histo]):
                counter[BigRound]+=1
        print counter

        
    for mainloop in range(768):
        defrence0.append(defrence[mainloop])
        defrence1.append(defrence[mainloop+768])
        defrence2.append(defrence[mainloop+(2*768)])
        defrence3.append(defrence[mainloop+(3*768)])
        defrence4.append(defrence[mainloop+(4*768)])
        defrence5.append(defrence[mainloop+(5*768)])
        defrence6.append(defrence[mainloop+(6*768)])
        defrence7.append(defrence[mainloop+(7*768)])
        defrence8.append(defrence[mainloop+(8*768)])
        defrence9.append(defrence[mainloop+(9*768)])



def second_histo_decreaser(im):
    for BigRound in range(10,20):
        for num_histo in range(768):
            defrence.append(abs(ex2.histogram()[num_histo]-ListOfHistograms[BigRound][num_histo]))
    for mainloop2 in range(768):
        defrence0.append(defrence[mainloop2])
        defrence1.append(defrence[mainloop2+768])
        defrence2.append(defrence[mainloop2+(2*768)])
        defrence3.append(defrence[mainloop2+(3*768)])
        defrence4.append(defrence[mainloop2+(4*768)])
        defrence5.append(defrence[mainloop2+(5*768)])
        defrence6.append(defrence[mainloop2+(6*768)])
        defrence7.append(defrence[mainloop2+(7*768)])
        defrence8.append(defrence[mainloop2+(8*768)])
        defrence9.append(defrence[mainloop2+(9*768)])

def third_histo_decreaser(im):
    for BigRound in range(20,29):
        for num_histo in range(768):
            defrence.append(abs(ex3.histogram()[num_histo]-ListOfHistograms[BigRound][num_histo]))
    for mainloop3 in range(768):
        defrence0.append(defrence[mainloop])
        defrence1.append(defrence[mainloop3+768])
        defrence2.append(defrence[mainloop3+(2*768)])
        defrence3.append(defrence[mainloop3+(3*768)])
        defrence4.append(defrence[mainloop3+(4*768)])
        defrence5.append(defrence[mainloop3+(5*768)])
        defrence6.append(defrence[mainloop3+(6*768)])
        defrence7.append(defrence[mainloop3+(7*768)])
        defrence8.append(defrence[mainloop3+(8*768)])
        defrence9.append(defrence[mainloop3+(9*768)])

first_histo_decreaser(ex1)
first_histo_decreaser(ex2)
first_histo_decreaser(ex3)
        
def adder():
    j0=0
    j1=0
    j2=0
    j3=0
    j4=0
    j5=0
    j6=0
    j7=0
    j8=0
    j9=0
    for h in range(768):
        j0+=defrence0[h]
        j1+=defrence1[h]
        j2+=defrence2[h]
        j3+=defrence3[h]
        j4+=defrence4[h]
        j5+=defrence5[h]
        j6+=defrence6[h]
        j7+=defrence7[h]
        j8+=defrence8[h]
        j9+=defrence9[h]
        listj[0]+=defrence0[h]
        listj[1]+=defrence1[h]
        listj[2]+=defrence2[h]
        listj[3]+=defrence3[h]
        listj[4]+=defrence4[h]
        listj[5]+=defrence5[h]
        listj[6]+=defrence6[h]
        listj[7]+=defrence7[h]
        listj[8]+=defrence8[h]
        listj[9]+=defrence9[h]
    print listj
    b= min(listj)
    print listj.index(b)
adder()
