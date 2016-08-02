import os
import subprocess
import signal
import sys
import json
import time

from pprint import pprint

bar="~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
bre="\n\n"

def formatMsg(msg):
    print bar + bre +bre + msg + bre + bre + bar

with open("locations.json") as loc_file:
    loc_data = json.load(loc_file)

with open("bots.json") as bot_file:
    bot_data = json.load(bot_file)

formatMsg("You are running PokeFarm by Cade. v1.0\nLocation info given below")

loc_fullmsg = "Locations:\n\n"

for location in loc_data:
    t_loc = loc_data[location]
    loc_fullmsg = loc_fullmsg + "Index: " + str(t_loc["index"]) + "\nName: " + t_loc["name"] + "\nLocation: " + t_loc["loc"] + "\nInfo: " + t_loc["info"] + bre

formatMsg(loc_fullmsg)

def getCmd(un, pw, auth):
    #return "until (python pokecli.py -u " + un + " -p " + pw + " -l " + loc + "); do echo 'Process crashed with exit code $?.  Respawning..' >&2; done;"
    return "python ./pokecli.py -u " + un + " -p " + pw + " -l " + loc + " -a " + auth
    #return "echo $PWD"

def runBotN(n):
    if bots[n]["enabled"] != 1:
        return
    if all_processes[n] != None:
        try:
            os.kill(all_processes[n], 0)
            return
        except OSError:
            return
    cmd = getCmd(bots[n]["username"], bots[n]["password"], bots[n]["auth_service"])
    print cmd
    process = subprocess.Popen(cmd.split())
    #process = os.system(cmd)    
    all_processes[n] = process.pid

loc_index = str(input("Location Index: "))
for location in loc_data:
    if int(loc_data[location]["index"]) == int(loc_index):
        loc = loc_data[location]["loc"] 
        break

bots = []
for bot in bot_data:
    bots.append(bot_data[bot])

all_processes = [None] * len(bots)

for m in range(0, len(bots)):
    runBotN(m)

print all_processes
print bar + bre + "Use CTRL-C to close" + bre + bar

try:
    while True:
        for k in range(0, len(bots)):
            runBotN(k)
        time.sleep(30)
except KeyboardInterrupt:
    print "Now killing all bots"
    for p in all_processes:
        os.kill(int(p), signal.SIGINT)
        print "Killed " + str(p)
    print bar + bre + "Bot is done" + bre + bar
