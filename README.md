# The TWITTER SLICER
**A Twitter thread maker that slices a text into tweetable chunks.**  

## Functions
### Slicing Modes 
**By Limit**   *-l* or *--limit*   
Slice text into strictly 280-character chunks to maximize Tweet limit.  

**By Space** *-s*   or *--space* *(default)*    
Slice text in the nearest whitespace before the Tweet limit.  

**By Punctuation**   *-p* or *--punct*  
Slice text in the nearest punctuation mark before the Tweet limit.  

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
2. Add a text file in the same directory
3. If you plan to use the Tweeting function, insert your API keys in `keys.py`
4. Run `main.py` along with the command-line parameters. One such command can look like this:
```
python main.py my_tweet.txt -l -t
```
5. All done! The tweets should be printed in the console or automatically tweeted.

*Note: This is a beginner project, do not expect high quality since I am still learning, suggestions and helpful criticisms are welcome. :)*  

MIT © KenesuEXE  
Dec 2020 - Jan 2021
