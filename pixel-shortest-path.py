from cv2 import cv2
import numpy as np
import sys
np.set_printoptions(threshold = sys.maxsize) #Allows the full matrix to be displayed if needed

image = input("Type file name with file extension of image you'd like to test:")
greyImage = cv2.imread(image,0) #Saves the grey image input by the user to greyImage

while(greyImage is None): #If the user inputs an incorrect file name
    image = input("The file you selected does not exist. Please type a file name with extension you'd like to test:")
    greyImage = cv2.imread(image, 0)  #Saves the grey image input by the user to greyImage

greyImageWidth = greyImage.shape[1] #Saves the number of horizontal pixels to greyImageWidth
greyImageHeight = greyImage.shape[0] #Saves the number of vertical pixels to greyImageHeight

#Initializes the V set. User inputs numbers between 0 and 255 one at a time until 'Done' is typed
V = set([])
vCheck = 0
while(vCheck == 0):
    vInput = input("Type a value between 0 and 255 to be included in set V. Type 'Done' when no more values need to be added:")
    try:
        vInput = int(vInput) #Converts user input into an integer
        if(vInput >= 0 and vInput <= 255):
            V.add(vInput)
            print("Set V contains:")
            print(V)
        else:
            print("The entered value was above 255 or less than 0. ")
    except ValueError:
        if(vInput == 'Done'):
            vCheck = 1
        else:
            print("The entered character was not an integer")

#Initializes the x and y pixel coordinates for p. If user input is not within pixel space or not an integer, an error is thrown and user is asked to input again.
xpCheck = 0
while(xpCheck == 0):
    xpStart = input("Enter a valid x coordinate for p:")
    try:
        xpStart = int(xpStart)
        if(xpStart < greyImageWidth and xpStart >= 0):
            xpCheck = 1
        else:
            print("The entered character was too large or less than 0. ")
    except ValueError:
        print("The entered character was not an integer. ")

ypCheck = 0
while(ypCheck == 0):
    ypStart = input("Enter a valid y coordinate for p:")
    try:
        ypStart = int(ypStart)
        if(ypStart < greyImageHeight and ypStart >= 0):
            ypCheck = 1
        else:
            print("The entered character was too large or less than 0. ")
    except ValueError:
        print("The entered character was not an integer. ")

#Initializes the x and y pixel coordinates for q. If user input is not within pixel space or not an integer, an error is thrown and user is asked to input again.
xqCheck = 0
while(xqCheck == 0):
    xqEnd = input("Enter a valid x coordinate for q:")
    try:
        xqEnd = int(xqEnd)
        if(xqEnd < greyImageHeight and xqEnd >= 0):
            xqCheck = 1
        else:
            print("The entered character was too large or less than 0. ")
    except ValueError:
        print("The entered character was not an integer. ")

yqCheck = 0
while(yqCheck == 0):
    yqEnd = input("Enter a valid y coordinate for q:")
    try:
        yqEnd = int(yqEnd)
        if(yqEnd < greyImageHeight and yqEnd >= 0):
            yqCheck = 1
        else:
            print("The entered character was too large or less than 0. ")
    except ValueError:
        print("The entered character was not an integer. ")

pathCheck = 0
while(pathCheck == 0):
    print("1 - 4-path")
    print("2 - 8-path")
    print("3 - m-path")
    path = input("Type a number for the pixel neighbor relationship you'd like to select:")
    try:
        path = int(path)
        if(path <= 3 and path >= 1):
            pathCheck = 1
        else:
            print("The entered character was not a valid option. ")
    except ValueError:
        print("The entered character was not an integer. ")

xPosition = 0
yPosition = 0

#List used to track x and y pixel coordinates that have intensities in set V
xyList = []

matrix = np.zeros(shape=(greyImageHeight,greyImageWidth)) #Creates matrix to evaluate set of pixels with intensities contained within set V

while(xPosition < greyImageWidth): #Loops through each row
    while(yPosition < greyImageHeight): #Loops through each column

        centerPixel = int(greyImage[yPosition, xPosition]) #Sets centerPixel to number for the intensity for the current x and y pixel position

        #If the current pixel intensity in centerPixel is not in set V, set the value at the same x and y pixel position in the matrix to 0.
        #Otherwise, set the value in the matrix to 999 and add the current x and y positions to their lists.
        if(centerPixel not in V):
            matrix[yPosition][xPosition] = 0
        else:
            xyList.append([xPosition,yPosition])
            matrix[yPosition][xPosition] = 999

        yPosition = yPosition + 1 #Increment Y position by 1

    yPosition = 0
    xPosition = xPosition + 1 #Increment X position by 1

#Evaluation begins by setting the beginning pixel position to the user inputs for the x and y coordinates of p.
xp = xpStart
yp = ypStart

listLength = len(xyList)
listSearch = 0

#The following functions are used to check if the pixel locations in the matrix for p and q are valid and if p and q match.
searchComplete = 0
pqMatch = 0
if(matrix[ypStart][xpStart] == 0):
    searchComplete = 1
if(matrix[yqEnd][xqEnd] == 0):
    searchComplete = 1
