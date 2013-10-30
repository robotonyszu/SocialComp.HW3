#!/usr/bin/env python

'''Load the latest update for a Twitter user and leave it in an XHTML fragment'''

__author__ = 'dewitt@google.com'

import codecs
import getopt
import sys
import twitter
import inspect
# Numpy is a library for handling arrays (like data points)
import numpy as np

# Pyplot is a module within the matplotlib library for plotting
import matplotlib.pyplot as plt


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

def test():
    print inspect.stack()[1]


def main():
    

    
    # Create an array of 100 linearly-spaced points from 0 to 2*pi
    x = np.linspace(0,2*np.pi,100)
    y = np.sin(x)
    
    # Create the plot
    plt.plot(x,y)
    
    # Save the figure in a separate file
    plt.savefig('sine_function_plain.png')
    
    # Draw the plot to the screen
    plt.show()

#     api = twitter.Api(consumer_key='sW6sjRTRekP8L0m4rPmVg',
#                    consumer_secret='PUa0mSgDrCCW7RsCHoLMrvy2ViqgbKKEd8CIGDGw1c',
#                    access_token_key='12996082-gvzUgnfZe0uIDgol1FD4y1RI1xDIyCxENO6r0BfrD',
#                    access_token_secret='UJgSMVp60ip7NM9j8h9iat6iXU8nQSMoPEBA5oJaSIcba',
#                    debugHTTP=True)
#     
#     item = api.GetUser(screen_name = 'ABrad789')
#     print item.GetStatusesCount()
#     print item.GetLocation()
#     print item.GetDescription()
#     print item.GetFriendsCount()
#     print item.GetProfileBackgroundImageUrl()

#     results = api.GetFollowerIDs('ruanqizhen')
#     print results
#     for result in results:
#         item = api.GetUser(result).AsDict()
#         print item['id'], item['screen_name']



if __name__ == "__main__":
    main()
