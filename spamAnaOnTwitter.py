#!/usr/bin/env python
'''connect to Twitter and output user IDs that will be banned'''

import time
import logging
import inspect
import datetime
    
import twitter

COMMAND_INTERVAL = 15
suspicious_keywords = ['money', 'finance', 'mortgage', 'health', 'airline',
                       'download', 'adult', 'sex', 'music', 'game', 
                       'sell', 'buy']


def initialize():
    #user infor for cs5750
    api = twitter.Api(consumer_key='otyqFeLTbZiRjlC3KhKZA',
                   consumer_secret='s4EjBZgvaTkEyRyARigkRjCzLnhlfe63WYgNgPpO4',
                   access_token_key='2151667861-MfgX0cunxe9S6lgTYo1mFBpxIWtcDG1zmNLbJcR',
                   access_token_secret='oeYIUHT6px0U5Euu9bZ9iNhorJuwcgGwDF5lwlCER4317',
                   debugHTTP=True)
    logging.basicConfig(filename='5750tweetspam.log',level=logging.ERROR)
    return api

def handle_twitter_error(errs):
    for err in errs:
        logging.error('%s error: %s' % (inspect.stack()[1][3], err.message()))
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
            
def main():
    api = initialize()
    
    for keyword in suspicious_keywords:
        current_time = datetime.datetime.now()
        seeds = get_users_search(api, keyword)
        for seed in seeds:
            followers = get_followers(api, seed.id)
            print len(followers)
            print '======================================================================'
            for follower in followers:
                user = get_user(api, follower)
                if current_time - user.GetCreatedAt() < datetime.timedelta(day=7):
                    print user.GetScreenName(),
                    print user.GetCreatedAt()
    
    
    #f = open('seeds.dat','w')

    # return list of User objects
#     users = api.GetFriends()
#     for user in users:
#         seeds.add(user)
#     for user in seeds:
#         friends = api.GetFriends(user_id=user.id)
#         for friend in friends:
#             f.write(friend.id + '\t' + friend.name +'\t' + friend.screen_name+ '\d')
#             seeds.add(friend)
#             if(len(seeds) > SEED_SIZE):
#                 break
#         if(len(seeds) > SEED_SIZE):
#             break
#     f.close()
#     print 'seed done'


   # item = api.GetUser(screen_name = 'Barack Obama').AsDict()
   # print item
#     results = api.GetFollowerIDs(screen_name = 'Barack Obama')
#     print results
#     for result in results:
#       item = api.GetUser(result).AsDict()
#       print item['id'], item['screen_name']



if __name__ == "__main__":
    main()

''' Instruction:
  *Methods:
  ---api.GetUser(user)
  ---api.GetFriends()
  ---api.GetFollowers()
  ---api.GetRepllies()
  ---api.GetRetweeters()
  ---api.GetRetweets()
  ---api.GetUserRetweets()   
  ---api.GetUserTimeLine()
  ---api.GetUserSearch()
  ---api.GetSearch()        // Return Status object
  ---api.GetTrendsCurrent() // Get the current top trending topics
  ---api.GetTrendsWoeid()   // Return the top 1- trending topics for 
                            // a specific WOEID
  ---api.UsersLookup()      // Fetch extended information for this user

  *Class:
  User: id,name,screen_name,location
  Status: contributors, coordinates, created_at, created_at_in_seconds,
          favorited,favorite_count,id,lang,place,source,text,truncated,
          location
  
'''

