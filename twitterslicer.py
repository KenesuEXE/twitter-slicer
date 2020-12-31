import textwrap

tweets = []
count = 1

def by_limit(text, counter):
  global tweets, count
  if counter:
    for i in range(0, len(text), 272):
      tweets.append(text[i:i+272] + " ({}/{})".format(count, len(text)//272+1))
      count += 1
  else:
    for i in range(0, len(text), 280):
     tweets.append(text[i:i+280])
  return tweets

def by_space(text, counter):
  global tweets, count
  if counter:
    for tweet in textwrap.wrap(text, width=272):
      tweets.append(tweet + " ({}/{})".format(count, len(text)//272+1))
      count += 1
  else:
    tweets = textwrap.wrap(text, width=280)
  return tweets
  
def by_punctuation(text, counter):
  global tweets, count
  punct_marks = ".?!;" 
  index = 0
  if counter:
    tweet_temp = []
    while index+280 < len(text):
      for punct_search in range (index+272, index-1, -1):
        if text[punct_search] in punct_marks:
          tweet_temp.append(text[index:punct_search+1] + " ({}/".format(count, count))
          index = punct_search+2
          count += 1
          break
    tweet_temp.append(text[index:len(text)] + " ({}/".format(count, count))
    for e in tweet_temp:
      tweets.append(e + "{})".format(count))
  else:
    while index+280 < len(text):
      for punct_search in range (index+280, index-1, -1):
        if text[punct_search] in punct_marks:
          tweets.append(text[index:punct_search+1])
          index = punct_search+2
          break
    tweets.append(text[index:len(text)])
  return tweets

sample = "Wowwwww, you meow like a cat! That means you are one, right? Shut the fuck up. If you really want to be put on a leash and treated like a domestic animal then that’s called a fetish, not “quirky” or “cute”. What part of you seriously thinks that any part of acting like a feline establishes a reputation of appreciation? Is it your lack of any defining aspect of personality that urges you to resort to shitty representations of cats to create an illusion of meaning in your worthless life? Wearing “cat ears” in the shape of headbands further notes the complete absence of human attribution to your false sense of personality, such as intelligence or charisma in any form or shape. Where do you think this mindset’s gonna lead you? You think you’re funny, random, quirky even? What makes you think that acting like a fucking cat will make a goddamn hyena laugh? I, personally, feel extremely sympathetic towards you as your only escape from the worthless thing you call your existence is to pretend to be an animal. But it’s not a worthy choice to assert this horrifying fact as a dominant trait, mainly because personality traits require an initial personality to lay their foundation on. You’re not worthy of anybody’s time, so go fuck off, “cat-girl”."
