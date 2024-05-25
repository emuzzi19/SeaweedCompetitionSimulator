# Seaweed Competition Simulator

## Introduction

The Seaweed Competition Simulator is an agent-based model designed to simulate the competition between different seaweed species for space. This project was developed as a final project for BIO247 and is inspired by the real-life scenario of invasive seaweed species in Hawaii.

## Table of Contents

- [Introduction](#introduction)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Methods](#methods)
- [Results](#results)
- [Discussion](#discussion)
- [References](#references)

## Installation

To install the necessary dependencies for running the Seaweed Competition Simulator, you can use the following commands:

```bash
# Clone the repository
git clone <repository-url>
```
# Navigate to the project directory
cd seaweed-competition-simulator

# Install the required Python packages
pip install -r requirements.txt


#Usage

To run the Seaweed Competition Simulator, execute the following command:
```
python sim.py
```
## Project Structure

    -seaweed.py: Contains the Seaweed class and related functions.
    -sim.py: Contains the GUI and simulation logic.
    -requirements.txt: Lists the Python dependencies for the project.
    -README.md: This README file.
    -DataAnalysis.pdf: The results of running the simulation to answer my research objectives
    -Documentation.pdf: A coding document to explain the functions and classes of the program
    
## Methods

The simulation is based on the Bio-Economic Seaweed Model (BESeM) equations. It simulates the growth of two seaweed species competing for limited space. The key components of the simulation include:

    -Seaweed Agents: Each seaweed agent is characterized by its name, initial size, growth rate, and maximum size.
    -Growth Equation: The weight of the seaweed over time is calculated using a logistic growth model.
    -Population Control Modes: The simulation includes different population control methods such as manual removal, the introduction of collector urchins, and a combination of both.

## Results

The results of the simulation demonstrate how different population control methods impact the competition between seaweed species. Key findings include:

    -High-frequency, low-percentage removal is more effective in supporting native species.
    -The introduction of collector urchins reduces the growth rate of invasive species.
    -Combining manual removal with collector urchins provides the most significant control over invasive species.

## Discussion

The simulation reveals that less aggressive but more frequent removal strategies are more effective for population control. The combination of manual removal and natural predation by collector urchins shows promising results in maintaining the balance between native and invasive species.

## References

For more detailed information, please refer to the documentation and final paper included in the project repository. 
