
#All in m

Swim_dis=float(input("Swiming Disance(m)"))
Cycle_dis=float(input("Cycling Disance (m)"))
Run_dis=float(input("Running Disance (m)"))


Time_Swim=float(0)
Time_Cycle=float(0)
Time_Running=float(0)

if Swim_dis<0 or Time_Cycle<0 or Run_dis<0:
    print "Error one or more of your entered input was less than 0 please try again."

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
        print "\n \n"

        print "swimming distance you entered:%.1f metres"%Swim_dis
        print "For cycling distance you entered: %.1f metres"%Cycle_dis
        print "For running distance you entered: %.1f metres"%Run_dis
        print
        print "Discipline       Time Taken (s)"
        print "======"*4
        print "Swim         %10.2f"%(Swim())
        print "Cycling      %10.2f" % (Cycling())
        print "Running      %10.2f" % (Running())

        Time=Swim()+Cycling()+Running()
        print Time

    Main()
