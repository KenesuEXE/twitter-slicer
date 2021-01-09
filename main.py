import argparse
import sys
from twitterslicer import *


def main():
    parser = argparse.ArgumentParser(description='Slices text into a tweetable chunks to make a Twitter thread')
    slice_mode = parser.add_mutually_exclusive_group()
    parser.add_argument("file_name", help='text file name containing text to be sliced')
    slice_mode.add_argument("-l", "--limit", action="store_true", help='slice to fit Tweet limit')
    slice_mode.add_argument("-s", "--space", action="store_true", help='slice in whitespaces')
    slice_mode.add_argument("-p", "--punct", action="store_true", help='slice in punctuation marks')
    parser.add_argument("-u", "--uncount", action="store_true", help='remove counter')
    parser.add_argument("-t", "--tweet", action="store_true", help='tweet thread directly to Twitter')
    args = parser.parse_args()

    try:
        with open(args.file_name) as text_file:
            text = text_file.read()
    except FileNotFoundError:
        sys.exit("ERROR: No such file or directory " + args.file_name)

    if args.uncount:
        counter = False
    else:
        counter = True

    slice_tweets = Slice(text, counter)
    if args.limit:
        tweets = slice_tweets.limit()
    elif args.space:
        tweets = slice_tweets.space()
    elif args.punct:
        tweets = slice_tweets.punct()
    else:
        tweets = slice_tweets.space()

    print("Here are your tweets:")
    for tweet in tweets:
        print("\n", tweet)

    if args.tweet:
        tweet_thread(tweets)

    print("\nAll done! Twitter-Slicer shutting down...")

if __name__ == "__main__":
    print("\nThe TWITTER-SLICER v2")
    print("by KenesuEXE\n\n")
    main()
