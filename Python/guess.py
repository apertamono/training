#! python3 
## Linux version: #! usr/bin/python3

# Inspired by the number guessing game in Al Sweigart's course Automate the Boring Stuff with Python, but more fun than the example in the course

import random, time 

secretNumber = random.randint(1, 25) # This goes from 1 to 25
hinted = False
unlucky = False
guess = 0 
replymode = 0
strinput = ""
# Word list for converting words into numbers
num_en = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen", "twenty", "twenty-one", "twenty-two", "twenty-three", "twenty-four", "twenty-five"] # Added zero so you can count from 1
# Use a list of Booleans to keep track of all numbers guessed
guessedbefore = [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False] # Added a Boolean for zero so you can count from 1

# Put guess input in a function + run the function once before the big loop
def guessinput():
	global guess, strinput, num_en, replymode, guessedbefore
	if guess > 0 and guess < 26:
		guessedbefore[guess] = True
	replymode = 4
	strinput = input()
	# Convert numbers entered as words
	if len(strinput) > 2: # Quickly filter out regular digits to avoid going through this loop every time
		for i in range(1, 26): # This goes from 1 to 25
			if strinput == num_en[i].lower():
				strinput = str(i)
				break
	# Exception for non-numerical strings - counted as a guess
	try:
		guess = int(strinput)
	except:
		print("You didn't enter a number.") # Can't say "Try again!" when it might be the last attempt
		guess = random.randint(26, 9999) # Make it an invalid number while avoiding repetition
		replymode = 5
				
print("I\'m thinking of a number between 1 and 25.")
print("Can you guess my number?")
guessinput()

# TODO: "Play again?" option instead of rerunning the script
# TODO: Change your mind occasionally, doubling or halving the number if possible
# TODO: Separate script to keep track of scores (fun twist: scores are multiplied, and they might be negative)

# Ask the player to guess 1+6=7 times
for guessesTaken in range(1, 8): # This goes from 1 to 7, while the last round won't be completed and one guess was made before the loop
	# Skip if non-numerical string was entered
	if replymode != 5:
		replymode = random.randint(1, 3) # Three different response types, replies skipped when > 3
	# Check for succesful guess	
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
		print("You failed! I was thinking of the number " + str(secretNumber) + ".")
		break
	# Replies and hints for failed guesses	
	elif guess == 42 or guess == 69 or guess == 420 or guess == 666:
		print("This is a mathematical excercise. Please take this seriously.")
	elif (guess < 1 or guess > 25) and replymode < 4:
		print("I said a number between 1 and 25.")
	elif replymode != 5 and guessedbefore[guess] == True: 
		print("You already guessed that, idiot!")
	elif (guess == 4 or guess == 13) and unlucky == False:
		print("You guessed an unlucky number, you\'re not getting a hint.")
		unlucky = True # Do give a hint for the second unlucky number guessed
	elif replymode == 1 or (replymode == 3 and hinted == True):
		if guess < secretNumber:
			print("Guess higher.")
		elif guess > secretNumber:
			print("Guess lower.")
	elif replymode == 2:
		if abs(guess - secretNumber) < 5:
			print("You\'re close.")
		elif abs(guess - secretNumber) < 10:
			print("You\'re not close.")
		else:
			print("You\'re far off!")
	elif replymode == 3 and hinted == False: # Only hint odd/even once
		hinted = True
		if secretNumber % 2 == 0:
			print("It\'s an even number.")
		else:
			print("It\'s an odd number.")
	guessinput() # Function call at the end because you want a hint to be followed by input


