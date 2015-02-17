"""
Return a random text when answer Yes to Prompt
"""


from loremipsum import Generator



answer = input("Do you want to see random text (yes or no)")
#if the the input is not yes or no ,  keep prompting for a valid answer
while answer.lower() not in ("yes", 'y', 'n', "no"):
     answer = input("What is your name:) ")
     
if answer.lower() == 'yes' or answer.lower() == 'y':
   g = Generator() 
 #  g.dictonary = ["I", ["code", "develop", "consult"], "east mode", "Python"] 
   g.sentence_mean = 20 #sentence length in words. 
   text = g.generate_sentence()
   print(text[2:])

else:
   print("Maybe next time")
