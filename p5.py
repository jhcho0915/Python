# p5.py: More Data Mining
# Created By: Jae Cho
# E-mail: jhcho@email.wm.edu
#
# Data mining is the process of sorting through large amounts of data and
# picking out relevant information. It is usually used by business intelligence
# organizations, and financial analysts, but is increasingly being used in the
# sciences to extract information from the enormous data sets generated by
# modern experimental and observational methods.
#
# This project performs some preliminary data mining on the prices of some
# company's stock, in particular Google and/or Cisco. The program will gather
# information from the Google or Cisco stock files and organize it by month
# and within each month by day. The files are called Google.csv and Cisco.csv
# and are in comma-separated format.

def processDataFileforDict(filename) :
    '''This procedure processes through the data file, ultimately creating a 
    dictionary. It asks the user for the name of the data file for use.'''
    
    # Open data file
    dataFile = open(filename, "r")
    mainDict = {}
    innerDict= {}
    count = 0
    # Create lists and variables
    volumeList = []
    highList = []
    lowList = []
    tup = ()
    date = " "
    
    # Read the data file by line and skip the header
    for line in dataFile:
        if line [0:7]  == 'Date' or 'Close' in line:
            continue
        # Divide the data by comma and hyphen to create lists
        lineList = line.strip().split(",")
        date = lineList [0]
        lineList[0] = lineList[0].split("-")
        year = int(lineList[0][0])
        month = int(lineList[0][1])
        day = int(lineList[0][2])
        
        openValue = "{:.2f}".format(float(lineList[1]))
        highValue = "{:.2f}".format(float(lineList[2]))
        lowValue = "{:.2f}".format(float(lineList[3]))
        closeValue = "{:.2f}".format(float(lineList[4]))
        volume = int(float(lineList[5]))
        adjCloseValue = "{:.2f}".format(float(lineList[6]))
        stockValues = [openValue, highValue, lowValue, closeValue, volume, \
                       adjCloseValue]
        
        # Set tuple for year and month in dictionary
        if count != 0:
            if month != tup[1]:
                mainDict[tup] = (innerDict)
                innerDict = {}
                tup = (year, month)
        
        innerDict[day] = stockValues
        tup = (year, month)
        
        # Create tuples and append
        tupl = (int(volume), date)
        volumeList.append(tupl)
        tupl = (float(highValue), date)
        highList.append(tupl)
        tupl = (float(lowValue), date)
        lowList.append(tupl)
        count += 1
        
    dataFile.close()
    
    data = {"mainDict":mainDict, "volumeList":volumeList, "highList":highList,\
"lowList":lowList}
    
    return data
    
    
################################################################################
def getParticularDay (mainDict, listOfMonths) :
    '''This procedure prints the information about a particular day.
    It then passes to the procedure the main dictionary. The user will then 
    enter the year, month and day (in that order, three prompts). With the year
    and month, create a tuple for the key. From the dictionary, this proecudre
    pulls out the value for this key.'''
    
    # Prompt user to input year, month, and day in order
    year = int(input("Please enter the year you are interested in: "))
    print (year)
    actualYear = str(year)
    month = int(input("Please enter the month you are interested in: "))
    print (month)
    day = int(input("Please enter the day you are interested in: "))
    actualDay = str(day)
    print (day)
    key = year, month
    
    try:
        key in mainDict
        day in mainDict[key]
        stock_vol = mainDict[key][day]
        print ("\n" + listOfMonths [month -1] + " " + actualDay + "," + " " + \
               actualYear)
        print ("   {:10}{:10}{:10}{:10}{:13}{:10}".format("Open", "High",\
"Low", "Close", "Volume", "Adj. Close"))
        print ("   {:10}{:10}{:10}{:10}{:7,}{:>10}".format(stock_vol[0],\
stock_vol[1], stock_vol[2], stock_vol[3], stock_vol[4], stock_vol[5]))
    except KeyError:
        print ("\nNo trading occured on this day.")
        
        
