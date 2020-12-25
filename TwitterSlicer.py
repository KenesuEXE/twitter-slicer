#The TWITTER SLICER

#made by: @KenesuEXE u/KnnthKnnth
#date: 18/12/20 — 25/12/20

#Slice a big body of text into tweetable chunks!

#Raw Slice
#Slices the text into strictly 280-character chunks.
def raw_slice(text):
  result1 = []
  for x in range(0, len(text), 280): #x = 0, 280, 560, ...
    result1.append(text[x:x+280]) #Append chars with index 0-279, then 280-559, and so on.
  return result1

#Clean Slice
#Will not slice in the middle of words, instead cuts in the nearest whitespace.
def clean_slice(text):
  result2 = []
  x = 0
  while x+280 < len(text): #Gets the first 280 chars.
    for y in range(x+280, x-1, -1): #Starting from the 280th, go backwards  and find  the nearest whitespace.
      if text[y].isspace():
        result2.append(text[x:y]) #Append from start up to the last word.
        x = y + 1 #The new starting point will be where we have just cutted it.
        break
  result2.append(text[x:len(text)]) #No more cutting needed, append the remaining words.
  return result2


#Counted Slice
#Includes a counter that displays the current tweet number over the total number of tweets in the thread.
#The counter is 8 chars long in the format (00/00).
def raw_counted_slice(text):
  result3 = []
  for x in range(0, len(text), 272): #280 minus 8 chars to make space for counter.
    result3.append(text[x:x+272] + " ({}/{})".format(x//272+1, len(text)//272+1))
  return result3

def clean_counted_slice(text):
  result4 = []
  x = 0
  while x+272 < len(text):
    for y in range(x+272, x-1, -1):
      if text[y].isspace():
        result4.append(text[x:y] + " ({}/{})".format(y//272+1, len(text)//272+1))
        x = y + 1 
        break
  result4.append(text[x:len(text)] + " ({}/{})".format(len(text)//272+1, len(text)//272+1))
  return result4


#INPUT
#Paste your text here! 
rs = raw_slice("""
I have come to think that life is a far more limited thing than those in the midst of its maelstrom realize. The light shines into the act of life for only the briefest moment—perhaps only a matter of seconds. Once it is gone and one has failed to grasp its offered revelation, there is no second chance. One may have to live the rest of one’s life in hopeless depths of loneliness and remorse. In that twilight world, one can no longer look forward to anything. All that such a person holds in his hands is the withered corpse of what should have been.
""")

cs = clean_slice("""
I have come to think that life is a far more limited thing than those in the midst of its maelstrom realize. The light shines into the act of life for only the briefest moment—perhaps only a matter of seconds. Once it is gone and one has failed to grasp its offered revelation, there is no second chance. One may have to live the rest of one’s life in hopeless depths of loneliness and remorse. In that twilight world, one can no longer look forward to anything. All that such a person holds in his hands is the withered corpse of what should have been.
""")

rcs = raw_counted_slice("""
I have come to think that life is a far more limited thing than those in the midst of its maelstrom realize. The light shines into the act of life for only the briefest moment—perhaps only a matter of seconds. Once it is gone and one has failed to grasp its offered revelation, there is no second chance. One may have to live the rest of one’s life in hopeless depths of loneliness and remorse. In that twilight world, one can no longer look forward to anything. All that such a person holds in his hands is the withered corpse of what should have been.
""")

ccs = clean_counted_slice("""
I have come to think that life is a far more limited thing than those in the midst of its maelstrom realize. The light shines into the act of life for only the briefest moment—perhaps only a matter of seconds. Once it is gone and one has failed to grasp its offered revelation, there is no second chance. One may have to live the rest of one’s life in hopeless depths of loneliness and remorse. In that twilight world, one can no longer look forward to anything. All that such a person holds in his hands is the withered corpse of what should have been.
""")

#OUTPUT
print("\n Raw Slice")
for e in rs:
  print ('\n')
  print (e)
  
print("\n Clean Slice")
for e in cs:
  print ('\n')
  print (e)

print("\n Raw Counted Slice")
for e in rcs:
  print ('\n')
  print (e)

print("\n Clean Counted Slice")
for e in ccs:
  print ('\n')
  print (e)
