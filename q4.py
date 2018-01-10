# Importing random, creating empty lists for distance, time, speed, race total 
import random
id=['Swim','Bike','Running']
speed=[1.72,14.66,5.1]
distance=[]
timetaken=[]
total_time=[]
racetotal=[]
swim_dist=[]

 # Lists of clothing variables, combo is an empty list, iterations combines clothing & eye_wearclothing=['Cycling Shoes','Running Shoes','Flippers']
eye_wear=['Swimming Goggles', 'Sunglasses']

combo=[]

iterations = len(clothing)*len(eye_wear)

# Values of athelete speeds with each displine & clothing opition
Cycling_Shoes=[0.9,1.12,0.75]
Running_Shoes=[0.98,1.04,1.25]
Flippers=[1.6,0.95,0.7]
Swimming Goggles=[0.35,-0.08,-0.12]
Sunglasses=[-0.1,0.08,0.05]

# Modifier is ensuring that the athelete's results is shown with only one pair of shoes
modifier = Cycling_Shoes + Running_Shoes + Flippers

# Creating a loop
count = 0
while (count < 15):
   del distance [:]
   count = count+1


# Randomsing the swimming distance
   swim=random.randrange(1000,20001)
   swim_dist.append(swim)

# Creating a function to append distances
   def input():
      distance.append(swim)
      distance.append(40000)
      distance.append(10000)

# Printing out display with calculation and using return function to get value from Time
   def Display():

       print "======"*3

   def Calculation(distance,speed,modifier,eyewear):       
      Time=float(distance/((speed*modifier)+(speed*eyewear)))
       return Time


# Calculating racetotal using values from above
   def Main():
       input()
       racetotal=[]
    
#  Printing out with metres and showing equipment combination 
       for i in range(len(id)):
           print
           print "For",id[i],"distance you entered",distance[i],"Metres"
       print "\n "*3

       for i in range (len(id)):
           print "Equipment Combination: %5s and %5s "%(clothing[i], eye_wear[0])
           combo.append(clothing[i]+' and '+eye_wear[0])
           print
           print "Discipline           Time Taken (s)"
           print
           z=i*3
        
        
           del timetaken[:]
        
        
       

# Making values floats, taking timetaken as the racetotal, printing it out the total race time        
           for t in range(len(id)):
                 
                   tmp=Calculation(float(distance[t]), float(speed[t]), float(modifier[z+t]), float(Gog[t]))
                
                   timetaken.append(tmp)
                   racetotal=sum(timetaken)
                
                
                   print "%10s %20.2f"%(id[t],tmp#
       
           total_time.append(racetotal)
       
           print ""
           print "The total race time is: %5.2f seconds."%(racetotal)        

           print "\n" *2
          
        

# Using equipment combos & printing out table with column for Discipline & Time taken        
       for i in range (len(id)):
           print "Equipment Combination: %5s and %5s "%(clothing[i], eye_wear[1])
           combo.append(clothing[i]+' and '+eye_wear[1])
           print
           print "Discipline           Time Taken (s)"
           print
           z=i*3
        
           del timetaken[:]
        
        
              

# Printing out the tmp, appending racetotal & total race time        
           for t in range(len(id)):

                
                   tmp=Calculation(float(distance[t]), float(speed[t]), float(modifier[z+t]), float(Sun[t]))
                
                   timetaken.append(tmp)
                   racetotal=sum(timetaken)
                
                
                
                   print "%10s %20.2f"%(id[t],tmp)
        
           total_time.append(racetotal)
        
       
        
           print ""
           print "The total race time is: %5.2f seconds."%(racetotal)
           print "\n"*2
 

               
                
        



       print ""
       print ""
    
       
       print


       
       
       
    

# Written message for clarity of the user incluing the minimum amount of time taken
   Main()

print "Johnny will take: %5.2f seconds to complete the race in the fastest combination." %(min(total_time))
sort=total_time.index(min(total_time))
print "The fastest combination is: %s" %(combo[sort])
