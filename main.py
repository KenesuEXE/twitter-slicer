import argparse
from twitterslicer import *


def main():

    # Command line flags
    parser = argparse.ArgumentParser(description="A Twitter thread maker that slices a text into tweetable chunks.")
    slice_mode = parser.add_mutually_exclusive_group()
    parser.add_argument("file_name", help='insert text file')
    slice_mode.add_argument("-l", "--limit", action="store_true", help='slice to fit Tweet char limit')
    slice_mode.add_argument("-s", "--space", action="store_true", help='slice in whitespace before limit')
    slice_mode.add_argument("-p", "--punct", action="store_true", help='slice in punctuation mark before limit')
    parser.add_argument("-u", "--uncount", action="store_true", help='remove counter')
    parser.add_argument("-t", "--tweet", action="store_true", help='tweet thread directly to Twitter (API keys required)')
    args = parser.parse_args()

    # Open and read text file
    with open(args.file_name) as text_file:
        text = text_file.read()

    # Set counter mode
    if args.uncount:
        counter = False
    else:
        counter = True

    slice_tweets = Slice(text, counter)

    # Set slice mode
    if args.limit:
        tweets = slice_tweets.limit()
    elif args.space:
        tweets = slice_tweets.space()
    elif args.punct:
        tweets = slice_tweets.punct()
    else:
        tweets = slice_tweets.space()

    # Output
    print("Here are your tweets:")
    for tweet in tweets:
        print("\n", tweet)

    # Directly tweet the thread
    if args.tweet:
        tweet_thread(tweets)

    print("\nAll done! Twitter-Slicer shutting down...")

if __name__ == "__main__":
    main()
