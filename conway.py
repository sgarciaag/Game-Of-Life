"""
conway.py 
A simple Python/matplotlib implementation of Conway's Game of Life.
"""

import sys, argparse
import numpy as np
import matplotlib.pyplot as plt 
import matplotlib.animation as animation
import datetime
from patterns import *

ON = 255
OFF = 0
vals = [ON, OFF]

def randomGrid(width, height):
    """returns a grid of with*height random values"""
    return np.random.choice(vals, width*height, p=[0.2, 0.8]).reshape(width, height)

def addGlider(i, j, grid):
    """adds a glider with top left cell at (i, j)"""
    glider = np.array([[0,    0, 255], 
                       [255,  0, 255], 
                       [0,  255, 255]])
    grid[i:i+3, j:j+3] = glider

# read the input configuration file
def readFile():
    print("\n\n File input:")
    print("Choose the file you wish to read the data from: ")
    f = input("Write the name of file and extension: ")
    file = open(f, "r")
    text = file.read().split("\n")
    width = int(text[0].split(" ")[0])
    height = int(text[0].split(" ")[1])
    generations = int(text[1])
    grid = np.zeros(width * height).reshape(width, height)
    
    for line in text[2:]:
        line = line.split(" ")
        x = int(line[0])
        y = int(line[1])
        grid[x, y] = ON
    
    file.close()

    return grid, width, height, generations 

# input manual configuration
def manualConfig():
    print("\n\n Manual data input:")
    width = int(input("Width: ") or 30)
    height = int(input("Height: ") or 30)
    generations = int(input("generations: ") or 200)

    # declare grid
    grid = np.array([])
    # populate grid with random on/off - more off than on
    grid = randomGrid(width, height)
    return grid, width, height, generations



def update(frameNum, img, grid, width, height, generations):
    global countGen
    # copy grid since we require 8 neighbors for calculation
    # and we go line by line
    newGrid = grid.copy()
    # iterate over each cell in the grid
    for i in range(width):
        for j in range(height):
            # count the number of live neighbors
            neighbors = [(i-1, j-1), (i-1, j), (i-1, j+1), (i, j-1), (i, j+1), (i+1, j-1), (i+1, j), (i+1, j+1)]
            num_live_neighbors = sum([grid[x][y] == ON for x,y in neighbors if x >= 0 and x < width and y >= 0 and y < height])
            
            # apply the rules of the game of life
            if grid[i][j] == ON and (num_live_neighbors < 2 or num_live_neighbors > 3):
                newGrid[i][j] = OFF
            elif grid[i][j] == OFF and num_live_neighbors == 3:
                newGrid[i][j] = ON
    
    # update data
    img.set_data(newGrid)
    grid[:] = newGrid[:]

    # Report Generation
    totalBlocks = 0
    totalBlocks = findPattern(grid, blocks)

    totalBeehives = 0
    totalBeehives = findPattern(grid, beehives)

    totalLoaves = 0
    totalLoaves = findPattern(grid, loafs)

    totalBoats = 0
    totalBoats = findPattern(grid, boats)

    totalTubs = 0
    totalTubs = findPattern(grid, tubs)
    
    totalBlinkers = 0
    totalBlinkers = findPattern(grid, blinker1)
    totalBlinkers += findPattern(grid, blinker2)
    
    totalToads = 0
    totalToads = findPattern(grid, toad1)
    totalToads += findPattern(grid, toad2)

    totalBeacons = 0
    totalBeacons = findPattern(grid, beacon1)
    totalBeacons += findPattern(grid, beacon2)

    totalGliders = 0
    totalGliders =  findPattern(grid, glider1)
    totalGliders +=  findPattern(grid, glider2)
    totalGliders +=  findPattern(grid,  glider3)
    totalGliders +=  findPattern(grid, glider4)

    totalSpaceships = 0
    totalSpaceships = findPattern(grid, spaceship1)
    totalSpaceships += findPattern(grid, spaceship2)
    totalSpaceships += findPattern(grid, spaceship3)
    totalSpaceships += findPattern(grid, spaceship4)

    allPatterns = [totalBlocks, totalBeehives, totalLoaves, totalBoats, totalTubs, totalBlinkers, totalToads, totalBeacons, totalGliders, totalSpaceships]

    printReport(generations, allPatterns, width, height)
    countGen += 1

    return img,
    
