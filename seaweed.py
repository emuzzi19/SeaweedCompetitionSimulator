#=====================================================================================================
#
#                       ~ Seaweed Agent for Seaweed Competition Simulation ~
#
#
#=====================================================================================================
#imports
import math

class seaweed:


    #constructor
    def __init__(self, name, currentSize,initialSize, growthRate, maxSize):
        self.name = name
        self.currentSize = currentSize
        self.initialSize = initialSize
        self.growthRate = growthRate
        self.maxSize = maxSize
        
    # Seaweed Methods
      
    
    # update is a function of days since planting in relation to biomass 
    def update(t):
        newBiomass = (self.maxSize)/(1+(self.maxSize - self.initialWeight/self.initialWeight))*math.exp(-1* self.growthRate * t)
        self.currentSize = newBiomass
