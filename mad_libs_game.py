"""
This program is a mini game (called Mad Libs) where you can ask your friends some words (like adjectives, nouns, etc.) and then those words will fill the hidden story.
Author: Karsi_
"""

# The template for the story

STORY = """""""""This morning %s woke up feeling %s. 
'It is going to be a %s day!' 
Outside, a bunch of %ss were protesting to keep %s in stores. 
They began to %s to the rhythm of the %s, which made all the %ss very %s. 
Concerned, %s texted %s, who flew %s to %s and dropped %s in a puddle of frozen %s. 
%s woke up in the year %s, in a world where %ss ruled the world. """""""""

print ("Time to play")

madlibs = []
madlibs.append (input("Enter a name: "))
madlibs.append (input("Enter an adjetive: "))
madlibs.append (input("Enter another adjetive: "))
madlibs.append (input("Enter an animal: "))
madlibs.append (input("Enter some food: "))
madlibs.append (input("Enter a verb: "))
madlibs.append (input("Enter a noun: "))
madlibs.append (input("Enter a fruit: "))
madlibs.append (input("Enter one more adjetive: "))
madlibs.append (input("Enter a name: "))
madlibs.append (input("Enter a superhero: "))
madlibs.append (input("Enter a name: "))
madlibs.append (input("Enter a country: "))
madlibs.append (input("Enter a name: "))
madlibs.append (input("Enter a dessert: "))
madlibs.append (input("Enter a name: "))
madlibs.append (input("Enter a year: "))
madlibs.append (input("Enter another noun: "))

print (STORY % (madlibs[0], madlibs[1], madlibs[2], madlibs[3], madlibs[4], madlibs[5], madlibs[6], madlibs[7], madlibs[8], madlibs[9], madlibs[10], madlibs[11], madlibs[12], madlibs[13], madlibs[14], madlibs[15], madlibs[16], madlibs[17]))
