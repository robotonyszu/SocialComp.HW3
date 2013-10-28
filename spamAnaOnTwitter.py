#!/usr/bin/env python
'''connect to Twitter and output user IDs that will be banned'''

import twitter


suspicious_keywords = ['money', 'finance', 'mortgage', 'health', 'airline',
                       'download', 'adult', 'sex', 'music', 'game', 
                       'sell', 'buy']


def initial():
    #user infor for cs5750
    api = twitter.Api(consumer_key='otyqFeLTbZiRjlC3KhKZA',
                   consumer_secret='s4EjBZgvaTkEyRyARigkRjCzLnhlfe63WYgNgPpO4',
                   access_token_key='2151667861-MfgX0cunxe9S6lgTYo1mFBpxIWtcDG1zmNLbJcR',
                   access_token_secret='oeYIUHT6px0U5Euu9bZ9iNhorJuwcgGwDF5lwlCER4317',
                   debugHTTP=True)
    return api

def main():

    api = initial()
    
    for keyword in suspicious_keywords:
        seeds = api.GetUsersSearch(keyword, count=30)
        for seed in seeds:
            followers = api.GetFollowerIDs(seed.id, count=100)
            for follower in followers():
                print follower
    
    
    
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

