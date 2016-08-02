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

The example file is `bots.json.example`

Copy that to `bots.json` (remove the `.example`), and change what you would like

The `enabled` tells it whether to run or not. `1` means the bot will run, `0` means it won't
You may add as many as you'd like.

### locations.json
The example file is locations.json.example

Copy this to `locations.json` (remove the `.example`)

Just like the bots, you may add a location here.
When the bot runs, it will ask which location you'd like to run.


## Updating

I try to keep this as updated as possible, but if you would like a new version of the bot, simply:
clone the main bot (https://github.com/PokemonGoF/PokemonGo-Bot) into a seperate folder.
Replace my `pokecli.py` with the cloned one, as well as the directory `pokemongo_bot/` and `requirements.txt`. Then run `pip install -r requirements.txt`. My manager is designed to run version-neutral of the bot.
