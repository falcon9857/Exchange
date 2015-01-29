import json
import time
import praw
import pdb
import re
import os
from config_bot import *
from pprint import pprint
from urllib2 import urlopen

#Checks for the user config file: config_bot.py
if not  os.path.isfile("config_bot.py"):
    print "You must create a config file with your username and password."
    print "Please see config_skel.py"
    exit(1)
    
#User Agent and Reddit User info to pass to Reddit
user_agent = ("ExchangeRateBot 1.0 by /u/falcon9857")
r = praw.Reddit(user_agent = user_agent)
r.login(REDDIT_USERNAME, REDDIT_PASS)

#Pulls the Exchange Rate API. Comes in list, changed to dictionary.
ExRateData = urlopen("http://www.getexchangerates.com/api/latest.json")
ExRateData = json.load(ExRateData)
ExRateData = ExRateData.pop(0)

#Opens the file "posts_replied_to.txt" to store ids
with open("posts_replied_to.txt", "r") as f:
   posts_replied_to = f.read()
   posts_replied_to = posts_replied_to.split("\n")
   posts_replied_to = filter(None, posts_replied_to)

#What subreddit(s) does it operate in?
subreddit = "falcon9857"

#Function for Currency Conversion
def conversion(request):
    request = request.upper()
    request = request.split(" ")
    request.remove("EXRATE!")
    if len(request)!= 4:
        return "Error"
    elif request[1] not in ExRateData or request[3] not in ExRateData:
        return "Error"
    else:
        rate = float(ExRateData[request[1]])
        exrate = float(ExRateData[request[3]])
        value = float(request[0])
        exchange = round(1/rate * value * exrate,2)
        request[2] = "="
        request.insert(3,str(exchange))
        conversion_comment = " ".join(request)
        comment.reply(conversion_comment)
        print "Commented!", comment.id
                        
#Commenting Criteria
while True:
    subreddit_comments = r.get_comments(subreddit,limit=100)
    for comment in  subreddit_comments:
        if "ExRate!" in comment.body and comment.id in posts_replied_to:
            pass
        if "ExRate!" in comment.body and comment.id not in posts_replied_to:
            print "Found One:", comment
            request = comment.body
            conversion(request)
            posts_replied_to.append(comment.id)
            with open("posts_replied_to.txt", "w") as f:
                for post_id in posts_replied_to:
                    f.write(post_id + "\n")
    # waits and timestamps the loops
    ts = time.time()
    print "-----", ts, "-----"
    time.sleep(5)


