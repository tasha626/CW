
Acivity=['Swim','Bike','Running']
speed=[1.77,14.66,5.1]
distance=[]
clothing=['Cycling Shoes','Running Shoes','Flippers','Swimming Goggles','Sunglasses']

Cycling_Shoes=[-0.1,0.12,-0.25]
Running_Shoes=[-0.02,0.04,0.25]
Flippers=[0.6,-0.05,-0.3]
Swimming_Goggles=[0.35,-0.08,-0.12]
Sunglasses=[-0.1,0.08,0.05]

Swimming=[-0.1,-0.02,0.6,0.35,-0.1]
Cycling=[0.12,0.04,-0.05,-0.08,0.08]
Running=[-0.25,0.25,-0.3,-0.12,0.05]



def input():
   distance.append(1500)
   distance.append(40000)
   distance.append(10000)


def Display():

    print "======"*3

def Calculation(disance,speed,modifier):
    modifier=1.0-modifier
    Time=float((disance/speed)*modifier)
    #print disance,speed,modifier,Time
    return Time


def Clothing_modifyer_finder(Clothing,Acivity):
    Clothing=0

    return Clothing


def Main():
    input()



    print "         Clothing              Time Taken (s)"
    print "======"*8

    time=[]
    for i in range(len(clothing)):
        tmp_time=0
        for x in range(len(Acivity)):
            if x==0:
                tmp_time = tmp_time+Calculation(float(distance[x]), float(speed[x]),Swimming[i])

            if x==1:
                tmp_time = tmp_time+Calculation(float(distance[x]), float(speed[x]),Cycling[i])

            if x==2:
                tmp_time = tmp_time+Calculation(float(distance[x]), float(speed[x]),Running[i])

        time.append(tmp_time)
        print "%17s %20.2f"%(clothing[i],tmp_time)

    print "Smallest =",min(time)," Largest =",max(time)





Main()