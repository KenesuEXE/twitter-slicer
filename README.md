# TWITTER-SLICER  
*Slice your text into tweetable chunks!*
The Twitter-Slicer that helps you make a Twitter thread by cutting your text (in a txt file) into tweetable portions that you can either manually copy-paste and tweet, or tweet directly (API keys required)

## How To Use
1. Clone repository by using `git clone https://github.com/KenesuEXE/twitter-slicer`
2. Paste a .txt file containing your text. You can indicate separators (default is \\) to slice where its located.
3. Run program using `python main.py [text_file_name] [other arguments]`

## Functions
### Slicing Modes 
**By Limit** *-l* or *--limit*   
Slice text into strictly 280-character chunks to maximize Tweet limit.  

**By Space** *-s* or *--space* *(default)*    
Slice text in the nearest whitespace before the Tweet limit.  

**By Punctuation** *-p* or *--punct*  
Slice text in the nearest punctuation mark before the Tweet limit.  

### Other Functions
**Change Separator** *-sep ** or *--separator **  
Slice text in indicated separators stated in your text.  Default set to \ .

**Uncount** *-u* or *--uncount*   
Remove the counter from your tweets.   

**Auto-Tweet** *-t* or *--tweet*   
Directly tweet the thread to Twitter. Twitter API keys required.

You can also view this by using `python main.py -h`

## Example
Here are some examples on how to run the program:   

`python main.py text_here.txt`  
*slices the text by space with counter(default)*  

`python main.py my_tweet.txt -p -t -s *`  
*slices the text by punctuations, change separator to asterisk, and auto-Tweet.*      

`python main.py thoughts_on_cats.txt --uncount --limit`  
*slices the text by Tweet limit and removes the counter*  


MIT © KenesuEXE  
Dec 2020 - Apr 2021
