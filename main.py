import twitterslicer


def main():
    mode_query = input("""
Choose slicing mode:
1 - By limit
2 - By space
3 - By punctuation
    \n""")

    counter_query = input("""
Choose counter mode:
1 - Yes
2 - No
    \n""")

    output_query = input("""
Choose output mode:
1 - Print here in console
2 - Tweet directly to Twitter
    \n""")

    if counter_query == "1":
        counter = True
    elif counter_query == "2":
        counter = False
    else:  # Wrong Input
        counter = True
        print("\nCounter mode input error, set to default: True")

    if mode_query == "1":
        tweets = twitterslicer.by_limit(text, counter)
    elif mode_query == "2":
        tweets = twitterslicer.by_space(text, counter)
    elif mode_query == "3":
        tweets = twitterslicer.by_punctuation(text, counter)
    else:  # Wrong  input
        tweets = twitterslicer.by_punctuation(text, counter)
        print("\nSlicing mode input error, set to default: Punctuation")

    if output_query == "1":
        twitterslicer.print_tweets(tweets)
    elif output_query == "2":
        twitterslicer.create_twitter_thread(tweets)
    else:  # Wrong Input
        print("\nOutput mode input error, set to default: Print Tweets")
        twitterslicer.print_tweets(tweets)
 

if __name__ == "__main__":    
    print("TWITTER SLICER v2 by KenesuEXE\n")

    while True:  # Loops script so it can be used multiple times

        with open('texthere.txt') as f:  # Open and read texthere.txt
            text = f.read()
            if text == "":  # Check if texthere.txt is blank
                print("Paste your text first in texthere.txt")
                break
        
        main()
