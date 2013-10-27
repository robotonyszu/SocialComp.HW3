
from twitter import *
OAUTH_TOKEN = '1315809169-S6aYuqVJaVNpKyTlMTXG3byHqL14NSWp6G1u9eH'
OAUTH_SECRET = 'yowEwXB1oGy8S0PzZ1zkPuw3M6AzZ7Mai5ZFXThKgMHs0'
CONSUMER_KEY = 'jzExA4kqvNMMrjwzFwDClA'
CONSUMER_SECRET ='va8CJBjAaiD1Am0aszBOUcXznM76nrmNoQ0OfoD63F8'

# see "Authentication" section below for tokens and keys
t = Twitter(
                auth=OAuth(OAUTH_TOKEN, OAUTH_SECRET,
                                         CONSUMER_KEY, CONSUMER_SECRET)
                           )

# Get your "home" timeline
t.statuses.home_timeline()

# Get a particular friend's timeline
t.statuses.friends_timeline(id="scavin")

# Also supported (but totally weird)
t.statuses.friends_timeline.scavin()

# to pass in GET/POST parameters, such as `count`
t.statuses.home_timeline(count=5)

# to pass in the GET/POST parameter `id` you need to use `_id`
t.statuses.oembed(_id=1234567890)

# Update your status
t.statuses.update(
        status="Using @sixohsix's sweet Python Twitter Tools.")

# Send a direct message
#t.direct_messages.new(
#        user="billybob",
#            text="I think yer swell!")

# Get the members of tamtar's list "Things That Are Rad"
#t._("tamtar")._("things-that-are-rad").members()

# Note how the magic `_` method can be used to insert data
# into the middle of a call. You can also use replacement:
#t.user.list.members(user="tamtar", list="things-that-are-rad")

# An *optional* `_timeout` parameter can also be used for API
# calls which take much more time than normal or twitter stops
# responding for some reasone
t.users.lookup(screen_name=','.join(A_LIST_OF_100_SCREEN_NAMES), _timeout=1)

# Overriding Method: GET/POST
# you should not need to use this method as this library properly
# detects whether GET or POST should be used, Nevertheless
# to force a particular method, use `_method`
t.statuses.oembed(_id=1234567890, _method='GET')

t.search.tweets(q="#pycon")
