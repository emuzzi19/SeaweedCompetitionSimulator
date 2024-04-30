#imports
import matplotlib.pyplot as plt
from seaweed import seaweed


# create agents

N1 = seaweed('N1',10.86,0.098523,134.46)
N2 = seaweed('N2',10.86,0.108391,170.69)

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
        self.modeDropdown.addItems(['none', 'mode1', 'mode2'])  # Add your modes here
        modeLayout.addWidget(QLabel('Mode:'))
        modeLayout.addWidget(self.modeDropdown)
        layout.addLayout(modeLayout)
        
         # Seaweed Species Dropdowns
        speciesLayout = QHBoxLayout()
        self.species1Dropdown = QComboBox(self)
        self.species1Dropdown.addItems(['N1', 'N2'])  # Add your seaweed species here
        speciesLayout.addWidget(QLabel('Seaweed Species 1:'))
        speciesLayout.addWidget(self.species1Dropdown)
        
        self.species2Dropdown = QComboBox(self)
        self.species2Dropdown.addItems(['N1', 'N2'])  # Add your seaweed species here
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
        timesteps = int(self.timestepsInput.text())
        mode = self.modeDropdown.currentText()
        species1 = self.species1Dropdown.currentText()
        species2 = self.species2Dropdown.currentText()
        size = float(self.sizeInput.text())
        print(f"Starting simulation with: Timesteps: {timesteps}, Mode: {mode}, Species 1: {species1}, Species 2: {species2}, Size: {size}")
        sim(timesteps, mode, size)


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

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SeaweedSimulatorGUI()
    window.show()
    sys.exit(app.exec_())

#sim(120,'none',400)