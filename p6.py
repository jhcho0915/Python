# p6.py Football
# Created by: Jae Cho
#
# The National Football League (NFL) is North America's professional league for
# men's football. This program helps to locate information about a particular
# NFL player.
# In football, the statistic for anyone who runs the ball is called the rusher
# rating. To calculate the rusher rating, four inputs are needed: rushing
# attempts, rushing yards, rushing touchdowns and fumbles. The algorithm
# consists of four steps:
#
# Yds is the average yards gained per attempt. This is [total yards /
# (4.05 * attempts)]. If this number is greater than 2.375, then 2.375 should
# be used instead.
#
# perTDs is the percentage of touchdowns per carry. This is [(39.5 * 
# touchdowns) / attempts]. If this number is greater than 2.375, then 2.375 
# should be used instead.
# perFumbles is the percentage of fumbles per carry. This is [2.375 - ((21.5 *
# fumbles) / attempts)].
#
# The rusher rating is [Yds + perTDs + perFumbles] * (100 / 4.5).
# This number can be negative if the player gets negative yardage or fumbles
# the ball often. The goal for this formula is to produce a scale of values 
# where the top rating is 158.3. The information about the players is kept on
# a yearly basis; therefore, a player may appear multiple times in the data.

# Import from the file Player.py
from Player import Player

def createPlayerDictionary (filename):
    '''This procedure creates one empty dictionary - the key is a player's
    name and the value will be a Player object (an object of the Player class 
    type). This then opens the data file for reading. The program reads the
    first line and throws away the column header information.'''
    players = {}
    
    dataFile = open (fileName, "r")
    dataFile.readline()
    
    for line in dataFile:
        # Divide the data by stripping and splitting by line and punctuation
        lineList = line.strip().split(",")
        name = "{} {}".format (lineList[0], lineList[1])
        player = Player (lineList[0], lineList[1])
        if name not in players:
            players[name] = player
        players[name].update (lineList[2], lineList[3], lineList[13], \
lineList[5], lineList[6], lineList[7], lineList[10])
    
    dataFile.close()
    return players

def printAlpha (players):
    '''This procedure creates an empty list. It then appends all the values
    (Player objects) to this list'''
    playerList = []
    # Create an empty list. Append all the values to this list.
    for val in players.values() :
        playerList.append(val)
        
    playerList.sort()
    
    for player in playerList:
        print (player)
        
def IndivPlayerInfo (players) :
    '''This procedure allows the user to enter a choice. If the choice is an 'a'
    (or 'A'), it print the player's information. If the choice is a 'b'
    (or 'B'), call a different method in the Player class which prints all
    years' information about his player.'''
    
    # Prompt user to answer if interested in particular player
    response = input("\nDo you want information about a particular player? ")
    answer = response.lower()
    
    while answer == "y":
        print (response)
        print()
        try:
            name = input ("Enter player's name: ")
            print (name)
            
            player = players[name]
            
            response = input ("\nPick one\na) Overall rusher rating\n" "b) \
Individual years and ratings\n\nEnter choice: ")
            
            choice = response.lower()
            print (choice + "\n")
            
            if choice == "a":
                print (player)
                
            elif choice == "b":
                player.printInfo()
            
            else:
                print ("You've entered an illegal chioce")
                
        except KeyError:
            print ("\nThis player is not in the system.")
            
        response = input ("\nAre you interested in another player? ")
        answer = response.lower()
        
# Set variables to corresponding values       
fileName = "rushers.csv"
players = createPlayerDictionary(fileName)
printAlpha (players)
IndivPlayerInfo (players)
