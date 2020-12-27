import twitterslicer

print("""
The TWITTER SLICER
Slice your lengthy text into tweetable chunks!
made by: KenesuEXE — u/KnnthKnnth\n
""")

text = input("""
Paste your text here:
(If you want a sample text, input 'example') \n
""")
if text == "example":
  text = twitterslicer.example

mode = input("""
Choose a slicing mode:
1 - Raw Slice
2 - Clean Slice
3 - Raw Counted Slice
4 - Clean Counted Slice \n
""")

if mode == "1":
  tweets = twitterslicer.raw_slice(text)
elif mode == "2":
  tweets = twitterslicer.clean_slice(text)
elif mode == "3":
  tweets = twitterslicer.raw_counted_slice(text)
elif mode == "4":
  tweets = twitterslicer.clean_counted_slice(text)

for chunks in tweets:
  print("\n", chunks)
