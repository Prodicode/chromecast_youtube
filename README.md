# Chromecast Youtube 

## Description
Chromecast Youtube is a simple python3 script that can play and stop specific YouTube videos on a chromecast device from the CLI.

## Usage
```
chromecast_youtube.py [-h] -t T -v V [--play] [--stop]
```

Help menu:
```
usage: chromecast_youtube.py [-h] -t T -v V [--play] [--stop]

A simple python3 script that plays or stops Youtube videos on a chromecast
device

optional arguments:
  -h, --help  show this help message and exit

Required:
  -t T        The IP of the targeted Chromecast device.
  -v V        The video id of the youtube video which should be played

Actions:
  --play      Plays the video
  --stop      Stops the video

Example: python3 chromecast_youtube.py -t 192.168.1.14 -v qhR1SqBjXQM --play
```

## To Do
* Implement volume control
* Create a GUI

Any Pull Requests are very welcomed!

## Note
The program requires the [requests](https://github.com/requests/requests) library. If the program doesn't work, make sure to install it.
