
#All in m

Swim_dis=float(input("Swiming Disance(m)"))
Cycle_dis=float(input("Cycling Disance (m)"))
Run_dis=float(input("Running Disance (m)"))


Time_Swim=float(0)
Time_Cycle=float(0)
Time_Running=float(0)

if Time_Swim or Time_Cycle or Time_Running>0:
    print "Error"
    Time_Swim = float(0)
    Time_Cycle = float(0)
    Time_Running = float(0)
else:

    Time=float(0)

    def Swim():
        Time=Swim_dis/1.722222
        return Time

    def Cycling():
        Time=Cycle_dis/14.66667
        return Time
    def Running():
        Time=Cycle_dis/5.083333
        return Time

 

    def Main():
        print "Discipline       Time Taken (s)"
        print "======"*4
        print "Swim         %2.2f"%(Swim())
        print "Cycling      %2.2f" % (Cycling())
        print "Running      %2.2f" % (Running())

        Time=Swim()+Cycling()+Running()
        print Time

    Main()
