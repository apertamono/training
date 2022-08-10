# Guess the number game, but more fun than the version in the course

## TODO: replace 2% of responses by a random quote about failure, knowledge, uncertainty or numbers:
## No, it's better to post a quote at the end, as a reward for guessing the number.
# Any observed statistical regularity will tend to collapse once pressure is placed upon it for control purposes. - Charles Goodhart.
# One should always play fair when one has the winning cards. - Oscar Wilde.
# It is better to stir up a question without deciding it, than to decide it without stirring it up. - Joseph Joubert.
# The desire of knowledge, like the thirst of riches, increases ever with the acquisition of it. - Laurence Sterne.
# If you torture the data long enough, it will confess. - Ronald Coase.
# There are many things of which a wise man might wish to be ignorant. - Ralph Waldo Emerson.
# On two occasions, I have been asked [by members of Parliament], \'Pray, Mr. Babbage, if you put into the machine wrong figures, will the right answers come out?\' I am not able to rightly apprehend the kind of confusion of ideas that could provoke such a question. - Charles Babbage.
# Honest criticism is hard to take, particularly from a relative, a friend, an acquaintance, or a stranger. - Franklin P. Jones.
# Knowledge comes, but wisdom lingers. - Alfred Tennyson.
# Where is the wisdom we have lost in knowledge? Where is the knowledge we have lost in information? - T.S. Eliot.
# A computer lets you make more mistakes faster than any other invention, with the possible exceptions of handguns and Tequila. ― Mitch Ratcliffe.
# Good judgement comes from experience, and experience comes from bad judgement. ― Frederick P. Brooks.
# Technology offers us a unique opportunity, though rarely welcome, to practice patience. ― Allan Lokos.
# We build our computers the way we build our cities — over time, without a plan, on top of ruins. ― Ellen Ullman.
# If the automobile had followed the same development as the computer, a Rolls Royce would today cost $100, get a million miles per gallon, and explode once a year killing everyone inside. ― Robert Cringely.
# A man is like a fraction whose numerator is what he is and whose denominator is what he thinks of himself. The larger the denominator, the smaller the fraction. - Lev Tolstoy.
# In mathematics the art of proposing a question must be held of higher value than solving it. - Georg Cantor.
# It is not knowledge, but the act of learning, not possession but the act of getting there, which grants the greatest enjoyment. - Carl Friedrich Gauss.
# If people do not believe that mathematics is simple, it is only because they do not realize how complicated life is. - John von Neumann.
# Mathematics is good for the soul, getting things right enlivens a sense of truth, efforts to understand automatically purify desires. - Iris Murdoch.
# We live in a fantasy world, a world of illusion. The great task in life is to find reality. - Iris Murdoch.
# Think wrongly, if you please, but in all cases think for yourself. - Doris Lessing.
# The only thing that makes life possible is permanent, intolerable uncertainty; not knowing what comes next. - Ursula K. Le Guin.
# The only questions that really matter are the ones you ask yourself. - Ursula K. Le Guin.
# I tore myself away from the safe comfort of certainties through my love for truth - and truth rewarded me. - Simone de Beauvoir.
# I can always choose, but I ought to know that if I do not choose, I am still choosing. - Jean-Paul Sartre.
# A person who never made a mistake never tried anything new. - Albert Einstein.
# Failure is success in progress. - Albert Einstein.
# There are two kinds of failures: those who thought and never did, and those who did and never thought. - Laurence J. Peter.
# Success consists of going from failure to failure without loss of enthusiasm. - Winston Churchill.
# Uncertainty is the refuge of hope. - Henri Frederic Amiel.
# Perfecting oneself is as much unlearning as it is learning. - Edsger Dijkstra.
# Your mind will answer most questions if you learn to relax and wait for the answer. - William S. Burroughs.
# So long as you have food in your mouth, you have solved all questions for the time being. - Franz Kafka.
# It is better to know some of the questions than all of the answers. - James Thurber.
# Failure is simply the opportunity to begin again, this time more intelligently. - Henry Ford.
# Truth lies within a little and certain compass, but error is immense. - Henry St John.
# It is one thing to show a man that he is in error, and another to put him in possesion of truth. - John Locke.
# Mediocrity knows nothing higher than itself, but talent instantly recognizes genius. - Arthur Conan Doyle.
# Once you eliminate the impossible, whatever remains, no matter how improbable, must be the truth. - Arthur Conan Doyle.
# If you tell the truth, you don't have to remember anything. - Mark Twain.
# Man is least himself when he talks in his own person. Give him a mask, and he will tell you the truth. - Oscar Wilde.
# Experience is simply the name we give our mistakes. - Oscar Wilde.
# No man ever steps in the same river twice, for it's not the same river and he's not the same man. - Heraclitus.
# Life is the art of drawing without an eraser. - John W. Gardner.
# A failure is not always a mistake, it may simply be the best one can do under the circumstances. The real mistake is to stop trying. - B. F. Skinner.
# Nothing in life is to be feared, it is only to be understood. Now is the time to understand more, so that we may fear less. - Marie Curie.
# Life consists not in holding good cards but in playing those you hold well. - Josh Billings.
# All truth passes through three stages. First, it is ridiculed. Second, it is violently opposed. Third, it is accepted as being self-evident. - Arthur Schopenhauer.
# Talent hits a target no one else can hit. Genius hits a target no one else can see. - Arthur Schopenhauer.