################################################################################        
def getAveragePrice (mainDict, listOfMonths) :
    '''This procedure finds out information about a particular month. It then
    passes the main dictionary into this procedure. The procedure asks the user
    to enter the year and month (in that order). Create a tuple of this info-
    rmation for the key and pull out the inner dictionary for this month.'''
    
    year = int(input("Please enter the year you are interested in: "))
    print (year)
    month = int(input("Please enter the month you are interested in: "))
    print (month)
    
    # Initialize variabels for average calculation
    totalSum = 0
    totalVolume = 0
    actualMonth = listOfMonths [month - 1]
    actualYear = str(year)
    
    try:
        for value in mainDict [year, month].values() :
            totalSum += float(value[3]) * float(value[4])
            totalVolume += float (value[4])
        averagePrice = totalSum / totalVolume
        prettyPrice = " {:.2f}".format(averagePrice)
        
        print ("\nThe average price for " + actualMonth + " " + actualYear + \
               " is" + prettyPrice + ".")
    except KeyError:
        print ("\nNot a legal date")
            

###############################################################################
def printHighLowInformation (listOfMonths, volumeList, highList, lowList) :
        '''This procedure prints out the highest and lowest trading volume days,
        the highest price achieved and the lowest price achieved.'''
        
        # Prompts maximum trading volume in the list with date
        maxVolumeTuple = max(volumeList)
        maxVolume = maxVolumeTuple[0]
        dateOccurs = maxVolumeTuple[1].split("-")
        year = dateOccurs [0]
        month = listOfMonths[int(dateOccurs[1])-1]
        
        if int(dateOccurs[2]) < 10 :
            day = dateOccurs[2].replace("0", " ")
        day = dateOccurs[2]
        print ("The day with the highest trading volume was on "+ month + " "\
               + day + ", " + year + " which was " "{:,}".format(maxVolume) +\
               " shares.")
        
        # Prompts minimum trading volume in the list with date
        minVolumeTuple = min(volumeList)
        minVolume = minVolumeTuple[0]
        dateOccurs = minVolumeTuple[1].split("-")
        year = dateOccurs [0]
        month = listOfMonths[int(dateOccurs[1])-1]
        
        if int(dateOccurs[2]) < 10:
            day = dateOccurs[2].replace("0", " ")
        day = dateOccurs[2]
        print("The day with the lowest trading volume was on " + month + " " + \
              day + ", " + year + " which was " "{:,}".format(minVolume) + \
              " shares.")
        
        # Prompts highest value with date
        highListTuple = max(highList)
        maxValue = "{:.2f}".format(highListTuple[0])
        dateOccurs = highListTuple[1].split ("-")
        year = dateOccurs[0]
        month = listOfMonths[int(dateOccurs[1])-1]
        if int(dateOccurs[2]) < 10 :
            day = dateOccurs[2].replace("0", "")
        print ("The day with the highest value was on " + month + " " + day +\
               ", " + year + " which was " + maxValue + ".")
        
        # Prompts lowest value with date
        lowListTuple = min(lowList)
        minValue = "{:.2f}".format(lowListTuple[0])
        dateOccurs = lowListTuple[1].split ("-")
        year = dateOccurs[0]
        month = listOfMonths [int(dateOccurs[1]) -1]
        if int(dateOccurs[2]) < 10 :
            day = dateOccurs[2].replace("0", " ")
        day = dateOccurs [2]
        print ("The day with the lowest value was on " + month + " " + day +\
               ", " + year + " which was " + minValue + ".")
        
        
############################################################################### 
# Main Function

# Create a global lists of months. This will be used in outputting date
# information later and can be referenced from anywhere in the program.
listOfMonths = ["January", "February", "March", "April", "May", "June", "July",\
                "August", "September", "October", "November", "December"] 
choice = " "

# Prompt user to input the name of the file  
filename = input("Enter the name of the stock file: ")
print (filename + '\n')
    
data = processDataFileforDict(filename)

# Print a menu driven program that loops repeatedly until the user enters a 
# 'q' (or 'Q').
while choice != 'q':
    # Menu options
    print ("a) Get information about a particular day of trading")
    print ("b) Find average information about a particular month")
    print ("c) Print high/Low information")
    print ("q) Quit")
    print ()

    response = input("Enter choice: ")
    print (response)
    choice = response.lower()
    print ()

    if choice == "a":
        getParticularDay (data["mainDict"], listOfMonths)
        print()

    elif choice == "b":
        getAveragePrice (data["mainDict"], listOfMonths) 
        print()

    elif choice == "c":
        printHighLowInformation (listOfMonths, data["volumeList"],\
data["highList"], data["lowList"])
        print()
        
    elif choice == "q":
        print ("Thanks for using my program")
    
    else:
        print ("You've entered an incorrect choice. Try again")
