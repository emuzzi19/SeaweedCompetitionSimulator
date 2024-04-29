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
    def __init__(self, name,initialSize, growthRate, maxSize):
        self.name = name
        self.currentSize = initialSize
        self.initialSize = initialSize
        self.growthRate = growthRate
        self.maxSize = maxSize
        
    # Seaweed Methods
      
    
    # update is a function of days since planting in relation to biomass 
    def update(self,t):
        newBiomass = (self.maxSize)/((1)+(((self.maxSize - self.initialSize)/self.initialSize)*math.exp(self.growthRate*-1*t)))
        self.currentSize = newBiomass
