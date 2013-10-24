#!/usr/bin/env python

'''Load the latest update for a Twitter user and leave it in an XHTML fragment'''

__author__ = 'dewitt@google.com'

import codecs
import getopt
import sys
import twitter

TEMPLATE = """
<div class="twitter">
  <span class="twitter-user"><a href="http://twitter.com/%s">Twitter</a>: </span>
  <span class="twitter-text">%s</span>
  <span class="twitter-relative-created-at"><a href="http://twitter.com/%s/statuses/%s">Posted %s</a></span>
</div>
"""

def Usage():
    print 'Usage: %s [options] twitterid' % __file__
    print
    print '  This script fetches a users latest twitter update and stores'
    print '  the result in a file as an XHTML fragment'
    print
    print '  Options:'
    print '    --help -h : print this help'
    print '    --output : the output file [default: stdout]'




def main():
    api = twitter.Api(consumer_key='sW6sjRTRekP8L0m4rPmVg',
                   consumer_secret='PUa0mSgDrCCW7RsCHoLMrvy2ViqgbKKEd8CIGDGw1c',
                   access_token_key='12996082-gvzUgnfZe0uIDgol1FD4y1RI1xDIyCxENO6r0BfrD',
                   access_token_secret='UJgSMVp60ip7NM9j8h9iat6iXU8nQSMoPEBA5oJaSIcba',
                   debugHTTP=True)
    
    item = api.GetUser(screen_name = 'risent').AsDict()
    print item
#     results = api.GetFollowerIDs('ruanqizhen')
#     print results
#     for result in results:
#         item = api.GetUser(result).AsDict()
#         print item['id'], item['screen_name']



if __name__ == "__main__":
    main()