if(xpStart == xqEnd and ypStart == yqEnd and matrix[ypStart][xpStart] == 999):
    pqMatch = 1
    searchComplete = 1

#Since the position for p is initialed with 0 in the matrix, stepCount is used to mark any vaild neighbors with 1 + the current pixel location value in the matrix
#if the neighbor's current value is greater than the value of stepCount
matrix[yp][xp] = 0
stepCount = 1

if(path == 1): #If the user selected '4- path'
    while(searchComplete == 0):

        #The following functions check to see if the neighbor is valid and the current value is greater than stepCount.
        #If so, reassign the value of the neighbor to stepCount.
        if(yp - 1 >= 0 and matrix[yp - 1][xp] > stepCount):
                matrix[yp - 1][xp] = stepCount

        if (xp + 1 < greyImageWidth and matrix[yp][xp + 1] > stepCount):
                matrix[yp][xp + 1] = stepCount

        if (yp + 1 < greyImageHeight and matrix[yp + 1][xp] > stepCount):
                matrix[yp + 1][xp] = stepCount

        if (xp - 1 >= 0 and matrix[yp][xp - 1] > stepCount):
                matrix[yp][xp - 1] = stepCount

        #The following function removes the current x and y coordinates for the currrent pixel position from the xyList since its neighbors have been evaluated
        removalComplete = 0
        listLength = len(xyList)
        listSearch = 0

        while(removalComplete == 0 and listSearch < listLength):
            if(xyList[listSearch][0] == xp and xyList[listSearch][1] == yp):
                xyList.pop(listSearch)
                removalComplete = 1
            else:
                listSearch = listSearch + 1

        listLength = len(xyList)
        listSearch = 0

        #The following function evaluates the xyList to determine if the coordinates of xq and yq are still in the list. If not, the search is complete
        searchComplete = 1
        while(listSearch < listLength):
            if(xyList[listSearch][0] == xqEnd and xyList[listSearch][1] == yqEnd):
                searchComplete = 0
            listSearch = listSearch + 1

        #The following function is a comparison between the matrix equivalents of the coordinates remaining in the xyList and the current matrixValue
        #If the evaluated matrix value in the matrix coordinate is less than the current matrixValue, that coordinate becomes the next xp and yp to be evaluated.
        matrixValue = 999
        listLength = len(xyList)
        listSearch = 0

        while (listSearch < listLength):
            if (int(matrix[xyList[listSearch][1]][xyList[listSearch][0]]) < matrixValue and int(matrix[xyList[listSearch][1]][xyList[listSearch][0]]) > 0):
                matrixValue = int(matrix[xyList[listSearch][1]][xyList[listSearch][0]])
                xp = xyList[listSearch][0]
                yp = xyList[listSearch][1]
                stepCount = matrixValue + 1

            listSearch = listSearch + 1

        if (listSearch == listLength and matrixValue == 999): #If the list has been fully evaluated and the largest value remaining in the matrix is 999, the search is complete
            searchComplete = 1

if(path == 2): #If the user selected '8-path'
    while (searchComplete == 0):

        # The following functions check to see if the neighbor is valid and the current value is greater than stepCount.
        # If so, reassign the value of the neighbor to stepCount.
        if (yp - 1 >= 0 and matrix[yp - 1][xp] > stepCount):
                matrix[yp - 1][xp] = stepCount

        if (xp + 1 < greyImageWidth and matrix[yp][xp + 1] > stepCount):
                matrix[yp][xp + 1] = stepCount

        if (yp + 1 < greyImageHeight and matrix[yp + 1][xp] > stepCount):
                matrix[yp + 1][xp] = stepCount

        if (xp - 1 >= 0 and matrix[yp][xp-1] > stepCount):
                matrix[yp][xp - 1] = stepCount

        if (yp - 1 >= 0 and xp - 1 >= 0 and matrix[yp - 1][xp - 1] > stepCount):
                matrix[yp - 1][xp - 1] = stepCount

        if (yp - 1 >= 0 and xp + 1 < greyImageWidth and matrix[yp - 1][xp + 1] > stepCount):
                matrix[yp - 1][xp + 1] = stepCount

        if (yp + 1 < greyImageHeight and xp + 1 < greyImageWidth and matrix[yp + 1][xp + 1] > stepCount):
                matrix[yp + 1][xp + 1] = stepCount

        if (yp + 1 < greyImageHeight and xp - 1 >= 0 and matrix[yp + 1][xp - 1] > stepCount):
                matrix[yp + 1][xp - 1] = stepCount

        # The following function removes the current x and y coordinates for the currrent pixel position from the xyList since its neighbors have been evaluated
        removalComplete = 0
        listLength = len(xyList)
        listSearch = 0

        while(removalComplete == 0 and listSearch < listLength):
            if(xyList[listSearch][0] == xp and xyList[listSearch][1] == yp):
                xyList.pop(listSearch)
                removalComplete = 1
            else:
                listSearch = listSearch + 1

        listLength = len(xyList)
        listSearch = 0

        #The following function evaluates the xyList to determine if the coordinates of xq and yq are still in the list. If not, the search is complete
        searchComplete = 1
        while(listSearch < listLength):
            if(xyList[listSearch][0] == xqEnd and xyList[listSearch][1] == yqEnd):
                searchComplete = 0
            listSearch = listSearch + 1

        #The following function is a comparison between the matrix equivalents of the coordinates remaining in the xyList and the current matrixValue
        #If the evaluated matrix value in the matrix coordinate is less than the current matrixValue, that coordinate becomes the next xp and yp to be evaluated.
        matrixValue = 999
        listLength = len(xyList)
        listSearch = 0

        while (listSearch < listLength):
            if (int(matrix[xyList[listSearch][1]][xyList[listSearch][0]]) < matrixValue and int(matrix[xyList[listSearch][1]][xyList[listSearch][0]]) > 0):
                matrixValue = int(matrix[xyList[listSearch][1]][xyList[listSearch][0]])
                xp = xyList[listSearch][0]
                yp = xyList[listSearch][1]
                stepCount = matrixValue + 1

            listSearch = listSearch + 1

        if (listSearch == listLength and matrixValue == 999):
            searchComplete = 1

