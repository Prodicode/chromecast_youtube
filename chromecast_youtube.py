#Copyright Tudor Gheorghiu - Prodicode Solutions S.R.L.
#Github: https://github.com/Prodicode/chromecast_youtube

import argparse;
import sys;
import urllib.request;
import os;
import requests;

print('\n');

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

ok = '['+bcolors.OKGREEN+'OK'+bcolors.ENDC+'] ';
err = '['+bcolors.FAIL+'ERROR'+bcolors.ENDC+'] ';
info = '['+bcolors.OKBLUE+'INFO'+bcolors.ENDC+'] ';

parser = argparse.ArgumentParser(description="A simple python3 script that plays or stops Youtube videos on a chromecast device. Made by Tudor Gheorghiu - Prodicode (https://prodicode.com)", epilog='Example: python3 chromecast_youtube.py -t 192.168.1.14 -v qhR1SqBjXQM --play');
requiredArgs = parser.add_argument_group('Required');
requiredArgs.add_argument('-t', help='The IP of the targeted Chromecast device.', required=True);
requiredArgs.add_argument('-v', help='The video id of the youtube video which should be played', required=True);
parser.add_argument('-p', help='The port on which chromecast is running. Default is 8008', default="8008");
actionArgs = parser.add_argument_group('Actions');
actionArgs.add_argument("--play", help='Plays the specified Youtube video', action='store_true');
actionArgs.add_argument("--stop", help='Stops the video', action='store_true');
args = parser.parse_args();

if not (args.play or args.stop):
    sys.exit(err+"Please specify one action: --play or --stop\n");

if (args.play and args.stop):
    sys.exit(err+"Please specify only ONE action: --play or --stop, not both\n");

print(ok+"Checking connection with "+args.t+" on port "+args.p);

response = os.system("ping -p "+args.p+" -c 1 " + args.t);

if response != 0:
    print(err+"Could not connect to target");


print(ok+"Gathering target information...");

try:
    r = requests.get('http://'+args.t+":"+args.p+"/setup/eureka_info?options=detail");
    uptime = r.json()['uptime'];
    model = r.json()['detail']['manufacturer'] + " " + r.json()['detail']['model_name'];
    device = r.json()['name'];
    print(info+"Model: "+model);
    print(info+"Device: "+device);
    print(info+"Up Time: "+str(uptime));
except:
    print(err+"Could not get information");
    uptime = "undefined";
    model = "undefined";
    device = "undefined";




if args.play:
    try:
        requests.post('http://'+args.t+':'+args.p+'/apps/YouTube', data={'v':args.v});
    except:
        sys.exit(err+"Error sending Youtube video");
    print(ok+"Sent video "+args.v+" to "+device);
else:
    try:
        requests.delete('http://'+args.t+':'+args.p+'/apps/YouTube');
    except:
        sys.exit(err+"Error stopping video");
    print(ok+"Stopped video on "+device);
