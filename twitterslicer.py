"""
Twitter-Slicer by KenesuEXE 2020-2021
Slice text into tweetable chunks
"""
# Tweets are restricted to 280 chars long. The program slices the text
# before the limit or the nearest whitespace/punct mark before the limit
# and optionally adds a counter. The counter is 8 chars long " (00/00)",
# thus tweets with counter will only hold 272 chars at max. The user can
# also indicate where they want it to split using a separator. Finally, the
# user can directly tweet the text to their Twitter, provided they have API keys.


class Slice:
    """Slice text into tweetable chunks"""
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
                while text:  # While text is not empty
                    count += 1
                    self.tweets.append(f"{text[:272]} ({count}/")  # Append the first 272 chars and add current count
                    text = text[272:]  # Replace var text with the remaining text
            self.tweets = [f"{text}{count})" for text in self.tweets]  # Loop back to every tweet and add final count

        # By Limit without counter
        else:
            for text in self.text_list:
                while text:  # While text is not empty
                    self.tweets.append(text[:280])  # Append the first 280 chars
                    text = text[280:]  # Replace var text with the remaining text

        return self.tweets

    def space(self):
        """Slice text in whitespace before tweet limit"""

        # By Space with counter
        if self.counter:
            count = 0
            for text in self.text_list:
                while len(text) > 272:  # While text is longer than limit
                    for index in range(271, -1, -1):  # Start at index 271, loop backwards, and find nearest whitespace
                        if text[index].isspace():
                            count += 1
                            self.tweets.append(f"{text[:index]} ({count}/")  # Append text from start to index and add current count
                            text = text[index+1:]  # Replace var text with remaining text after whitespace
                            break
                    else:  # Slice by limit if no whitespace is found
                        count += 1
                        self.tweets.append(f"{text[:272]} ({count}/")
                        text = text[272:]
                else:  # Append remaining text
                    count += 1
                    self.tweets.append(f"{text} ({count}/")
            self.tweets = [f"{text}{count})" for text in self.tweets]  # Loop back to every tweet and add final count

        # By Space without counter
        else:
            for text in self.text_list:
                while len(text) > 280:  # While text is longer than limit
                    for index in range(279, -1, -1):  # Start at index 279, loop backwards, and find nearest whitespace
                        if text[index].isspace():
                            self.tweets.append(text[:index])  # Append text from start to index
                            text = text[index+1:]  # Replace var text with remaining text after whitespace
                            break
                    else:  # Slice by limit if no whitespace is found
                        self.tweets.append(text[:280])
                        text = text[280:]
                else:  # Append remaining text
                    self.tweets.append(text)

        return self.tweets

    def punct(self):
        """Slice text in punctuation marks before tweet limit"""
        punct_marks = ".?!"

        # By Punctuation with counter
        if self.counter:
            count = 0
            for text in self.text_list:
                while len(text) > 272:  # While text is longer than limit
                    for index in range(271, -1, -1):  # Start at index 271, loop backwards, and find nearest punct mark
                        if text[index] in punct_marks:
                            count += 1
                            self.tweets.append(f"{text[:index+1]} ({count}/")  # Append text from start to index and add current count
                            text = text[index+2:]  # Replace var text with remaining text after punct mark
                            break
                    else:  # Slice by limit if no punct mark is found
                        count += 1
                        self.tweets.append(f"{text[:272]} ({count}/")
                        text = text[272:]
                else:  # Append remaining text
                    count += 1
                    self.tweets.append(f"{text} ({count}/")
            self.tweets = [f"{text}{count})" for text in self.tweets]  # Loop back to every tweet and add final count

        # By Punctuation without counter
        else:
            for text in self.text_list:
                while len(text) > 280:  # While text is longer than limit
                    for index in range(279, -1, -1):  # Start at index 279, loop backwards, and find nearest punct mark
                        if text[index] in punct_marks:
                            self.tweets.append(text[:index+1])  # Append text from start to index
                            text = text[index+2:]  # Replace var text with remaining text after punct mark
                            break
                    else:  # Slice by limit if no punct mark is found
                        self.tweets.append(text[:280])
                        text = text[280:]
                else:  # Append remaining text
                    self.tweets.append(text)

        return self.tweets

    @staticmethod
    def indicated(text, sep):
        """Slice text in indicated separators"""
        text_list = []

        while text:  # While text is not empty

            for index in range(len(text)):  # Search for indicated separator throughout text
                if text[index:index+len(sep)] == sep:
                    text_list.append(text[:index])  # Append from start to index
                    text = text[index+len(sep):]  # Replace var text with the remaining text
                    break
            else:  # Append whole text if no separators found
                text_list.append(text)
                text = None  # Break out of while loop

        text_list = list(filter(None, text_list))

        return text_list


def tweet_thread(tweets):
    """Tweet thread to Twitter"""
    import keys
    import tweepy

    # Authenticate to Twitter
    print("\nConnecting to Twitter...")
    auth = tweepy.OAuthHandler(keys.CONSUMER_KEY, keys.CONSUMER_SECRET)
    auth.set_access_token(keys.ACCESS_KEY, keys.ACCESS_SECRET)
    api = tweepy.API(auth)

    # Tweet the parent/first tweet
    print("Tweeting your tweets...")
    tweet = api.update_status(status=tweets[0])

    # Tweet the rest of the thread
    for tweet_index in range(1, len(tweets)):
        tweet = api.update_status(status=tweets[tweet_index],
                                  in_reply_to_status_id=tweet.id,
                                  auto_populate_reply_metadata=True)
