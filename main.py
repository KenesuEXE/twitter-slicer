import twitterslicer

print("""
The TWITTER SLICER
by KenesuEXE \n
""")

text = input ("""
Paste your text here:
(If you want to use a sample text, input 'sample')
\n""")

if text == 'sample':
  text = twitterslicer.sample

mode = input ("""
Pick a slicing mode:
1 - By limit
2 - By space
3 - By punctuation
\n""")

count = input("""
Add counter?
1 - Yes
2 - No
\n""")

if count.lower() == "1":
  counter = True
elif count.lower() == "2":
  counter = False
else:
  counter = True
  print ("\nCounter input error, set to default: True")
  
if mode == "1":
  tweets = twitterslicer.by_limit(text, counter)
elif mode == "2":
  tweets = twitterslicer.by_space(text, counter)
elif mode == "3":
  tweets = twitterslicer.by_punctuation(text, counter)
else:
  print("\nMode input error, set to default: Punctuation")
  tweets = twitterslicer.by_punctuation(text, counter)
  
for tweet in tweets:
  print ("\n", tweet)
