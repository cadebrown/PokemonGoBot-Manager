import os
import subprocess
import signal
import sys
import json

from pprint import pprint

#Formatting stuff
bar="~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
bre="\n\n"

#Send with breaks
def formatMsg(msg):
    print bar + bre +bre + msg + bre + bre + bar

#Opening json
with open("locations.json") as loc_file:
    loc_data = json.load(loc_file)

#Open bot info
with open("bots.json") as bot_file:
    bot_data = json.load(bot_file)

#Intro
formatMsg("You are running PokeFarm by Cade. v1.0\nLocation info given below")

#Start building a string
loc_fullmsg = "Locations:\n\n"

#Read up to 20 locations
for location in loc_data:
    t_loc = loc_data[location]
    loc_fullmsg = loc_fullmsg + "Index: " + t_loc["index"] + "\nName: " + t_loc["name"] + "\nLocation: " + t_loc["loc"] + "\nInfo: " + t_loc["info"] + bre

#Print out all the location names
formatMsg(loc_fullmsg)

#Gets command for username and password
def getCmd(un, pw):
    return ["python", "pokecli.py", "-cf", "configs/config.json", "-u", un, "-p", pw, "-l", loc]


#Collecintg PIDs
all_processes = []

#Determining where the user wants to farm
loc_index = str(input("Location Index: "))
for location in loc_data:
    if int(loc_data[location]["index"]) == int(loc_index):
        loc = loc_data[location]["loc"] 
        break

#Loop through and create processes
for bot in bot_data:
    if int(bot_data[bot]["enabled"]) != 1:
        continue
    #We build the cmd string/array
    cmd = getCmd(bot_data[bot]["username"], bot_data[bot]["password"])
    #Print out for debugging
    print cmd

    #Create it from our builder
    process = subprocess.Popen(cmd)
    #Store it's pid
    all_processes.append(process.pid)

#it waits for them to press enter
print bar + bre + "Press enter to close anytime" + bre + bar
raw_input("Press to close")

for p in all_processes:
    os.kill(p, signal.SIGINT)
    print "Killed " + str(p)
print bar + bre + "Bot is done" + bre + bar
