# discord-aikatsu-image

## Requirement
* Python 3.6

## Setup

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
```:.env
API_KEY={YOUR_APP_TOKEN}
```
See: [Creating a discord bot & getting a token](https://github.com/reactiflux/discord-irc/wiki/Creating-a-discord-bot-&-getting-a-token)

## Usage
### Run 
```
$ pipenv shell
$ python run.py
```

### Run Nohup & Background Mode
```
$ sh ./run.sh
```