def findPattern(grid, pattern):
    aux = pattern.copy()
    height, width = aux.shape
    counter = 0
    for i in range(grid.shape[0] - height + 1):
        for j in range (grid.shape[1] - width + 1):
            if np.all(grid[i:i+height, j:j+width] == aux):
                counter += 1
    return counter

def printReport(generations, allPatterns, width, height):
    global countGen
    date = str(datetime.date.today())

    outputFile = open("Final_Report5_"+date+".txt", "a")

    #Total patterns found
    total = 0
    for i in allPatterns:
        total += i

    #this total is needed so you don't divide by 0
    total4div = total
    if (total4div == 0):
        total4div = 1

    outputFile.write("Simulation at "+date+"\n")
    outputFile.write("Universe size "+str(width)+" x "+str(height)+"\n")
    outputFile.write("Iteration: "+str(countGen)+"\n")
    outputFile.write("+__________+________+__________+\n")
    outputFile.write("|          |  Count |  Percent |\n")
    outputFile.write("| Blocks   |  "+str(allPatterns[0])+"   |  "+str((allPatterns[0]/total4div)*100)+"      |\n")
    outputFile.write("| Beehives |  "+str(allPatterns[1])+"   |  "+str((allPatterns[1]/total4div)*100)+"      |\n")
    outputFile.write("| Loaves   |  "+str(allPatterns[2])+"   |  "+str((allPatterns[2]/total4div)*100)+"      |\n")
    outputFile.write("| Boats    |  "+str(allPatterns[3])+"   |  "+str((allPatterns[3]/total4div)*100)+"      |\n")
    outputFile.write("| Tubs     |  "+str(allPatterns[4])+"   |  "+str((allPatterns[4]/total4div)*100)+"      |\n")
    outputFile.write("| Blinkers |  "+str(allPatterns[5])+"   |  "+str((allPatterns[5]/total4div)*100)+"      |\n")
    outputFile.write("| Toads    |  "+str(allPatterns[6])+"   |  "+str((allPatterns[6]/total4div)*100)+"      |\n")
    outputFile.write("| Beacons  |  "+str(allPatterns[7])+"   |  "+str((allPatterns[7]/total4div)*100)+"      |\n")
    outputFile.write("| Gliders  |  "+str(allPatterns[8])+"   |  "+str((allPatterns[8]/total4div)*100)+"      |\n")
    outputFile.write("| SpcShips |  "+str(allPatterns[9])+"   |  "+str((allPatterns[9]/total4div)*100)+"      |\n")
    outputFile.write("+__________+________+__________+\n")
    outputFile.write("| Total    |  "+str(total)+"   |          |\n\n")
    

# main() function
def main():
    # Command line args are in sys.argv[1], sys.argv[2] ..
    # sys.argv[0] is the script name itself and can be ignored
    # parse arguments
    global countGen
    countGen = 0
    parser = argparse.ArgumentParser(description="Runs Conway's Game of Life system.py.")

    print("Select the option for your data: ")
    print("1.- Using an input file")
    print("2.- Input configuration manually")
    selection = int(input("[1 or 2]:"))
    if (selection == 1):
        grid, width, height, generations = readFile()
    elif(selection==2):
        grid, width, height, generations = manualConfig()
    else:
        grid, width, height, generations = manualConfig()
    # set animation update interval
    updateInterval = 50

    # set up animation
    fig, ax = plt.subplots()
    img = ax.imshow(grid, interpolation='nearest')
    ani = animation.FuncAnimation(fig, update, fargs=(img, grid, width, height, generations),
                                  frames = generations,
                                  interval = updateInterval,
                                  save_count=50, repeat = False)

    plt.show()

# call main
if __name__ == '__main__':
    main()