id=['Swim','Bike','Running']
speed=[1.72,14.66,5.1]
distance=[]
timetaken=[]

def input():
    for i in range(len(id)):
        distance.append(float(raw_input("Disance for "+id[i])))
        if distance[i]<0:

            print "Error disance cannot be less than 0"
            exit(0)


def Display():

    print "======"*3

def Calculation(disance,speed):
    Time=float(disance/speed)
    return Time



def Main():
    input()

    for i in range(len(id)):
        print
        print "For",id[i],"distance you entered",distance[i],"Metres"
    print "\n "*3
    print "Discipline           Time Taken (s)"
    print

    for i in range(len(id)):
        tmp=Calculation(float(distance[i]), float(speed[i]))
        timetaken.append(tmp)
        print "%10s %15.2f"%(id[i],tmp)
        


    print ""
    print ""
    print "Johnny will take: %5.2f seconds to complete the race." %(sum(timetaken))
    


Main()
