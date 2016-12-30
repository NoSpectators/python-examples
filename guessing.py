import random 


def main():
	number = random.randint(1,9)
	count = 0
	guess = 0
	
	while guess != number and guess != 'exit':
		guess = raw_input('what\'s your guess? ')
		if guess == 'exit':
			break
		guess = int(guess)
		count+=1
		
		if guess < number:
			print "Too low!"
		elif guess > number:
			print "Too high!"
		else:
			print "You got it!"
			print "And it only took you",count,"tries!" 

main()


	

	