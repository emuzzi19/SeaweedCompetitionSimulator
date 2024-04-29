#imports
import matplotlib.pyplot as plt
from seaweed import seaweed


# create agents

N1 = seaweed('N1',10.86,0.098523,134.46)
N2 = seaweed('N2',10.86,0.108391,170.69)


# simulation logic
#------------------------
# parameters
# t is the maximum number of timesteps you want to simulate in days
# mode is the types of population controls you want to impose on N2 (species 2 of seaweed)
# size is the maximum amount of space the two seaweeds have to grow into (the combined size of both has to be less than size)
#---------------------------

def sim(t,mode,size):
    days = 0
    x = size
    xaxis = []  #sets up an array to capture timesteps as we move through the simulation
    N1Trace = []   # sets up an array to capture the values N1 biomass as we move through time 
    N2Trace = []    # sets up an array to capture the values N2 biomass as we move through time 
    while days < t:
        leftToGrow = (N1.currentSize + N2.currentSize < x) # checks at each timestep to see if there is room left to grow
        if leftToGrow:
            if N1.currentSize <= N1.maxSize:
                N1.update(days)
            if N2.currentSize <= N2.maxSize:
                N2.update(days)
        N1Trace.append(N1.currentSize)
        N2Trace.append(N2.currentSize)
        xaxis.append(days)
        days += 1
    plot(xaxis,N1Trace,N2Trace)
 
#------------------------
# parameters
# x is an array of values for the xaxis
# values1 and values2 are arrays for the values of the biomass of seaweeds 1 & 2 over time
#---------------------------
def plot(x,values1, values2):
    plt.plot(x, values1, label='Seaweed 1 Biomass')
    plt.plot(x, values2, label='Seaweed 2 Biomass')
    plt.legend()
    plt.title("Trace of Seaweed Biomass over Time")
    plt.xlabel('Time (Days)')
    plt.ylabel('Biomass (KG)')
    plt.show()
    

#----------------------------------------------------------------------------------------------------

sim(120,'none',400)