# TWITTER-SLICER
The Twitter-Slicer is a Python program that helps you make a Twitter 
thread by cutting a text in a file into tweetable parts that you
can Tweet directly (using Tweepy) or copy-paste to Twitter.

## Functions
### Slicing Modes 
**By Limit**   *-l* or *--limit*   
Slice text into strictly 280-character chunks to maximize Tweet limit.  

**By Space** *-s*   or *--space* *(default)*    
Slice text in the nearest whitespace before the Tweet limit.  

**By Punctuation**   *-p* or *--punct*  
Slice text in the nearest punctuation mark before the Tweet limit.  

### Other Functions
**Uncount** *-u* or *--uncount*   
Remove the counter from your tweets.   

**Auto-Tweet** *-t* or *--tweet*   
Directly tweet the thread to Twitter. Twitter API keys required.

You can also view this by using either:
```
python main.py -h
python main.py --help
```
## How To Use
1. Clone repository. One way you can do it is using:
```
gh repo clone KenesuEXE/twitter-slicer
```
2. Install tweepy using: `pip install tweepy`
3. Add a text file in the same directory
4. If you plan to use the auto-tweeting function, insert your API keys in `keys.py`
5. Run `main.py` along with the command-line parameters.
6. All done! The tweets should be printed in the console or automatically tweeted.

## Example
Here are some examples on how to run the program:   

`python main.py text_here.txt`  
*slices the text by space (default)*  

`python main.py my_tweet.txt -p -t`  
*slices the text by punctuations and auto-Tweets it.*      

`python main.py thoughts_on_cats.txt --uncount --limit`  
*slices the text by Tweet limit and removes the counter*  

*Note: This is a beginner project, do not expect high quality since I am still learning, suggestions and helpful criticisms are welcome. :)*  

MIT © KenesuEXE  
Dec 2020 - Jan 2021
