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
    def update(self,t,x):
        newBiomass = (self.maxSize)/((1)+(((self.maxSize - self.initialSize)/self.initialSize)*math.exp(self.growthRate*-1*t)))
        if newBiomass < self.maxSize:
            self.currentSize = newBiomass
            if self.currentSize >= x:
                self.currentSize += ((x-self.currentSize)*self.growthRate)

    # remove is a function to model what percent of seaweed is removed 
    def remove(self,percent):
        newBiomass = self.currentSize*(percent/100)
        self.currentSize = self.currentSize - newBiomass

    def relativeX(self,x):
        relativeX = x - self.currentSize
        return relativeX
    
    def adjSGR(self):
        self.growthRate -= (self.growthRate)*0.24