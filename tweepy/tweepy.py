# can you write roboust python script using tweepy to find trending topics?

import tweepy

# authenticate to the Twitter API
auth = tweepy.OAuthHandler('consumer_key', 'consumer_secret')
auth.set_access_token('access_token', 'access_token_secret')

# create API object
api = tweepy.API(auth)

# get the WOEID (Where On Earth ID) for a location
location = api.trends_closest(37.781157, -122.40061283)
woeid = location[0]['woeid']

# get the trending topics for the location
trends = api.trends_place(woeid)

# extract the name of each trending topic
trend_topics = [trend['name'] for trend in trends[0]['trends']]

# print the trending topics
print("Trending topics:", trend_topics)
