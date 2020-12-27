#Raw Slice
#Slices the text into strictly 280-character chunks.
def raw_slice(text):
  rs = []
  for i in range(0, len(text), 280): #i = 0, 280, 560, ...
    rs.append(text[i:i+280]) #Append chars with index 0-279, then 280-559, and so on.
  return rs

#Clean Slice
#Will not slice in the middle of words, instead cuts in the nearest whitespace.
def clean_slice(text):
  cs = []
  i = 0
  while i+280 < len(text): #Gets the first 280 chars.
    for z in range(i+280, i-1, -1): #Starting from the 280th, go backwards  and find the nearest whitespace.
      if text[z].isspace():
        cs.append(text[i:z]) #Append from start up to the last word.
        i = z + 1 #The new starting point will be where we have just cutted it.
        break
  cs.append(text[i:len(text)]) #No more cutting needed, append remaining words.
  return cs


#Counted Slice
#Includes a thread counter which is 8 chars long in the format " (00/00)".
def raw_counted_slice(text):
  rcs = []
  for i in range(0, len(text), 272): #280 minus 8 chars to make space for counter.
    rcs.append(text[i:i+272] + " ({}/{})".format(i//272+1, len(text)//272+1))
  return rcs

def clean_counted_slice(text):
  ccs = []
  i = 0
  while i+272 < len(text):
    for z in range(i+272, i-1, -1):
      if text[z].isspace():
        ccs.append(text[i:z] + " ({}/{})".format(z//272+1, len(text)//272+1))
        i = z + 1 
        break
  ccs.append(text[i:len(text)] + " ({}/{})".format(len(text)//272+1, len(text)//272+1))
  return ccs

#its the navy seal copypasta lmfaoooo
example = "What the fuck did you just fucking say about me, you little bitch? I'll have you know I graduated top of my class in the Navy Seals, and I've been involved in numerous secret raids on Al-Quaeda, and I have over 300 confirmed kills. I am trained in gorilla warfare and I'm the top sniper in the entire US armed forces. You are nothing to me but just another target. I will wipe you the fuck out with precision the likes of which has never been seen before on this Earth, mark my fucking words. You think you can get away with saying that shit to me over the Internet? Think again, fucker. As we speak I am contacting my secret network of spies across the USA and your IP is being traced right now so you better prepare for the storm, maggot. The storm that wipes out the pathetic little thing you call your life. You're fucking dead, kid. I can be anywhere, anytime, and I can kill you in over seven hundred ways, and that's just with my bare hands. Not only am I extensively trained in unarmed combat, but I have access to the entire arsenal of the United States Marine Corps and I will use it to its full extent to wipe your miserable ass off the face of the continent, you little shit. If only you could have known what unholy retribution your little \"clever\" comment was about to bring down upon you, maybe you would have held your fucking tongue. But you couldn't, you didn't, and now you're paying the price, you goddamn idiot. I will shit fury all over you and you will drown in it. You're fucking dead, kiddo."
