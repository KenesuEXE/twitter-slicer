import textwrap
import tweepy
from keys import *

def by_limit(text, counter):
    tweets = []
    count = 1

    if counter:  # By Limit with Counter
        for i in range(0, len(text), 272):  # Append text with index 0-272, plus a counter which is 8 characters long, then repeat.
            tweets.append(text[i:i+272] + " ({}/{})".format(count, len(text)//272+1))
            count += 1

    else:  # By Limit without Counter
        for i in range(0, len(text), 280):  # Append text with index 0-280, and so on.
            tweets.append(text[i:i+280])

    return tweets


def by_space(text, counter):
    tweets = []
    count = 1

    if counter:  # By Space with Counter
        for tweet in textwrap.wrap(text, width=272):  # Use textwrap.wrap module to cut to the nearest whitespace, plus a counter.
            tweets.append(tweet + " ({}/{})".format(count, len(text)//272+1))
            count += 1

    else:  # By Space without Counter
        tweets = textwrap.wrap(text, width=280)

    return tweets


def by_punctuation(text, counter):
    tweets = []
    punct_marks = ".!?;"  # Sentence ending punctuations
    count = 1
    index = 0

    if counter:  # By Punctuation with Counter
        tweet_temp = []  # Temporary list
        while index+272 < len(text):  # If the remaining text still has more than 272 (+8 for counter) characters, we must cut.
            for punct_search in range(index+272, index-1, -1):  # From the 280th, go backwards and find the nearest punctuation mark.
                if text[punct_search] in punct_marks:
                    tweet_temp.append(text[index:punct_search+1] + " ({}/".format(count))  # Append from starting index up to punctuation mark. Since we can't yet find the total number of tweets we will be creating, we'll add the denominator later.
                    index = punct_search+2  # New starting index at the next word
                    count += 1
                    break  # Go back to while loop
        tweet_temp.append(text[index:len(text)] + " ({}/".format(count))  # No more cutting needed, append remaining words.
        for tweet in tweet_temp:  # Call all tweets and add the denominator in the counter since we now know the total amount of tweets created. Remember format " ({}/{})".
            tweets.append(tweet + "{})".format(count))

    else:  # By Punctuation without Counter
        while index+280 < len(text):  # Same thing as above, without the complex counter
            for punct_search in range(index+280, index-1, -1):
                if text[punct_search] in punct_marks:
                    tweets.append(text[index:punct_search+1])
                    index = punct_search+2
                    break
        tweets.append(text[index:len(text)])

    return tweets


def print_tweets(tweets):
    print("\nHere are your tweets:")
    for tweet in tweets:  # Prints all elements in list 'tweets'.
        print("\n", tweet)
    print("\nAll Done!")

def create_twitter_thread(tweets):

    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
    api = tweepy.API(auth)

    count = 0
    print("\nTweeting tweet #1")
    tweet = api.update_status(status=tweets[0])
    while count <= len(tweets) - 2:

        count += 1
        print("\nTweeting tweet #" + str(count+1))
        tweet = api.update_status(status=tweets[count], in_reply_to_status_id=tweet.id, auto_populate_reply_metadata=True)

    print("\nAll Done!")