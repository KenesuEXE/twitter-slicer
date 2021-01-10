from keys import *
import sys
import textwrap
import tweepy


class Slice:
    def __init__(self, text, counter):
        self.text = text
        self.counter = counter
        self.tweets = []

    def limit(self):

        if self.counter:
            for index in range(0, len(self.text), 272):
                self.tweets.append(self.text[index:index+272] +
                                   " ({}/{})".format(index//272+1, len(self.text)//272+1))

        else:
            for index in range(0, len(self.text), 280):
                self.tweets.append(self.text[index:index+280])

        return self.tweets

    def space(self):

        if self.counter:
            tweets_temp = textwrap.wrap(self.text, width=272)
            for tweet in tweets_temp:
                self.tweets.append(tweet + " ({}/{})".format
                                   (tweets_temp.index(tweet)+1, len(tweets_temp)))

        else:
            self.tweets = textwrap.wrap(self.text, width=280)

        return self.tweets

    def punct(self):
        punct_marks = '.!?'
        index = 0

        if self.counter:
            tweet_temp = []
            count = 1

            while index+272 < len(self.text):
                for punct_search in range(index+272, index-1, -1):
                    if self.text[punct_search] in punct_marks:
                        tweet_temp.append(self.text[index:punct_search+1] +
                                          " ({}/".format(count))
                        index = punct_search+2
                        count += 1
                        break
            tweet_temp.append(self.text[index:len(self.text)] +
                              " ({}/".format(count))

            for tweet in tweet_temp:
                self.tweets.append(tweet + "{})".format(count))

        else:
            while index+280 < len(self.text):
                for punct_search in range(index+280, index-1, -1):
                    if self.text[punct_search] in punct_marks:
                        tweets.append(self.text[index:punct_search+1])
                        index = punct_search+2
                        break
            self.tweets.append(text[index:len(text)])

        return self.tweets


def tweet_thread(tweets):

    print("\nConnecting to Twitter...")
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
    api = tweepy.API(auth)

    try:
        tweet = api.update_status(status=tweets[0])
    except tweepy.error.TweepError:
        sys.exit("ERROR: Invalid API keys")

    print("Tweeting your tweets...")
    for tweet_index in range(1, len(tweets)):
        tweet = api.update_status(status=tweets[tweet_index],
                                  in_reply_to_status_id=tweet.id,
                                  auto_populate_reply_metadata=True)
