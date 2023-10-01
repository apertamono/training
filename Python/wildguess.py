# Optional Windows shebang: #! python3
# Linux/Mac: #!/usr/bin/env python3

# Wild Guess version 9 (previous version uploaded as guess.py)
# Guess a number while the hints you get might be unreliable
# Inspired by the number guessing game in Al Sweigart's course Automate the Boring Stuff with Python

# From version 3, the code needs to remain a secret, because it's full of surprises
# From version 7, the code is convoluted enough that making it open-source won't spoil the surprises

# I know it's full of hard-coded numbers and global variables, shut up
# TODO: replace text by constants, so they can be translated in one place

import random, time
from datetime import datetime

# Initialize global variables
guess = 0 
replymode = 0
strinput = ""
hinted = False
primed = False
unlucky = False
counseled = False
changed = False
fooled = False
guessesTakenFooled = 0
lied = False
forget = False
wrong = 0

# Use a list of Booleans to keep track of all numbers guessed
guessedbefore = [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False] # Added a Boolean for zero so you can count from 1 # Version 7: doubled the list for the lied twist

# Word list for converting words into numbers
num_en = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen", "twenty", "twenty-one", "twenty-two", "twenty-three", "twenty-four", "twenty-five"] # Added zero so you can count from 1
num_nl = ["nul", "een", "twee", "drie", "vier", "vijf", "zes", "zeven", "acht", "negen", "tien", "elf", "twaalf", "dertien", "veertien", "vijftien", "zestien", "zeventien", "achttien", "negentien", "twintig", "eenentwintig", "tweeëntwintig", "drieëntwintig", "vierentwintig", "vijfentwintig"] # Dutch
num_zh = ["〇", "一", "二", "三", "四", "五", "六", "七", "八", "九", "十", "	十一", "十二", "十三", "十四", "十五", "十六", "十七", "十八", "十九", "二十", "二十一", "二十二", "二十三", "二十四", "二十五"] # Chinese

# Useless life advice + useless hints
advice = [
"Everything happens for a reason.",
"You miss 100% of the shots you don’t take.",
"You can do anything you set your mind to.",
"What goes around, comes around.",
"Whatever you do, give it 100%.",
"Forgive so you can live.",
"Never stop learning and growing as a person.",
"Change your thinking, change your life.",
"Treat people as you would like to be treated.",
"Never give up, never surrender.",
"Be patient and persistent.",
"Luck comes from hard work.",
"Do your best at all times.",
"You can't always get what you want.",
"Use adversity as an opportunity.",
"Learn something new every day.",
"Believe in yourself.",
"Get over your fear of rejection.",
"You attract what you are.",
"When life gives you lemons, make lemonade.",
"We all have a purpose.",
"Your purpose will find you.",
"There are lessons in everything.",
"Don't be afraid to ask for guidance.",
"Fear is your only true limitation.",
"For every problem, there is always a solution.",
"You're exactly where you’re meant to be in the universe.",
"What you put out is what you get back.",
"Release the need to control your life.",
"Reflect on your spiritual health.",
"Look for deeper meanings.",
"Explore your spiritual core.",
"Take time to meditate.",
"Learn to say no.",
"Take your time when you eat.",
"Do one thing at a time.",
"Spend time alone and with your family.",
"Don't compare yourself to others.",
"Live in the present.",
"Stick to a regular sleep schedule.",
"Practice the habit of positive thinking.",
"Congratulate yourself for an accomplishment every day.",
"Stay focused on the present and don’t worry about past or future.",
"Surround yourself with good people.",
"You weren't born to impress others.",
"Follow your heart.",
"Make a few good friends, don't worry about being popular.",
"Never be afraid to ask questions.",
"Invest in your most important relationships.",
"Cultivate a spirit of gratitude.",
"It's a real number.",
"It's a rational number.",
"It's an integer.",
"It's a positive number.",
"It's a natural number.",
"It's a real number.",
"It's a rational number.",
"It's an integer.",
"It's a positive number.",
"It's a natural number.",
"The number can't be divided by 0.",
"The number can be divided by 2.",  # No one's promising the result will be an integer :)
"The number can be divided by 3.",
"The number can be divided by 1."
]

# Determine the pseudo-random number from 1 to 25 to be guessed
randomNumber = random.randint(3, 82) # This goes from 3 to 82
if randomNumber < 78:
	secretNumber = randomNumber // 3  # Floor division, 3 to 77 => 1 to 25
# Twist: Higher chance for 3, 13, 23	
elif randomNumber == 78:
	secretNumber = 3
elif randomNumber == 79:
	secretNumber = 13
