# beginner-scraps
Scraps of code for the GitHub & Python beginner that I am :-) 

Entries below in reverse chronological order:

-2017-01-19: Created an iteration of the last script that attempts to log into each pingable device to grab its configured hostname to see how it compares to the configured DNS A-record

-2017-01-13: Created my second script based off my first one. The script pings a list of IPs, uses nslookup to see if they have a hostname associated with them, and writes the results to a file. The list of IPs are generated programmatically instead of being entered in entirely manually, with room for a few outliers to be added manually. The goal of this script is to see if a device is reachable, and to see if the DNS entry is what it should be. Putting this script together gave me a bunch of ideas for other things :-)

-2016-09-15: Created my first script used on a production network, cmdinput1.py. Very simple, asks for input command, runs command against list of Cisco IOS routers listed in file "input.txt", saves the results of the command to "output.txt". I first used it to run a "show cdp n | inc SEP" across all our routers to see which locations do not have a Cisco switch, but have more than a certain number of phones connected. If you look at the code, I am sure you will see all sorts of indications that I am an absolute beginner with this stuff.
