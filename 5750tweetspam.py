#!/usr/bin/env python
'''
connect to Twitter and output user IDs that will be banned
Created on Oct 29, 2013  @author: Qizhen
'''

import time
import datetime
import logging
import random
    
import twitter

COMMAND_INTERVAL = 5
SUSPICIOUS_KEYWORDS = ['money', 'finance', 'mortgage', 'health', 'airline',
                       'download', 'adult', 'sex', 'music', 'game', 'following',
                       'sell', 'buy', 'diet', 'jewelery', 'electronics', 'vehicle',
                       'contest', 'lottery', 'prize', 'loans', 'realty', 'girl',
                       'free', 'porn', 'dating']
KEYWORDS_COUNT = len(SUSPICIOUS_KEYWORDS)


def initialize():
    #user infor for cs5750
    api = twitter.Api(consumer_key='otyqFeLTbZiRjlC3KhKZA',
                   consumer_secret='s4EjBZgvaTkEyRyARigkRjCzLnhlfe63WYgNgPpO4',
                   access_token_key='2151667861-MfgX0cunxe9S6lgTYo1mFBpxIWtcDG1zmNLbJcR',
                   access_token_secret='oeYIUHT6px0U5Euu9bZ9iNhorJuwcgGwDF5lwlCER4317',
                   debugHTTP=True)
    logging.basicConfig(filename='5750tweetspam.log',level=logging.ERROR)
    return api

def handle_twitter_error(err):
    logging.exception(err)
    #logging.error('%s error: %s' % (inspect.stack()[1][3], err.message()[0]))
    time.sleep(COMMAND_INTERVAL)


    
def get_users_search(api, keyword):
    while True:
        try:
            seeds = api.GetUsersSearch(keyword, count=30)
            time.sleep(COMMAND_INTERVAL)
            return seeds
        except twitter.TwitterError as errs:
            handle_twitter_error(errs)

def get_followers(api, id):
    try:
        followers = api.GetFollowerIDs(id, count=5000, total_count=5000)
        time.sleep(COMMAND_INTERVAL)
        return followers
    except twitter.TwitterError as errs:
        handle_twitter_error(errs)
        return []
        
def get_user(api, id):
    try:
        user = api.GetUser(id)
        time.sleep(COMMAND_INTERVAL)
        return user
    except twitter.TwitterError as errs:
        handle_twitter_error(errs)    
        
def is_user_spam(user):
    is_spam = True
    current_time = time.mktime(time.gmtime())
    created_time = time.mktime(time.strptime(user.GetCreatedAt(), "%a %b %d %H:%M:%S +0000 %Y"))
    relative_created_time = datetime.timedelta(seconds = (current_time - created_time))
    is_spam &= relative_created_time < datetime.timedelta(days=7)
#     is_spam &= user.GetStatusesCount() > 5
#     is_spam &= user.GetFriendsCount() > 10
#     is_spam &= not user.GetLocation()

    #print user.GetProfileBackgroundImageUrl()
    return is_spam
    
            
def main():
    api = initialize()
    
    while True:
        keyword_index = random.randrange(0, KEYWORDS_COUNT)
        tweets = api.GetSearch(SUSPICIOUS_KEYWORDS[keyword_index], count = 5000)
        for tweet in tweets:
            if len(tweet.urls) >0:
                sapm_url = False
                for url in tweet.urls:
                    print url.expanded_url
                print tweet
#             if is_user_spam(tweet.GetUser()):
#                 print tweet.GetText()
#                 print tweet.urls
#                 print tweet.GetUser()
    




if __name__ == "__main__":
    main()