elif randomNumber == 80:
	secretNumber = 23
# Twist: Higher chance for month number * 2 and hour number + 1
elif randomNumber == 81:
	secretNumber = datetime.today().month * 2
elif randomNumber == 82:
	secretNumber = datetime.now().hour + 1
# Sanity check in case the time is malfunctioning
if secretNumber < 1 or secretNumber > 25:
	secretNumber = random.randint(1, 25)
# Twist: Sometimes (5%) choose a number higher than 25.
if random.randint(1, 100) < 6:
	secretNumber = random.randint(26, 50)
	lied = True
	
# Put guess input in a function + run the function once before the big for loop
def guessinput():
	global guess, strinput, num_en, replymode, guessedbefore
	if guess > 0 and guess < 51:
		guessedbefore[guess] = True
	replymode = 4
	strinput = input()
	# Convert numbers entered as words
	# if len(strinput) > 2: # Quickly filter out regular digits 
	# Exception is a better filter for Chinese words:
	try:
		guess = int(strinput)
	except:	
		for i in range(1, 26): # This goes from 1 to 25
			if strinput == num_en[i].lower():
				strinput = str(i)
				break
			if strinput == num_nl[i].lower():
				strinput = str(i)
				break	
			if strinput == num_zh[i].lower():
				strinput = str(i)
				break				
	# Exception for non-numerical strings - counted as a guess
	try:
		guess = int(strinput)
	except:
		print("You didn't enter a number.") # Can't say "Try again!" when it might be the last attempt
		guess = random.randint(51, 999999999) # Make it an invalid number while avoiding repetition
		replymode = 5
				
# Start the conversation
print("I\'m thinking of a number between 1 and 25.")
print("Can you guess my number?")
guessinput()

# TODO: Keep track of scores. 
# TODO: "Play again?" option instead of rerunning the script.
# TODO: Let the user enter their name.
# TODO: Twist: Change your mind sometimes (5%), doubling or halving the number if possible

