import tweepy

# Authenticate to Twitter API
auth = tweepy.OAuthHandler("consumer_key", "consumer_secret")
auth.set_access_token("access_token", "access_token_secret")

# Create API object
api = tweepy.API(auth)

# Define the hashtag or keyword you want to search for
query = "#example"

# Define the number of tweets to retrieve per request
tweets_per_request = 100

# Define the maximum number of requests to make
max_requests = 5

# Initialize a variable to store the max_id from each request
max_id = -1

# Initialize a variable to keep track of the number of requests made
request_count = 0

# Initialize a list to store all the tweets
tweets = []

# Use a while loop to make multiple requests and retrieve more data
while request_count < max_requests:
    if max_id <= 0:
        # First request, retrieve the most recent tweets
        new_tweets = api.search(q=query, count=tweets_per_request)
    else:
        # Subsequent requests, retrieve tweets older than the max_id from the previous request
        new_tweets = api.search(q=query, count=tweets_per_request, max_id=str(max_id - 1))

    if not new_tweets:
        # No more tweets to retrieve, break out of the loop
        break

    # Add the new tweets to the list of tweets
    tweets.extend(new_tweets)

    # Update the max_id for the next request
    max_id = new_tweets[-1].id

    # Increment the request count
    request_count += 1

# Do something with the tweets
for tweet in tweets:
    print(tweet.text)
