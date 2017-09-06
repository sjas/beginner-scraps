# beginner-scraps
Scraps of code for the GitHub & Python beginner that I am :-) 

Entries below in reverse chronological order:

-2017-09-06: Spent a couple of days attempting to work in Python3. I'm sure I got some syntax wrong. I wrote a script that uses SNMP to poll a switch, determine if it's a Cisco 48-port Gigabit, 48-port FE, or 24-port FE (that's what I have in my environment right now), or none of those. It then polls for the system uptime, and the timer for the last interface state change is subtracted. If the interface has been down for longer than 14 days, and doesn't have a description set, it is available for re-use and is displayed in the output. I wrote this script because people kept asking me which ports were available on which switches, and while I had a switch port mapping tool to handle this, I found running this script to gather the specific information I was looking for was much faster. This script definitely reveals the n00b I am -- I know this can be modularized with functions and features, I just haven't got there yet.

-2017-08-09: First attempt with Ansible to push out configs to Cisco routers

-2017-03-17: Added an old script that I found in my archives that truly is a beginner scrap :-) It's a PowerShell script to log into SSH devices and issue a command, with the intended use case of logging into a bunch of Cisco equipment and issuing "show run" and saving the output to separate files for configuration backup.

-2017-01-19: Created an iteration of the last script that attempts to log into each pingable device to grab its configured hostname to see how it compares to the configured DNS A-record

-2017-01-13: Created my second script based off my first one. The script pings a list of IPs, uses nslookup to see if they have a hostname associated with them, and writes the results to a file. The list of IPs are generated programmatically instead of being entered in entirely manually, with room for a few outliers to be added manually. The goal of this script is to see if a device is reachable, and to see if the DNS entry is what it should be. Putting this script together gave me a bunch of ideas for other things :-)

-2016-09-15: Created my first script used on a production network, cmdinput1.py. Very simple, asks for input command, runs command against list of Cisco IOS routers listed in file "input.txt", saves the results of the command to "output.txt". I first used it to run a "show cdp n | inc SEP" across all our routers to see which locations do not have a Cisco switch, but have more than a certain number of phones connected. If you look at the code, I am sure you will see all sorts of indications that I am an absolute beginner with this stuff.