# Ask the player to guess 1+6=7 times (plus 2 possibe extensions)
for guessesTaken in range(1, 10): # This goes from 1 to 9, while the last round won't be completed and one guess was made before the loop

	# Twist: "Sorry, the previous hint was wrong. It's the other way around." Not a boolean but a counter: 1 = wrong hint, 2 = apology, >2 = don't repeat, >0 = don't do any other shenannigans
	if wrong > 0:
		wrong += 1
	else:
		if random.randint(1, 100) < 5 and replymode != 5 and lied == False and fooled == False and counseled == False:
			wrong = 1
	if wrong == 2:
		print("Sorry, the previous hint was wrong. It's the other way around. This one is true:")

	# Twist: Occasionally (5%) keep going when the number is guessed correctly
	if fooled == True and guessesTaken > 6:
		print("Never mind, I fooled you. My number was " + str(secretNumber) + ". You actually guessed it in " + str(guessesTakenFooled) + " turns. You're not so bad after all.")
		break
	if guess == secretNumber and fooled == False and guessesTaken < 6 and random.randint(1, 100) < 6 and wrong == 0:
		fooled = True
		unlucky = True # Avoid calling the wrong numbers unlucky
		guessesTakenFooled = guessesTaken
		guess = secretNumber + 2 # Need to give a slightly wrong clue
		if secretNumber > 23:
			guess = secretNumber - 2

	# Skip if non-numerical string was entered
	if replymode != 5:
		replymode = random.randint(1, 4) # Four different response types, replies skipped when replymode > 4
		if random.randint(1, 100) > 90 and counseled == False and guessesTaken in [3, 4, 5] and wrong == 0: 
			replymode = 0 # Another response type: useless advice, around 5% of all replies
		if wrong == 1:
			replymode = random.randint(2, 4)

	# Check for succesful guess	
	if guess == secretNumber and fooled == False:
		if guessesTaken == 1:
			print("What is this magic? You only needed 1 guess!")
		elif guessesTaken < 4:
			print("You\'re a genius! You only needed " + str(guessesTaken) + " guesses.")
		elif guessesTaken < 6:
			print("Excellent! You guessed my number in " + str(guessesTaken) + " tries.")			
		else:
			print("OK, you got there eventually, on the " + str(guessesTaken) + "th attempt.")
		break
	# Twist: 20% chance of an extension, hence 4% chance of two extensions
	elif (guessesTaken == 9 or (guessesTaken > 6 and random.randint(1, 100) > 20)) and fooled == False:
		if lied == False:
			print("You failed! I was thinking of the number " + str(secretNumber) + ".")
		else:
			print("I lied, I was thinking of the number " + str(secretNumber) + ". Don't be such a sheep! You shouldn't trust authority figures.")
		break
		
	# Negative replies for invalid or unlucky guesses
	elif guess > 999999999:
		print("Wow, that's a big number! I\'m impressed.")
		replymode = 6 # Skip the hints, where we can't use elif anymore	because of the lucky 8 twist		
	elif guess == 42 or guess == 69 or guess == 420 or guess == 666:
		print("This is a mathematical excercise. Please take this seriously.")
		replymode = 6
	elif (guess < 1 or guess > 25) and replymode < 5 and (lied == False or guess > 50):
		print("I said a number between 1 and 25.")
		replymode = 6 
	elif replymode < 5 and guessedbefore[guess] == True and fooled == False: 
		print("You already guessed that, idiot!")
		replymode = 6 		
	elif (guess == 4 or guess == 13) and unlucky == False and fooled == False:
		print("You guessed an unlucky number, you\'re not getting a hint.")
		unlucky = True # Do give a hint for the second unlucky number guessed
		replymode = 6 
	elif replymode == 0:
		if random.randint(1, 4) > 1:
			print(advice[random.randint(0, 63)])
		else:
			print("The number can be divided by " + str(random.randint(1, 1000)) + ".")
		replymode = 6
		counseled = True # Don't give useless advice more than once
	
	# Hints for valid failed guesses
	if replymode < 5 and guess == 23 and random.randint(1, 100) <= 20:
		print("Study the Law of Fives.") # Random off-topic addition.
	# Echo the guess for online play: "It's not n." Turned off. Confusing to read.
	# if replymode < 5:
	# 	print("It's not " + str(guess) + ". ")
	# TODO: Twist: forget the number (2% chance per answer). 
	if replymode < 5 and random.randint(1, 100) > 98 and fooled == False and wrong == 0:
		print("Sorry, I forget which number I was thinking of.")
		forget = True
		break
	if replymode == 1 or (replymode == 4 and primed == True):
		if abs(guess - secretNumber) < 5:
			print("You\'re close.")
		elif abs(guess - secretNumber) < 10:
			print("You\'re not close.")
		elif abs(guess - secretNumber) > 9:
			print("You\'re far off!")
		# Twist: Give two hints for lucky 8 in < 1/6 of cases (?)
		if guess == 8 and random.randint(1, 3) == 1 and wrong != 1:
			replymode = 2
	if replymode == 2 or (replymode == 3 and hinted == True):
		if guess < secretNumber and wrong != 1:
			print("Guess higher.")
		elif guess > secretNumber and wrong != 1:
			print("Guess lower.")
		elif guess < secretNumber and wrong == 1:
			print("Guess lower.")
		elif guess > secretNumber and wrong == 1:
			print("Guess higher.")			
	if replymode == 3 and hinted == False: # Only hint odd/even once
		hinted = True
		if secretNumber % 2 == 0 and wrong != 1:
			print("It\'s an even number.")
		elif secretNumber % 2 != 0 and wrong != 1:
			print("It\'s an odd number.")
		elif secretNumber % 2 == 0 and wrong == 1:
			print("It\'s an odd number.")
		elif secretNumber % 2 != 0 and wrong == 1:
			print("It\'s an even number.")			
	if replymode == 4 and primed == False: # Only hint prime/divisible once
		primed = True
		if secretNumber in [2, 3, 5, 7, 11, 13, 17, 19, 23] and wrong != 1:
			print("It\'s a prime number.")
		elif secretNumber not in [2, 3, 5, 7, 11, 13, 17, 19, 23] and wrong != 1:
			print("It\'s not a prime number.")			
		elif secretNumber in [2, 3, 5, 7, 11, 13, 17, 19, 23] and wrong == 1:
			print("It\'s not a prime number.")
		elif secretNumber not in [2, 3, 5, 7, 11, 13, 17, 19, 23] and wrong == 1:
			print("It\'s a prime number.")				
	guessinput() # Function call at the end because you want a hint to be followed by input


## Post an inspiring quote about knowledge or failure at the end, as a reward for guessing the number.
## TODO: to make it easier to extend the quote collection, convert it from a regular text file.
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
"A computer lets you make more mistakes faster than any other invention, with the possible exceptions of handguns and tequila.\n– Mitch Ratcliffe",
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

if forget == False and (guessesTaken < 5 or (fooled == True and guessesTakenFooled < 5)):
	time.sleep(0.5) # in seconds, not milliseconds!
	print ("\n" + inspiration[random.randint(0, 49)])