# discordbot-aikatsup-search

A discord bot search an Aikatsu image and write its url on the text channel.

## Requirement
* Python 3.6

## Setup

### Installation
Install pipenv with pip or Homebrew.
```
$ pip install pipenv
or
$ brew install pipenv
```
Run pipenv.
```
$ pipenv install
```
And then, edit `.env` to set your app token.
```
API_KEY={YOUR_APP_TOKEN}
```
See: [Creating a discord bot & getting a token](https://github.com/reactiflux/discord-irc/wiki/Creating-a-discord-bot-&-getting-a-token)

### Run 
```
$ pipenv shell
$ python run.py
```

### Run Nohup & Background Mode
```
$ sh ./run.sh
```

## Usage
Write `/aup/{keyword}` (ex. `/aup/穏やか` ) on text channel.


## AikatsUP!
This discord bot uses AikatsuUP!(aikatsu capture database) API.

http://aikatsup.com/

thanks @sakura_metal !