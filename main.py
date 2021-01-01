import twitterslicer


def main():
    mode_query = input("""
Pick a slicing mode:
1 - By limit
2 - By space
3 - By punctuation
    \n""")

    counter_query = input("""
Add counter?
1 - Yes
2 - No
    \n""")

    if counter_query == "1":
        counter = True
    elif counter_query == "2":
        counter = False
    else:  # Wrong Input
        counter = True
        print("\nCounter input error, set to default: True")

    if mode_query == "1":
        tweets = twitterslicer.by_limit(text, counter)
    elif mode_query == "2":
        tweets = twitterslicer.by_space(text, counter)
    elif mode_query == "3":
        tweets = twitterslicer.by_punctuation(text, counter)
    else:  # Wrong  input
        tweets = twitterslicer.by_punctuation(text, counter)
        print("\nMode input error, set to default: Punctuation")

    print("\nHere are your tweets:")
    for tweet in tweets:  # Prints all elements in list 'tweets'.
        print("\n", tweet)

if __name__ == "__main__":    
    print("TWITTER SLICER v2 by KenesuEXE\n")

    while True:  # Loops script so it can be used multiple times

        with open('texthere.txt') as f:  # Open and read texthere.txt
            text = f.read()
            if text == "":  # Check if texthere.txt is blank
                print("Paste your text first in texthere.txt")
                break
        
        main()