## Post an inspiring quote about knowledge or failure at the end, as a reward for guessing the number.
## TODO LATER: to make it easier to extend the quote collection, convert it from a regular text file.
inspiration = [
"Any observed statistical regularity will tend to collapse once pressure is placed upon it for control purposes.\n– Charles Goodhart",
"One should always play fair when one has the winning cards.\n– Oscar Wilde",
"It is better to stir up a question without deciding it, than to decide it without stirring it up.\n– Joseph Joubert",
"The desire of knowledge, like the thirst of riches, increases ever with the acquisition of it.\n– Laurence Sterne",
"If you torture the data long enough, it will confess.\n– Ronald Coase",
"There are many things of which a wise man might wish to be ignorant.\n– Ralph Waldo Emerson",
"On two occasions, I have been asked, \'Pray, Mr. Babbage, if you put into the machine wrong figures, will the right answers come out?\' I am not able to rightly apprehend the kind of confusion of ideas that could provoke such a question.\n– Charles Babbage",
"Honest criticism is hard to take, particularly from a relative, a friend, an acquaintance, or a stranger.\n– Franklin P. Jones",
"Knowledge comes, but wisdom lingers.\n– Alfred Tennyson",
"Where is the wisdom we have lost in knowledge? Where is the knowledge we have lost in information?\n– T.S. Eliot",
"A computer lets you make more mistakes faster than any other invention, with the possible exceptions of handguns and Tequila.\n– Mitch Ratcliffe",
"Good judgement comes from experience, and experience comes from bad judgement.\n– Frederick P. Brooks",
"Technology offers us a unique opportunity, though rarely welcome, to practice patience.\n– Allan Lokos",
"We build our computers the way we build our cities — over time, without a plan, on top of ruins.\n– Ellen Ullman",
"If the automobile had followed the same development as the computer, a Rolls Royce would today cost $100, get a million miles per gallon, and explode once a year killing everyone inside.\n– Robert Cringely",
"A man is like a fraction whose numerator is what he is and whose denominator is what he thinks of himself. The larger the denominator, the smaller the fraction.\n– Lev Tolstoy",
"In mathematics the art of proposing a question must be held of higher value than solving it.\n– Georg Cantor",
"It is not knowledge, but the act of learning, not possession but the act of getting there, which grants the greatest enjoyment.\n– Carl Friedrich Gauss",
"If people do not believe that mathematics is simple, it is only because they do not realize how complicated life is.\n– John von Neumann",
"Mathematics is good for the soul, getting things right enlivens a sense of truth, efforts to understand automatically purify desires.\n– Iris Murdoch",
"We live in a fantasy world, a world of illusion. The great task in life is to find reality.\n– Iris Murdoch",
"Think wrongly, if you please, but in all cases think for yourself.\n– Doris Lessing",
"The only thing that makes life possible is permanent, intolerable uncertainty; not knowing what comes next.\n– Ursula K. Le Guin",
"The only questions that really matter are the ones you ask yourself.\n– Ursula K. Le Guin",
"I tore myself away from the safe comfort of certainties through my love for truth - and truth rewarded me.\n– Simone de Beauvoir",
"I can always choose, but I ought to know that if I do not choose, I am still choosing.\n– Jean-Paul Sartre",
"A person who never made a mistake never tried anything new.\n– Albert Einstein",
"Failure is success in progress.\n– Albert Einstein",
"There are two kinds of failures: those who thought and never did, and those who did and never thought.\n– Laurence J. Peter",
"Success consists of going from failure to failure without loss of enthusiasm.\n– Winston Churchill",
"Uncertainty is the refuge of hope.\n– Henri Frederic Amiel",
"Perfecting oneself is as much unlearning as it is learning.\n– Edsger Dijkstra",
"Your mind will answer most questions if you learn to relax and wait for the answer.\n– William S. Burroughs",
"So long as you have food in your mouth, you have solved all questions for the time being.\n– Franz Kafka",
"It is better to know some of the questions than all of the answers.\n– James Thurber",
"Failure is simply the opportunity to begin again, this time more intelligently.\n– Henry Ford",
"Truth lies within a little and certain compass, but error is immense.\n– Henry St John",
"It is one thing to show a man that he is in error, and another to put him in possesion of truth.\n– John Locke",
"Mediocrity knows nothing higher than itself, but talent instantly recognizes genius.\n– Arthur Conan Doyle",
"Once you eliminate the impossible, whatever remains, no matter how improbable, must be the truth.\n– Arthur Conan Doyle",
"If you tell the truth, you don't have to remember anything.\n– Mark Twain",
"Man is least himself when he talks in his own person. Give him a mask, and he will tell you the truth.\n– Oscar Wilde",
"Experience is simply the name we give our mistakes.\n– Oscar Wilde",
"No man ever steps in the same river twice, for it's not the same river and he's not the same man.\n– Heraclitus",
"Life is the art of drawing without an eraser.\n– John W. Gardner",
"Be human, until your accountant explodes.\n– Inspirobot",
"Nothing in life is to be feared, it is only to be understood. Now is the time to understand more, so that we may fear less.\n– Marie Curie",
"Life consists not in holding good cards but in playing those you hold well.\n– Josh Billings",
"All truth passes through three stages. First, it is ridiculed. Second, it is violently opposed. Third, it is accepted as being self-evident.\n– Arthur Schopenhauer",
"Talent hits a target no one else can hit. Genius hits a target no one else can see.\n– Arthur Schopenhauer"
]

if guessesTaken < 5:
	time.sleep(1) # in seconds, not milliseconds!
	print ("\n" + inspiration[random.randint(0, 49)])