if(path == 3): #If the user selected 'm-path'
    while (searchComplete == 0):

        # The following functions check to see if the neighbor is valid and the current value is greater than stepCount.
        # If so, reassign the value of the neighbor to stepCount.
        fourCheck = 0 #Used to check if any of the '4-path' directions have been evaluated
        if (yp - 1 >= 0 and matrix[yp - 1][xp] > stepCount):
                matrix[yp - 1][xp] = stepCount
                fourCheck = 1

        if (xp + 1 < greyImageWidth and matrix[yp][xp + 1] > stepCount):
                matrix[yp][xp + 1] = stepCount
                fourCheck = 1

        if (yp + 1 < greyImageHeight and matrix[yp + 1][xp] > stepCount):
                matrix[yp + 1][xp] = stepCount
                fourCheck = 1

        if (xp - 1 >= 0 and matrix[yp][xp-1] > stepCount):
                matrix[yp][xp-1] = stepCount
                fourCheck = 1

        if (yp - 1 >= 0 and xp - 1 >= 0 and fourCheck == 0 and matrix[yp - 1][xp - 1] > stepCount):
                matrix[yp - 1][xp - 1] = stepCount

        if (yp - 1 >= 0 and xp + 1 < greyImageWidth and fourCheck == 0 and matrix[yp - 1][xp + 1] > stepCount):
                matrix[yp - 1][xp + 1] = stepCount

        if (yp + 1 < greyImageHeight and xp + 1 < greyImageWidth and fourCheck == 0 and matrix[yp + 1][xp + 1] > stepCount):
                matrix[yp + 1][xp + 1] = stepCount

        if (yp + 1 < greyImageHeight and xp - 1 >= 0 and fourCheck == 0 and matrix[yp + 1][xp - 1] > stepCount):
                matrix[yp + 1][xp - 1] = stepCount

        # The following function removes the current x and y coordinates for the currrent pixel position from the xyList since its neighbors have been evaluated
        removalComplete = 0
        listLength = len(xyList)
        listSearch = 0

        while(removalComplete == 0 and listSearch < listLength):
            if(xyList[listSearch][0] == xp and xyList[listSearch][1] == yp):
                xyList.pop(listSearch)
                removalComplete = 1
            else:
                listSearch = listSearch + 1

        listLength = len(xyList)
        listSearch = 0

        #The following function evaluates the xyList to determine if the coordinates of xq and yq are still in the list. If not, the search is complete
        searchComplete = 1
        while(listSearch < listLength):
            if(xyList[listSearch][0] == xqEnd and xyList[listSearch][1] == yqEnd):
                searchComplete = 0
            listSearch = listSearch + 1

        #The following function is a comparison between the matrix equivalents of the coordinates remaining in the xyList and the current matrixValue
        #If the evaluated matrix value in the matrix coordinate is less than the current matrixValue, that coordinate becomes the next xp and yp to be evaluated.
        matrixValue = 999
        listLength = len(xyList)
        listSearch = 0

        while (listSearch < listLength):
            if (int(matrix[xyList[listSearch][1]][xyList[listSearch][0]]) < matrixValue and int(matrix[xyList[listSearch][1]][xyList[listSearch][0]]) > 0):
                matrixValue = int(matrix[xyList[listSearch][1]][xyList[listSearch][0]])
                xp = xyList[listSearch][0]
                yp = xyList[listSearch][1]
                stepCount = matrixValue + 1

            listSearch = listSearch + 1

        if (listSearch == listLength and matrixValue == 999):
            searchComplete = 1


answer = int(matrix[yqEnd][xqEnd])
if(int(matrix[yqEnd][xqEnd]) == 999 or answer < 1 and pqMatch == 0):#If the value for q in the matrix is 999 or 0, q was not evaluated and there is no path between p and q
    print("The path does not exist between point p and point q")
else:#If q was evaluated, the path beween p and q is the value of q in the matrix
    print('The length of the shortest path is: ' + str(answer))

print(matrix)#Shows the evaluated matrix with 1 being the starting position and sequentially increasing with each neigboring pixel to q