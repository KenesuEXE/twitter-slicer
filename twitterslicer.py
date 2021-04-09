class Slice:
    def __init__(self, text_list, counter):
        self.text_list = text_list
        self.counter = counter
        self.tweets = []

    def limit(self):
        """Slice text to fit tweet character limit"""

        # By limit with counter
        if self.counter:
            count = 0
            for text in self.text_list:
                while text:
                    count += 1
                    self.tweets.append(f"{text[:272]} ({count}/")
                    text = text[272:]
            self.tweets = [f"{text}{count})" for text in self.tweets]

        # By Limit without counter
        else:
            for text in self.text_list:
                while text:
                    self.tweets.append(text[:280])
                    text = text[280:]

        return self.tweets

    def space(self):
        """Slice text in whitespace before tweet limit"""

        # By Space with counter
        if self.counter:
            count = 0
            for text in self.text_list:
                while len(text) > 272:
                    for index in range(271,-1,-1):
                        if text[index].isspace():
                            count += 1
                            self.tweets.append(f"{text[:index]} ({count}/")
                            text = text[index+1:]
                            break
                    else:
                        count += 1
                        self.tweets.append(f"{text[:272]} ({count}/")
                        text = text[272:]
                else:
                    count += 1
                    self.tweets.append(f"{text} ({count}/")
            self.tweets = [f"{text}{count})" for text in self.tweets]

        # By Space without counter
        else:
            for text in self.text_list:
                while len(text) > 280:
                    for index in range(279,-1,-1):
                        if text[index].isspace():
                            self.tweets.append(text[:index])
                            text = text[index+1:]
                            break
                    else:
                        self.tweets.append(text[:280])
                        text = text[280:]
                else:
                    self.tweets.append(text)

        return self.tweets

    def punct(self):
        """Slice text in punctuation marks before tweet limit"""
        punct_marks = ".?!"

        # By Punctuation with counter
        if self.counter:
            count = 0
            for text in self.text_list:
                while len(text) > 272:
                    for index in range(271,-1,-1):
                        if text[index] in punct_marks:
                            count += 1
                            self.tweets.append(f"{text[:index+1]} ({count}/")
                            text = text[index+2:]
                            break
                    else:
                        count += 1
                        self.tweets.append(f"{text[:272]} ({count}/")
                        text = text[272:]
                else:
                    count += 1
                    self.tweets.append(f"{text} ({count}/")
            self.tweets = [f"{text}{count})" for text in self.tweets]

        # By Punctuation without counter
        else:
            for text in self.text_list:
                while len(text) > 280:
                    for index in range(279,-1,-1):
                        if text[index] in punct_marks:
                            self.tweets.append(text[:index+1])
                            text = text[index+2:]
                            break
                    else:
                        self.tweets.append(text[:280])
                        text = text[280:]
                else:
                    self.tweets.append(text)

        return self.tweets

    @staticmethod
    def indicated(text, sep):
        """Slice text in indicated separators"""
        text_list = []

        while text:

            for index in range(len(text)):
                if text[index:index+len(sep)] == sep:
                    text_list.append(text[:index])
                    text = text[index+len(sep):]
                    break
            else:
                text_list.append(text)
                text = None
    
        text_list = list(filter(None, text_list))
    
        return text_list


def tweet_thread(tweets):
    """Tweet thread to Twitter"""
    import keys
    import tweepy

    print("\nConnecting to Twitter...")
    auth = tweepy.OAuthHandler(keys.CONSUMER_KEY, keys.CONSUMER_SECRET)
    auth.set_access_token(keys.ACCESS_KEY, keys.ACCESS_SECRET)
    api = tweepy.API(auth)

    # Tweet the first tweet
    print("Tweeting your tweets...")
    tweet = api.update_status(status=tweets[0])

    # Tweet the rest of the thread
    for tweet_index in range(1, len(tweets)):
        tweet = api.update_status(status=tweets[tweet_index],
                                  in_reply_to_status_id=tweet.id,
                                  auto_populate_reply_metadata=True)