import random # Errors on the command-line because keyword.py in the same folder was using the name of a module called by random

secretNumber = random.randint(1, 23) # This goes from 1 to 23
hinted = False
previous = 0
print("I\'m thinking of a number between 1 and 23.")
print("Can you guess my number?")
guess = int(input()) # TODO: exception for non-numerical strings ## TODO: conversion function

# Ask the player to guess 1+6=7 times
for guessesTaken in range (1, 8): # This goes from 1 to 7, while the last round won't be completed
	toggle = random.randint(1, 3) # Three different response types
	if guess == secretNumber:
		if guessesTaken == 1:
			print("What is this magic? You only needed 1 guess!")
		elif guessesTaken < 4:
			print("You\'re a genius! You only needed " + str(guessesTaken) + " guesses.")
		elif guessesTaken < 6:
			print("Excellent! You guessed my number in " + str(guessesTaken) + " tries.")			
		else:
			print("OK, you got there eventually, on the " + str(guessesTaken) + "th attempt.")
		break
	elif guessesTaken == 7:
		print("No, you failed! I was thinking of the number " + str(secretNumber) + ".")
		break		
	elif guess == 42 or guess == 69 or guess == 420 or guess == 666:
		print("This is a mathematical excercise. Please take this seriously.")
		toggle = 4 # Skip the other responses ## Could use `continue` if input wasn't at the end of the loop
	elif guess < 1 or guess > 23:
		print("I said a number between 1 and 23.")
		toggle = 4 
	elif guess == previous: # TODO: use a list to keep track of all numbers guessed
		print("You already guessed that, idiot!")
		toggle = 4
	elif guess == 4 or guess == 13:
		print("You guessed an unlucky number. And it\'s wrong too. Try again.")
		toggle = 4
	elif toggle == 1 or (toggle == 3 and hinted == True):
		if guess < secretNumber:
			print("Guess higher.")
		else:
			print("Guess lower.")
	elif toggle == 2:
		if abs(guess - secretNumber) < 5:
			print("You\'re close.")
		elif abs(guess - secretNumber) < 10:
			print("You\'re not close.")
		else:
			print("You\'re far off!")
	elif toggle == 3 and hinted == False: # Only hint odd/even once
		hinted = True
		if secretNumber % 2 == 0:
			print("Hint: it\'s an even number.")
		else:
			print("Hint: it\'s an odd number.")
	previous = guess		
	guess = int(input()) # At the end because you don't want a hint without input


