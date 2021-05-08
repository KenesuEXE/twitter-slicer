import argparse
import twitterslicer as ts


def main():

    # Command line flags
    parser = argparse.ArgumentParser(description="a Twitter thread maker that slices a text into tweetable chunks.")
    slice_mode = parser.add_mutually_exclusive_group()
    parser.add_argument("file_name", help='insert text file name')
    slice_mode.add_argument("-l", "--limit", action="store_true", help='slice to fit Tweet char limit')
    slice_mode.add_argument("-s", "--space", action="store_true", help='slice in whitespace before limit, set to default')
    slice_mode.add_argument("-p", "--punct", action="store_true", help='slice in punctuation mark before limit')
    parser.add_argument("-u", "--uncount", action="store_true", help='remove counter')
    parser.add_argument("-t", "--tweet", action="store_true", help='tweet thread directly to Twitter (API keys required)')
    parser.add_argument("-sep", "--separator", default="\\", help='set separation indicator, default set to \\')
    args = parser.parse_args()

    # Retrieve text
    with open(args.file_name) as text_file:
        text = text_file.read()
    if text == "":
        raise Exception("Text file should contain text")

    # Set separator and slice on indicated chars
    sep = args.separator

    text_list = ts.Slice.indicated(text, sep)

    # Set counter and slicing mode
    has_counter = False if args.uncount else True

    Slice = ts.Slice(text_list, has_counter)

    if args.limit:
        tweets = Slice.limit()
    elif args.space:
        tweets = Slice.space()
    elif args.punct:
        tweets = Slice.punct()
    else:
        tweets = Slice.space()

    # Print output
    print("Here are your tweets:")
    for tweet in tweets:
        print("\n", tweet)

    # Create Twitter thread
    if args.tweet:
        ts.tweet_thread(tweets)

    print("\nAll done! Twitter Slicer shutting down...")

if __name__ == "__main__":
    main()
