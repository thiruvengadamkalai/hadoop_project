#!/usr/bin/env python
import sys
import string
import json

tweets = []
#badwords = []
#f = open('part-00030','r+')
for line in sys.stdin:
  #print line
  tweets.append(json.loads(line))
#f1=open('bad.txt','r+')
#for line in f1:
  #badwords.append(line.strip())
#print badwords
badwords =['Alcoholic', 'Amateur', 'Analphabet', 'Anarchist', 'Ape', 'Arse', 'Arselicker', 'Ass', 'Ass master', 'Ass-kisser', 'Ass-nugget', 'Ass-wipe', 'Asshole', 'Baby', 'Backwoodsman', 'Balls', 'Bandit', 'Barbar', 'Bastard', 'Bastard', 'Beavis', 'Beginner', 'Biest', 'Bitch', 'Blubber gut', 'Bogeyman', 'Booby', 'Boozer', 'Bozo', 'Brain-fart', 'Brainless', 'Brainy', 'Brontosaurus', 'Brownie', 'Bugger', 'Bugger, silly', 'Bulloks', 'Bum', 'Bum-fucker', 'Butt', 'Buttfucker', 'Butthead', 'Callboy', 'Callgirl', 'Camel', 'Cannibal', 'Cave man', 'Chaavanist', 'Chaot', 'Chauvi', 'Cheater', 'Chicken', 'Children fucker', 'Clit', 'Clown', 'Cock', 'Cock master', 'Cock up', 'Cockboy', 'Cockfucker', 'Cockroach', 'Coky', 'Con merchant', 'Con-man', 'Country bumpkin', 'Cow', 'Creep', 'Creep', 'Cretin', 'Criminal', 'Cunt', 'Cunt sucker', 'Daywalker', 'Deathlord', 'Derr brain', 'Desperado', 'Devil', 'Dickhead', 'Dinosaur', 'Disguesting packet', 'Diz brain', 'Do-Do', 'Dog', 'Dog, dirty', 'Dogshit', 'Donkey', 'Drakula', 'Dreamer', 'Drinker', 'Drunkard', 'Dufus', 'Dulles', 'Dumbo', 'Dummy', 'Dumpy', 'Egoist', 'Eunuch', 'Exhibitionist', 'Fake', 'Fanny', 'Farmer', 'Fart', 'Fart, shitty', 'Fatso', 'Fellow', 'Fibber', 'Fish', 'Fixer', 'Flake', 'Flash Harry', 'Freak', 'Frog', 'Fuck', 'Fuck face', 'Fuck head', 'Fuck noggin', 'Fucker', 'Gangster', 'Ghost', 'Goose', 'Gorilla', 'Grouch', 'Grumpy', 'Head', 'Hell dog', 'Hillbilly', 'Hippie', 'Homo', 'Homosexual', 'Hooligan', 'Horse fucker', 'Idiot', 'Ignoramus', 'Jack-ass', 'Jerk', 'Joker', 'Junkey', 'Killer', 'Lard face', 'Latchkey child', 'Learner', 'Liar', 'Looser', 'Lucky', 'Lumpy', 'Luzifer', 'Macho', 'Macker', 'Man, old', 'Minx', 'Missing link', 'Monkey', 'Monster', 'Motherfucker', 'Mucky pub', 'Mutant', 'Neanderthal', 'Nerfhearder', 'Nobody', 'Nurd', 'Nuts, numb', 'Oddball', 'Oger', 'Oil dick', 'Old fart', 'Orang-Uthan', 'Original', 'Outlaw', 'Pack', 'Pain in the ass', 'Pavian', 'Pencil dick', 'Pervert', 'Pig', 'Piggy-wiggy', 'Pirate', 'Pornofreak', 'Prick', 'Prolet', 'Queer', 'Querulant', 'Rat', 'Rat-fink', 'Reject', 'Retard', 'Riff-Raff', 'Ripper', 'Roboter', 'Rowdy', 'Rufian', 'Sack', 'Sadist', 'Saprophyt', 'Satan', 'Scarab', 'Schfincter', 'Shark', 'Shit eater', 'Shithead', 'Simulant', 'Skunk', 'Skuz bag', 'Slave', 'Sleeze', 'Sleeze bag', 'Slimer', 'Slimy bastard', 'Small pricked', 'Snail', 'Snake', 'Snob', 'Snot', 'Son of a bitch', 'Square', 'Stinker', 'Stripper', 'Stunk', 'Swindler', 'Swine', 'Teletubby', 'Thief', 'Toilett cleaner', 'Tussi', 'Typ', 'Unlike', 'Vampir', 'Vandale', 'Varmit', 'Wallflower', 'Wanker', 'Wanker, bloody', 'Weeze Bag', 'Whore', 'Wierdo', 'Wino', 'Witch', 'Womanizer', 'Woody allen', 'Worm', 'Xena', 'Xenophebe', 'Xenophobe', 'XXX Watcher', 'Yak', 'Yeti', 'Zit face']

for tweet in tweets:
  message=tweet['text']
  word_count = 0  
  bad_count = 0
  for word in message.split(' '):
    word_count +=1
    if word in badwords:
      bad_count += 1
  print '%s\t%s' % (word_count,bad_count)



    
