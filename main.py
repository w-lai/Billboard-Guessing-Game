import requests
import random

NUMBER_OF_GAMES = 3
BASE = "https://webscrapingpythonapi.herokuapp.com/"
#create an array that stores all the song data
songInfo = []
response = requests.get(BASE + "songs/")
response = response.json()
songInfo.append(response)
    

print("Welcome to the game of guessing song rankings on the top charts")
statistics = 0
#make a loop that makes the game run the # game times

for i in range(1, NUMBER_OF_GAMES + 1):
    print("Pick the order of the following songs:")
    # get three random numbers
    x = songInfo[random.randrange(0,3)]
    y = songInfo[random.randrange(0,3)]
    while(y == x):
        y = songInfo[random.randrange(0,3)]
    z = songInfo[random.randrange(0,3)]
    while(z == x or z == y):
        z = songInfo[random.randrange(0,3)]
    print(x["name"])
    print(y["name"])
    print(z["name"])
    num1 = input("Highest ranked song name: ")
    num2 = input("Second highest ranked song name: ")
    num3 = input("Lowest ranked song name: ")
    xRank = x["rank"]
    yRank = y["rank"]
    zRank = z["rank"]
    if(yRank > xRank and yRank < zRank):
        winningLetter = x
        secondLetter = y
        lastLetter = z
    if(yRank > zRank and yRank < xRank):
        winningLetter = z
        secondLetter = y
        lastLetter = x
    if(xRank > zRank and xRank < yRank):
        winningLetter = z
        secondLetter = x
        lastLetter = y
    if(xRank > yRank and xRank < zRank):
        winningLetter = y
        secondLetter = x
        lastLetter = z
    if(zRank > yRank and zRank < xRank):
        winningLetter = y
        secondLetter = z
        lastLetter = x
    if(zRank > xRank and zRank < yRank):
        winningLetter = x
        secondLetter = z
        lastLetter = y
    
    
    if(num1 == winningLetter["name"] and num2 == secondLetter["name"] and num3 == lastLetter["name"]):
        statistics += 1
        print("You're Correct!")
    else:
        print("Sorry, you were wrong :(")
        print("The correct ranking is: ")
        print(winningLetter["name"])
        print(secondLetter["name"])
        print(lastLetter["name"])
        
print("Congrats! You got " + str(statistics) + " right out of " + str(NUMBER_OF_GAMES))
        
