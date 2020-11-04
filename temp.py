"""
Author: Jun Fei Cheung
Studentid: s1719890
Last worked: 3-11-2020
"""
import numpy as np
import random

def findPath(listOfCoordinates):
        totalDistance = 0
        # Determine what would be the fastest way, first stone1 or stone2
        # steps from start to stone1
        stepStone = listOfCoordinates[0][0] + listOfCoordinates[0][1]
        # steps from start to stone2
        stepStone1 = listOfCoordinates[1][0] + listOfCoordinates[1][1]

        # The stone with least steps taken comes first in the list
        if stepStone <= stepStone1:
            print("Stone1 at location " + str(listOfCoordinates[0]) + " is the shortest.")
            totalDistance = stepStone
        else:
            listOfCoordinates.reverse()
            print("Stone2 at location " + str(listOfCoordinates[0]) + " is the shortest.")
            totalDistance = stepStone1
        print(f"list of coordinates:  {listOfCoordinates} \n")
        # Travel the coordinates and keep track of your route
        # Travel from point (0,0) to stone1
        path = [[0,0]]
        point = [0,0]
        while listOfCoordinates[0] != point:
            if  point[0] != listOfCoordinates[0][0]:
                point[0] = point[0] + 1
                path.append([point[0],point[1]])
            else:
                if point[1] != listOfCoordinates[0][1]:
                    point[1] = point[1] + 1
                    path.append([point[0],point[1]])

        # Travel to stone2, through x axis
        xDiff = listOfCoordinates[1][0] - listOfCoordinates[0][0]
        if xDiff > 0:
            for i in range (xDiff):
                point[0] = point[0] + 1
                path.append([point[0],point[1]])
        else:
            for i in range (-xDiff):
                point[0] = point[0] - 1
                path.append([point[0],point[1]])
            xDiff = xDiff * - 1

        # Travel to stone2, through y axis
        yDiff = listOfCoordinates[1][1] - listOfCoordinates[0][1]
        if yDiff > 0:
            for i in range (yDiff):
                point[1] = point[1] + 1
                path.append([point[0],point[1]])
        else:
            for i in range (-yDiff):
                point[1] = point[1] - 1
                path.append([point[0],point[1]])
            yDiff = yDiff * - 1
        totalDistance = totalDistance + xDiff + yDiff
        return path, totalDistance



def giveCoordinates(tupleArray):
    # x,y coordinates but reversed  [(1, 0), (2, 1)]
    reverse_listOfCoordinates = list(zip(tupleArray[0], tupleArray[1]))

    # making it x,y coordinates and in a list  [[0, 1], [1, 2]]
    listOfCoordinates = []
    for coordinate in reverse_listOfCoordinates:
        listOfCoordinates.append(list(coordinate[::-1]))
    return listOfCoordinates



def find_stone(moon):
    return(np.where(moon == 1))



def getMoon():
    moonSize = input("On what moon size do you want your robot to search (5, 6, 7 or 8)? ")
    try:
        moonSize = int(moonSize)
        if moonSize in [5, 6, 7, 8]:
            moon = np.zeros((moonSize, moonSize))
            while moon[0, 0] == 1 or ((moon == 1).sum() < 2):
                moon[0, 0] = 0
                moon[random.randint(0, moonSize-1), random.randint(0, moonSize-1)] = 1
            return moonSize, moon
        else:
            print("Your input is invalid!")
            return getMoon()
    except:
        print("Your input is invalid!")
        return getMoon()


def printResult(moon, fastestPath, totalDistance):
    #Print your route as well as the length of your travels
    print(fastestPath)
    print(f"The shortest path to get both stones is {totalDistance} steps \n")

    moon = moon.astype('str')
    for path in fastestPath:
        moon[path[1], path[0]] = " X "
    print(moon)



def main():
    moonSize, moon = getMoon()
    print(moon)

    # Find the location of both stones
    # coordinates as in (row,column)
    #(array([1, 4], dtype=int64), array([0, 0], dtype=int64))
    tupleArray = find_stone(moon)

    # Give coordinates of the stones
    listOfCoordinates = giveCoordinates(tupleArray)

    # Find fastest path
    fastestPath, totalDistance = findPath(listOfCoordinates)

    # print Result of path and how many steps needed to take
    printResult(moon, fastestPath, totalDistance)



# This makes sure that the program start running with the main() function
if __name__ == "__main__":
    main()
