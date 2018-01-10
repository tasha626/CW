id=['Swim','Bike','Running']
speed=[1.72,14.66,5.1]
distance=[]
timetaken=[]
total_time=[]
racetotal=[]



clothing=['Cycling Shoes','Running Shoes','Flippers']
eye_wear=['Swimming Goggles', 'Sunglasses']

combo=[]

iterations = len(clothing)*len(eye_wear)

Cycling_Shoes=[0.9,1.12,0.75]
Running_Shoes=[0.98,1.04,1.25]
Flippers=[1.6,0.95,0.7]
Gog=[0.35,-0.08,-0.12]
Sun=[-0.1,0.08,0.05]

modifier = Cycling_Shoes + Running_Shoes + Flippers





def input():
   distance.append(1500)
   distance.append(40000)
   distance.append(10000)

def Display():

    print "======"*3

def Calculation(distance,speed,modifier,eyewear):
    Time=float(distance/((speed*modifier)+(speed*eyewear)))
    return Time



def Main():
    input()
    racetotal=[]
    

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
        
        
       

        
        for t in range(len(id)):
                 
                tmp=Calculation(float(distance[t]), float(speed[t]), float(modifier[z+t]), float(Gog[t]))
                
                timetaken.append(tmp)
                racetotal=sum(timetaken)
                
                
                print "%10s %20.2f"%(id[t],tmp)
        
        total_time.append(racetotal)
       
        print ""
        print "The total race time is: %5.2f seconds."%(racetotal)        

        print "\n" *2
          
        

        
    for i in range (len(id)):
        print "Equipment Combination: %5s and %5s "%(clothing[i], eye_wear[1])
        combo.append(clothing[i]+' and '+eye_wear[1])
        print
        print "Discipline           Time Taken (s)"
        print
        z=i*3
        
        del timetaken[:]
        
        
              

        
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
    
    print "Johnny will take: %5.2f seconds to complete the race in the fastest combination." %(min(total_time))


    sort=total_time.index(min(total_time))
    print "The fastest combination is: %s" %(combo[sort]) 
    


Main()
