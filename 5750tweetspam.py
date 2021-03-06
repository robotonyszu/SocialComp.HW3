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

COMMAND_INTERVAL = 15
SUSPICIOUS_KEYWORDS = ['money', 'finance', 'mortgage', 'health', 'airline',
                       'download', 'adult', 'sex', 'music', 'game', 'following',
                       'sell', 'buy', 'diet', 'jewelery', 'electronics', 'vehicle',
                       'contest', 'lottery', 'prize', 'loans', 'realty', 'girl',
                       'free', 'porn', 'dating', 'clearance', 'singles', 'Income',
                       'boss', 'earn', 'double', 'extra', 'cash', 'business', 
                       'degree', 'diploma', 'work', 'affordable', 'bargain',
                       'best', 'beneficiary', 'price', 'bucks', 'bonus', 'cheap',
                       'check', 'claims', 'collect', 'rates', 'credit', 'easy',
                       'fast', 'investment', 'lower', 'only', 'profit', 'dollars',
                       'debt', 'stock', 'chance', 'leave', 'passwords', 'solution',
                       'teen', 'wife', 'success', 'cures', 'viagra', 'xanax',
                       'vicodin', 'weight', 'bill', 'inventory', 'nature', 'shipping',
                       'available', 'fingertips', 'online']
#http://www.inmotionhosting.com/support/edu/everything-email/spam-prevention-techniques/common-spam-words
KEYWORDS_COUNT = len(SUSPICIOUS_KEYWORDS)


def initialize():
    #user infor for cs5750
#     api = twitter.Api(consumer_key='otyqFeLTbZiRjlC3KhKZA',
#                    consumer_secret='s4EjBZgvaTkEyRyARigkRjCzLnhlfe63WYgNgPpO4',
#                    access_token_key='2151667861-MfgX0cunxe9S6lgTYo1mFBpxIWtcDG1zmNLbJcR',
#                    access_token_secret='oeYIUHT6px0U5Euu9bZ9iNhorJuwcgGwDF5lwlCER4317',
#                    debugHTTP=True)
    api = twitter.Api(consumer_key='sW6sjRTRekP8L0m4rPmVg',
                   consumer_secret='PUa0mSgDrCCW7RsCHoLMrvy2ViqgbKKEd8CIGDGw1c',
                   access_token_key='12996082-gvzUgnfZe0uIDgol1FD4y1RI1xDIyCxENO6r0BfrD',
                   access_token_secret='UJgSMVp60ip7NM9j8h9iat6iXU8nQSMoPEBA5oJaSIcba',
                   debugHTTP=True)
    logging.basicConfig(filename='5750tweetspam.log',level=logging.ERROR)
    return api

def handle_twitter_error(err):
    logging.exception(err)
    time.sleep(COMMAND_INTERVAL)
   
def tweet_search(api, keyword):
    #print keyword
    while True:
        try:
            tweets = api.GetSearch(keyword, count = 5000)
            #print len(tweets)
            time.sleep(COMMAND_INTERVAL)
            return tweets
        except twitter.TwitterError as err:
            handle_twitter_error(err)
        
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
    
def is_url_spam(urls):
    suspicus_sites = ['bit.ly', 'tinyurl.com', 'is.gd', 'goo.gl', 'ow.ly', 
                      'dlvr.it', 'tiny.cc', '3.ly', 'tiny.ly']
    for url in urls:
        for site in suspicus_sites:
            if site in url.expanded_url:
                return True
    return False
            
def main():
    api = initialize()
<<<<<<< HEAD
=======
    spammers = set()
    normal_user = set()
    
>>>>>>> f9c49f784296ff5590721133ff789073328952bb
    while True:
        keyword_index = random.randrange(0, KEYWORDS_COUNT)
        tweets = tweet_search(api, SUSPICIOUS_KEYWORDS[keyword_index])
        for tweet in tweets:
            if is_url_spam(tweet.urls):
                user = tweet.GetUser()
                user_id = user.GetId()
                if not user_id in normal_user and not user_id in spammers:
                    if is_user_spam(user):
                        print user_id
                        print user
                        spammers.add(user_id)
                    else:
                        normal_user.add(user_id)
                        
    




if __name__ == "__main__":
    main()
