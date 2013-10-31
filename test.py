#!/usr/bin/env python

'''Load the latest update for a Twitter user and leave it in an XHTML fragment'''

__author__ = 'dewitt@google.com'


import twitter
import inspect




def main():
    
    api = twitter.Api(consumer_key='sW6sjRTRekP8L0m4rPmVg',
                   consumer_secret='PUa0mSgDrCCW7RsCHoLMrvy2ViqgbKKEd8CIGDGw1c',
                   access_token_key='12996082-gvzUgnfZe0uIDgol1FD4y1RI1xDIyCxENO6r0BfrD',
                   access_token_secret='UJgSMVp60ip7NM9j8h9iat6iXU8nQSMoPEBA5oJaSIcba',
                   debugHTTP=True)
     
    item = api.GetUser('2153352006') #screen_name = 'BatuTurguteli17')
    print item.GetStatusesCount()
    print item.GetLocation()
    print item.GetDescription()
    print item.GetFollowersCount()
    print item.GetFriendsCount()
    print item.GetProfileBackgroundImageUrl()
  
#     results = api.GetFollowerIDs('ruanqizhen')
#     print results
#     for result in results:
#         item = api.GetUser(result).AsDict()
#         print item['id'], item['screen_name']



if __name__ == "__main__":
    main()
