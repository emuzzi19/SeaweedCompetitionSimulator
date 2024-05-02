#imports
from email.errors import FirstHeaderLineIsContinuationDefect
from tkinter import LAST
from turtle import left
import matplotlib.pyplot as plt
from seaweed import seaweed


# create agents

#N1 = seaweed('N1',10.86,0.098523,134.46)
#N2 = seaweed('N2',10.86,0.108391,170.69)

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QComboBox, QHBoxLayout

class SeaweedSimulatorGUI(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Seaweed Competition Simulation')
        self.setFixedSize(700, 400)  
        layout = QVBoxLayout()
        
        header = QLabel('<h2 style="color: green; text-align: center; line-height: 1">Seaweed Competition Simulation</h2>')
        layout.addWidget(header)
        
         # Timesteps Input
        timestepsLayout = QHBoxLayout()
        self.timestepsInput = QLineEdit(self)
        timestepsLayout.addWidget(QLabel('Time (Days):'))
        timestepsLayout.addWidget(self.timestepsInput)
        layout.addLayout(timestepsLayout)
        
        # Mode Dropdown
        modeLayout = QHBoxLayout()
        self.modeDropdown = QComboBox(self)
        self.modeDropdown.addItems(['None', 'Manual Removal', 'Collector Urchin','Removal + Urchin'])  # Add modes here
        self.frequencyInput = QLineEdit(self)
        self.percentInput = QLineEdit(self)
        modeLayout.addWidget(QLabel('Mode:'))
        modeLayout.addWidget(self.modeDropdown)
        modeLayout.addWidget(QLabel('Frequency:'))
        modeLayout.addWidget(self.frequencyInput)
        modeLayout.addWidget(QLabel('Percent:'))
        modeLayout.addWidget(self.percentInput)
        layout.addLayout(modeLayout)
        
         # Seaweed Species Dropdowns
        speciesLayout = QHBoxLayout()
        self.species1Dropdown = QComboBox(self)
        self.species1Dropdown.addItems(['Gracilaria salicornia', 'Kappaphycus alvarezii','Chondrus crispus','Pterocladiella capillacea'])  # Add seaweed species here
        speciesLayout.addWidget(QLabel('Seaweed Species 1:'))
        speciesLayout.addWidget(self.species1Dropdown)
        
        self.species2Dropdown = QComboBox(self)
        self.species2Dropdown.addItems(['Gracilaria salicornia', 'Kappaphycus alvarezii','Chondrus crispus','Pterocladiella capillacea'])  # Add seaweed species here
        speciesLayout.addWidget(QLabel('Seaweed Species 2:'))
        speciesLayout.addWidget(self.species2Dropdown)
        
        layout.addLayout(speciesLayout)
        
       # Size Input
        sizeLayout = QHBoxLayout()
        self.sizeInput = QLineEdit(self)
        sizeLayout.addWidget(QLabel('Size:'))
        sizeLayout.addWidget(self.sizeInput)
        layout.addLayout(sizeLayout)
        
        # Start Simulation Button
        self.startButton = QPushButton('Start Simulation', self)
        self.startButton.clicked.connect(self.start_simulation)
        layout.addWidget(self.startButton)
        
        self.setLayout(layout)
    
    def start_simulation(self):
        agents = []
        timesteps = int(self.timestepsInput.text())
        mode = self.modeDropdown.currentText()
        species1 = self.species1Dropdown.currentText()
        species2 = self.species2Dropdown.currentText()
        freq = int(self.frequencyInput.text())
        percent = int(self.percentInput.text())
        size = float(self.sizeInput.text())
        print(f"Starting simulation with: Timesteps: {timesteps}, Mode: {mode}, Species 1: {species1}, Species 2: {species2}, Size: {size}")
        if species1 == 'Gracilaria salicornia':
            agents.append(seaweed('Gracilaria salicornia',1,0.61,196.57))
        if species2 == 'Gracilaria salicornia':
            agents.append(seaweed('Gracilaria salicornia',1,0.61,196.57))
        if species1 == 'Kappaphycus alvarezii':
            agents.append(seaweed('Kappaphycus alvarezii',1,0.70,190.60))
        if species2 == 'Kappaphycus alvarezii':
            agents.append(seaweed('Kappaphycus alvarezii',1,0.70,190.60))
        if species1 == 'Chondrus crispus':
            agents.append(seaweed('Chondrus crispus',1,1.86,137.00))
        if species2 == 'Chondrus crispus':
            agents.append(seaweed('Chondrus crispus',1,1.86,137.00))
        if species1 == 'Pterocladiella capillacea':
            agents.append(seaweed('Pterocladiella capillacea',1,2.35,40.00))
        if species2 == 'Pterocladiella capillacea':
            agents.append(seaweed('Pterocladiella capillacea',1,2.35,40.00))
            

        sim(timesteps, mode, size,agents,freq,percent)


# simulation logic
#------------------------
# parameters
# t is the maximum number of timesteps you want to simulate in days
# mode is the types of population controls you want to impose on N2 (species 2 of seaweed)
# size is the maximum amount of space the two seaweeds have to grow into (the combined size of both has to be less than size)
#---------------------------

def sim(t,mode,size,agents,freq,percent):
    days = 0
    lastState = True
    x = size
    xaxis = []  #sets up an array to capture timesteps as we move through the simulation
    N1Trace = []   # sets up an array to capture the values N1 biomass as we move through time 
    N2Trace = []    # sets up an array to capture the values N2 biomass as we move through time
    N1 = agents[0]
    N2 = agents[1]
    adjValue = 0
    lastgrown = 0
    firstTime = True
    notAdjusted = True 
    
    while days < t:
        leftToGrow = ((N1.currentSize + N2.currentSize) < x) # checks at each timestep to see if there is room left to grow
        print(leftToGrow,days,lastgrown)
        if lastState == True and leftToGrow == False:
            if firstTime == True:
                print("First Time True to False Change")
                lastgrown = (days-1)
                print(lastgrown)
            else:
                print("Incrimenting lastgrown...")
                lastgrown += 1
                print(lastgrown)
        if lastState == True and leftToGrow == True:
            print("Incrimenting lastgrown...")
            lastgrown += 1
            
        if lastState == False and leftToGrow == True:
            print((N1.currentSize + N2.currentSize))
            if firstTime == True:
                print("First Time False to True Change")
                firstTime = False
                lastgrown += 1
                print(lastgrown)
            adjValue = lastgrown
       
        if lastState == True and leftToGrow == True: 
            print((N1.currentSize + N2.currentSize))
            if firstTime == True:
                adjValue = days
                
        if (mode == 'Manual Removal' or mode == 'Removal + Urchin') and days%freq == 0:
            N2.remove(percent)
        if mode == 'Collector Urchin':
            if notAdjusted:
                N1.adjSGR()
                N2.adjSGR()
                notAdjusted = False
        if mode == 'Removal + Urchin':
            if notAdjusted:
                N1.adjSGR()
                N2.adjSGR()
                notAdjusted = False
            
        if N1.currentSize < N1.maxSize: 
            if leftToGrow:
                N1x = N2.relativeX(x)
                N1.update(adjValue,N1x)
            
        if N2.currentSize < N2.maxSize: 
            if leftToGrow:
                N2x = N1.relativeX(x)
                N2.update(adjValue,N2x)
           
        
        N1Trace.append(N1.currentSize)
        N2Trace.append(N2.currentSize)
        xaxis.append(days)
        lastState = leftToGrow
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

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SeaweedSimulatorGUI()
    window.show()
    sys.exit(app.exec_())

#sim(120,'none',400)