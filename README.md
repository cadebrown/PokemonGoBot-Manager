# PokemonGoBot-Manager

Manager for a pokemon go bot - https://github.com/PokemonGoF/PokemonGo-Bot - , written in python, utilizing json

## Installation/Setup
First, run:  `./install.sh`

Then, go to `configs/config.json`, and enter your Gmaps API key. You should not enter gmail/passwords here.

Set up your bots in `bots.json` replacing the example fields. You can copy and paste new bots with new info here.

Run `python start.py`, and it will list locations, just enter the index of the one you want, and it starts running!

You see all output from all bots in this one shell. Press enter, or ctrl c to stop at any time!



## Configuration

### bots.json

Here is the example file:
```
{
  "an enabled bot": {
    "username": "$name@gmail.com",
    "password": "$password",
    "enabled": "1"
  },
  "another bot that wont run": {
    "username": "$othername@gmail.com",
    "password": "$otherpassword",
    "enabled": "0"
  }
}
```

You can copy a section, then change the login info like so:
```
{
  "an enabled bot": {
    "username": "$name@gmail.com",
    "password": "$password",
    "enabled": "1"
  },
  "another bot that wont run": {
    "username": "$othername@gmail.com",
    "password": "$otherpassword",
    "enabled": "0"
  },
  "A third bot": {
    "username": "$thirdname@gmail.com",
    "password": "$thirdpassword",
    "enabled": "1"
  }
}
```
The `enabled` tells it whether to run or not. `1` means the bot will run, `0` means it won't
You may add as many as you'd like.

### locations.json
```
{
  "0. Santa Monica Pier - Great General Farming": {
    "index": "0",
    "name": "Santa Monica Pier",
    "info": "Great for water types, electabuzz, pokestops, overall great for general grinding",
    "loc": "34.008344620842834,-118.49794507026672"
  },
  "1. Dratini Nest in CA": {
    "index": "1",
    "name": "Eagle's Nest Dratini Nest",
    "info": "The best dratini nest in the US (so far)",
    "loc": "38.55543153813066,-121.23698472976685"
  },
  "2.Good farming spot": {
    "index": "2",
    "name": "Sydney",
    "info": "General farming",
    "loc": "-33.866609,151.209120"
  },
  "3. Central Park - Snorlax Spot": {
    "index": "3",
    "name": "Central Park SW",
    "info": "Snorlax spawned here",
    "loc": "40.76976805976344,-73.979771733284"
  },
  "4. London": {
    "index": "4",
    "name": "Densest area of london",
    "info": "Good for XP/Snorlax",
    "loc": "51.495011293466746,-0.13200759887695312"
  }
}
```

Just like the bots, you may add a location here:
```
{
  "0. Santa Monica Pier - Great General Farming": {
    "index": "0",
    "name": "Santa Monica Pier",
    "info": "Great for water types, electabuzz, pokestops, overall great for general grinding",
    "loc": "34.008344620842834,-118.49794507026672"
  },
  "1. Dratini Nest in CA": {
    "index": "1",
    "name": "Eagle's Nest Dratini Nest",
    "info": "The best dratini nest in the US (so far)",
    "loc": "38.55543153813066,-121.23698472976685"
  },
  "2.Good farming spot": {
    "index": "2",
    "name": "Sydney",
    "info": "General farming",
    "loc": "-33.866609,151.209120"
  },
  "3. Central Park - Snorlax Spot": {
    "index": "3",
    "name": "Central Park SW",
    "info": "Snorlax spawned here",
    "loc": "40.76976805976344,-73.979771733284"
  },
  "4. London": {
    "index": "4",
    "name": "Densest area of london",
    "info": "Good for XP/Snorlax",
    "loc": "51.495011293466746,-0.13200759887695312"
  },
  ,
  "5. KY Dratini Nest": {
    "index": "4",
    "name": "KY dratini nest on campus",
    "info": "Good for dratini",
    "loc": "38.015111, -84.504557"
  }
}
```
And when you run start.py again, 5. KY Dratini Nest will show up
