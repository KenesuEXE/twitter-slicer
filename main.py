import twitter-slicer.py

print("""
The TWITTER SLICER
Slice your lengthy text into tweetable chunks!

made by: @KenesuEXE, u/KnnthKnnth
""")

text = input("Paste your text here: (or of you want a sample text, type 'example')\n")
text = example if text == "example"

mode = input("""
Select Mode
1 - Raw Slice
2 - Clean Slice \n
""")

counter = input("Add counter? (Y/N) \n")

