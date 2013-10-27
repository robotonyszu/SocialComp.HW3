#!/usr/bin/env python
'''Load the latest update for a Twitter user and leave it in an XHTML fragment'''

__author__ = 'CS5750@google.com'

import codecs
import getopt
import sys
import twitter


def Usage():
    print 'Usage: %s [options] twitterid' % __file__
    print
    print '  This script fetches a users latest twitter update and stores'
    print '  the result in a file as an XHTML fragment'
    print
    print '  Options:'
    print '    --help -h : print this help'
    print '    --output : the output file [default: stdout]'


def initial():
   # user infor for cs5750
    api = twitter.Api(consumer_key='otyqFeLTbZiRjlC3KhKZA',
                   consumer_secret='s4EjBZgvaTkEyRyARigkRjCzLnhlfe63WYgNgPpO4',
                   access_token_key='2151667861-MfgX0cunxe9S6lgTYo1mFBpxIWtcDG1zmNLbJcR',
                   access_token_secret='oeYIUHT6px0U5Euu9bZ9iNhorJuwcgGwDF5lwlCER4317',
                   debugHTTP=True)
    return api
def main():
    SEED_SIZE = 100
    seeds = set()
    api = initial()
    # return list of User objects
    users = api.GetFriends()
    for user in users:
      seeds.add(user)
    for user in seeds:
      friends = api.GetFriends(user_id=user.id)
      for friend in friends:
        seeds.add(friend)
        if(len(seeds) > SEED_SIZE):
          break
      if(len(seeds) > SEED_SIZE):
        break
    print 'seed done'


   # item = api.GetUser(screen_name = 'Barack Obama').AsDict()
   # print item
    results = api.GetFollowerIDs(screen_name = 'Barack Obama')
    print results
    for result in results:
      item = api.GetUser(result).AsDict()
      print item['id'], item['screen_name']



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
  ---api.GetSearch()
  ---api.GetTrendsCurrent() // Get the current top trending topics
  ---api.GetTrendsWoeid()   // Return the top 1- trending topics for 
                            // a specific WOEID
  ---api.UsersLookup()      // Fetch extended information for this user

  *Class:
  User: id,name,screen_name,location

'''
