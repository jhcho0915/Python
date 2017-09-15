# p4.py: Data Mining
# Created by: Jae Cho
#
# This program prompts the user to input the name of a datafile, in particular
# Google and Cisco. The program calculates the monthly average prices of the 
# company's stock and reports the six best and the six worst months for that
# stock. In addition the program also calculates some high and low statistics
# for the stock price and the stock volume. The Google data covers August 2004
# to March 2013, while the Cisco stock covers March 1990 to September 2015.

def open_dataFile (filename) :
    '''This procedure opens the data file for reading. It then reads the first\
    line of the file and throws away the column header information.'''
    dataFile = open (filename, "r")
    dataList = []
    
    for line in dataFile:
        if line[0:7] == "Date" or "Close" in line:
            continue
        lineList = line.strip().split(",")  # Strip and split after punctuation
        stockList = [lineList[0], float(lineList[4]), int (lineList[5]), \
                      float(lineList[2]), float(lineList[3])]
        dataList.append(stockList)
    dataFile.close()           # Close the dataFile 
    return dataList

def get_monthly_averages (dataList) :
    '''This function receives the dataList generated above as a parameter. The\
    program calculates the average monthly prices using the Date, Volume, and\
    Close fields'''
    
    # The program receives each monthly average stock and dates through a list.
    newStockList = []
    for stockList in dataList:
        # Divide the dates in dataList 
        stockList [0] = stockList [0].split ("-")
        stockList [0][0] = int (stockList [0][0])
        stockList [0][1] = int (stockList [0][1])
        stockList [0][2] = int (stockList [0][2])
        newStockList.append(stockList) #Append to the new list
    
    # Create and initialize variables for calculating monthly average stocks    
    runningTotal = 0
    daily_value = 0
    volumeTotal = 0
    monthlyAveragePrice = 0
    count = 0
    monthlyAverages = []   # New list for monthly averages
    
    # The program reads each line and adds up monthly prices and volumes
    for line in dataList:
        month = dataList [count-1][0][1]
        year = dataList [count-1][0][0]
        
        daily_value = line[1] * line[2]
        runningTotal += daily_value
        volumeTotal += line[2]
        
        # If the month in the line does not match previous line's month then 
        # the program calculates the previous and moves on to the next averages
        if count != 0:  
            if line[0][1] != dataList [count-1][0][1]:
                runningTotal -= daily_value
                volumeTotal -= line[2]
                averagePrice = runningTotal/volumeTotal   # Average Price
                monthlyAverages += [[averagePrice, (month, year)]]
                daily_value = line[1] * line[2]
                volumeTotal = line[2]
                runningTotal = daily_value
        count += 1
        
    averagePrice = runningTotal/ volumeTotal
    monthlyAverages += [[averagePrice, (month, year)]]    # Finish calculation
    
    return monthlyAverages

def print_info (monthlyAverages, name) :
    '''In this function, the program lists of monthly averages calculated\
    above. This procedure finds and prints the 6 best and 6 worst months for\
    the average stock price. '''
    
    # The program sorts the monthly average stock from high to low 
    monthlyAverages.sort(reverse = True)
    sixBestAvg = monthlyAverages[0:6]   # Find and use first six average prices
    print ("The six best months for", name, "stock are as follows: ")
    
    count = 0
    while count < 6:  
        year = str(monthlyAverages[count][1][1])  # Arrange year and then month 
        month = str(monthlyAverages[count][1][0])
        if len(month) < 2:
            month = "0" + month
        print (year + "-" + month + "   {:0.3f}".format(monthlyAverages\
                                                        [count][0]))
        count +=1   
    print ()
    
    # Orders the monthly average stock from low to high and takes first six
    monthlyAverages.sort()
    sixWorstAvg = monthlyAverages[0:6]
    print ("The six worst months for" , name, "stock are as follows: ")
    
    count = 0
    while count < 6:    # Format with year and then month 
        year = str (monthlyAverages[count][1][1])
        month = str (monthlyAverages[count][1][0])
        if len(month) < 2:
            month = "0" + month
        print (year + "-" + month + \
               "    {:0.3f}".format(monthlyAverages[count][0]))
        count += 1  
    print ()
    
def getHighestStock (dataList) :
    '''This procedure finds the day with the highest stock price'''
    for line in dataList:
        line[0], line[3] = line[3], line[0]
    
    highestDay = max (dataList)
    highestValue = str("{:0.2f}".format(highestDay[0]))
    day = str(highestDay[3][2])
    month = str(highestDay[3][1])
    year = str(highestDay[3][0])
    
    # Place 0 in front of months less than the months with doubles digits.
    if len(day) < 2:
        day = "0" + day
    if len(month) < 2:
        month = "0" + month
        
    date = year + "-" + month + "-" + day
    print ("The day when the stock reached its highest point was", date, \
           "with a value of", highestValue + ".")
            
def getLowestStock (dataList):
    '''This procedure finds the day with the lowest stock price'''
    for line in dataList:
        line[0], line[4] = line[4], line[0]
    
    lowestDay = min(dataList)
    lowestValue = str(lowestDay[0])
    day = str(lowestDay[3][2])
    month = str(lowestDay[3][1])
    year = str(lowestDay[3][0])
    
    # Place 0 in front of months less than the months with doubles digits.
    if len(day) < 2:
        day = "0" + day     # Add to day
    if len(month) < 2:
        month = "0" + month   # Add to month
    
    date = year + "-" + month + "-" + day 
    print ("The day when the stock reached its lowest point was", date, \
           "with a value of", lowestValue + ".")

def getHighestVolume (dataList):
    '''This procedure finds the day with the highest volume shares'''
    for line in dataList:
        line[0], line[2] = line[2], line[0]
    highestVolumeDay = max(dataList)
    highestVolume = int(highestVolumeDay[0])
    day = str(highestVolumeDay[3][2])
    month = str(highestVolumeDay[3][1])
    year = str(highestVolumeDay[3][0])
    
    # Place 0 in front of months less than the months with doubles digits.
    if len(day) < 2:
        day = "0" + day
    
    if len(month) < 2:
        month = "0" + month
        
    date = year + "-" + month + "-" + day
    print ("The day with the highest volume was", date, \
           "with a volume of", "{:,}".format(highestVolume) , "shares.")
    
def getLowestVolume (dataList):
    '''This procedure finds the day with the lowest volume shares'''
    lowestVolumeDay = min(dataList)
    lowestVolume = int(lowestVolumeDay[0])
    day = str(lowestVolumeDay[3][2])
    month = str(lowestVolumeDay[3][1])
    year = str(lowestVolumeDay[3][0])
    
    # Place 0 in front of months less than the months with doubles digits.
    if len (day) < 2:
        day = "0" + day
    if len (month) < 2:
        month = "0" + month
    
    date = year + "-" + month + "-" + day
    print ("The day with the lowest volume was", date, \
           "with a volume of", "{:,}".format (lowestVolume), "shares.")
    
#-------------------------------------------------------------------------------
#main function 
# This asks the user for the name of the external data file. Once the user
# enters that information the program calls a function to process the data, 
# ultimately creating a list which should be returned. 

filename = input ("\nEnter the name of the data file: ")
print (filename + "\n")
name = filename.replace(".csv", "'s")

# Run the procedures
dataList = open_dataFile (filename)
monthlyAverages = get_monthly_averages (dataList)
print_info (monthlyAverages, name)
getHighestStock (dataList)
getLowestStock (dataList)
getHighestVolume (dataList)
getLowestVolume (dataList)
