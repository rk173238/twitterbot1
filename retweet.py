import tweepy
import datetime
from textblob import TextBlob

#Read credential from txt file.
file = open("twitterkeys.txt", "r")
data = file.readlines()
cons_key = data[0][10:-1]
cons_sec = data[1][10:-1]
acc_token = data[2][10:-1]
acc_sec = data[3][10:-1]
auth = tweepy.OAuthHandler(cons_key,cons_sec)
auth.set_access_token(acc_token,acc_sec)
api = tweepy.API(auth)

#define tags
l = ['climate','pollution','clean ocean','forest','plastic','recycl','recycling']


from random import randint
ptime,tweetnumber = 0,0
ttime = datetime.datetime.now().hour
while (ttime > 0):
    #Pick any tag and search tweets related to it
    tweets = api.search(q = l[randint(0,6)])
    i = 0
    polp,poln,ipos,ineg = 0,0,0,0
    
    #checks sentiment for each tweet.
    for t in tweets:
        a = TextBlob(t.text)
        pol = a.sentiment.polarity
        if pol > 0 and pol > polp:
            polp = pol
            ipos = i
        elif pol < 0 and pol < poln:
            poln = pol
            ineg = i
        i = i + 1
    #make tweets(each tweet should be different,so i added tweet number)
    tweetpos = "#HumNahiSudhrenge it is good to hear. something good is happening.\n this tweet is a small attempt to create twitter trend about world's actual cause. \n\n\n\ndisclaimer\nthese tweets are automated " + str(tweetnumber) + " https://twitter.com/screenname/status/" + str(tweets[ipos].id)
    tweetneg = "#HumNahiSudhrenge it is bad to hear. we definatly need to change our lifestyle,\n this tweet is a small attempt to create twitter trend about world's actual cause. \n\n\n\ndisclaimer\nthese tweets are automated " + str(tweetnumber) + " https://twitter.com/screenname/status/" + str(tweets[ineg].id)

    #retweet with help of tweepy's update_status.
    api.update_status(tweetpos)
    api.update_status(tweetneg)
    tweetnumber = tweetnumber + 1
    ttime = datetime.datetime.now().hour
    if ptime < ttime:
        ptime = ttime
        print(ptime)
    #if any (pos or neg tweet) posted till 150 times stop the code for today. 
    if tweetnumber == 150:
        print("today's task completed")
        break