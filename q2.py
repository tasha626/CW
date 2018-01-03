
# Importing matplot & pylab
import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt
import pylab


# Defining list of "Activities" & time taken to complete themnt# Empty list for distance so can be imputted by user


Acivity=['Swim','Bike','Running']
 speed=[1.77,14.66,5.1]
distance=[]
clothing=['Cycling Shoes','Running Shoes','Flippers','Swimming Goggles','Sunglasses']

# Adding variables to clothing items changing timings for each event

Cycling_Shoes=[-0.1,0.12,-0.25]
Running_Shoes=[-0.02,0.04,0.25]
Flippers=[0.6,-0.05,-0.3]
Swimming_Goggles=[0.35,-0.08,-0.12]
Sunglasses=[-0.1,0.08,0.05]
 

# Changes to each activity from each clothing item catergorised 
# Time as an open list & creating points for graph

Swimming=[-0.1,-0.02,0.6,0.35,-0.1]
Cycling=[0.12,0.04,-0.05,-0.08,0.08]
Running=[-0.25,0.25,-0.3,-0.12,0.05]
y = []
time=[]
xx = [0,2,3]


# Defining new function to append distances & calculations & display clearly with lines  
# Time function gets value using return function


def input():
   distance.append(1500)
   distance.append(40000)
   distance.append(10000)


   def Display():

     print "======"*3

def Calculation(distance,speed,modifier):
    modifier=1.0-modifier
    Time=float((distance/speed)*modifier)
    print distance,speed,modifier,Time
    return Time

# Return function gets value from Clothing function


def Clothing_modifyer_finder(Clothing,Acivity):
    Clothing=0

    return Clothing

# Plotting graph, labelling y axis Time, x axis Time
# Creating the histogram from imputted data

def Graph_plot():
    n = len(clothing)
    window = [0,max(time)]
    pylab.ylabel("Time")
    pylab.xlabel("Time")
    pylab.title("Histogram")

    pylab.hist(y, 900, window)
    pylab.savefig("q2d.png")
    pylab.show()

# Creating max & min, printing out histogram
   
def Main():
    input()

    print "         Clothing              Time Taken (s)"
    print "======"*8

    Name_clothing_max=''
    Name_clothing_min=''




    #TODO x append does not work for some reason.
    for i in range(10):
        xx.append(i)


    for i in range(len(clothing)):
        ##TODO Fix this

        tmp_time=0
        for x in range(len(Acivity)):

            if x==0:
                tmp_time = tmp_time+Calculation(float(distance[x]), float(speed[x]),Swimming[i])

            if x==1:
                tmp_time = tmp_time+Calculation(float(distance[x]), float(speed[x]),Cycling[i])

            if x==2:
                tmp_time = tmp_time+Calculation(float(distance[x]), float(speed[x]),Running[i])

        time.append(tmp_time)
        print "%17s | %20.2f"%(clothing[i],tmp_time)
        y.append(tmp_time)
    #Names for Clothing with largest and smallest
    for i in range(len(clothing)):
        if time[i]==max(time):
            Name_clothing_max=clothing[i]
        elif time[i]==min(time):
            Name_clothing_min=clothing[i]


    print "Smallest =",Name_clothing_min,round(min(time),2),"(s)",Name_clothing_max," Largest =",round(max(time),2),"(s)"
    Graph_plot()



Main()
