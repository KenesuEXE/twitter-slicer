#The TWITTER SLICER

#made by: KenesuEXE
#date: 18/12/20 — ???

#Slice a big body of text into tweetable chunks!

#The output list
result = []

#Raw Slice
#Slice the text into strictly 280-character chunks.
def raw_slice(text):
  global result
  for x in range(0, len(text), 280): #x = 0, 280, 560, ...
    result.append(text[x:x+280]) #Append characters with index 0-279, then 280-559, and so on.
  return result
  
#Input
#Paste your text here
raw_slice("I have come to think that life is a far more limited thing than those in the midst of its maelstrom realize. The light shines into the act of life for only the briefest moment—perhaps only a matter of seconds. Once it is gone and one has failed to grasp its offered revelation, there is no second chance. One may have to live the rest of one’s life in hopeless depths of loneliness and remorse. In that twilight world, one can no longer look forward to anything. All that such a person holds in his hands is the withered corpse of what should have been.")

#Output
#Print list into presentable and ready to be tweeted chunks
for num in range(0, len(result)):
  print ("\n")
  print (result[num])