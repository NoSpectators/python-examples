import random 

def rockPaperScissors():
	user1 = raw_input("What is your name, player1? ")
	user2 = raw_input("What is your name, player2? ")
	options = ["rock","paper","scissors"]
	play = True
	while play:
		option1 = options[random.randint(0,2)]
		option2 = options[random.randint(0,2)]
		if option1 == option2: #both choose same 
			print 'sorry, that\'s the same response: both of you chose',option1 
			play = False
		elif option1 == options[0]: #if first player rolls "rock"
			if option2 == options[2]:#if second player rolls "scissors"
				print 'user1 wins with',options[0]
				print 'user2 you lost by choosing',options[2]
				play = False
			elif option2 == options[1]:
				print 'user2 wins with',options[1]
				print 'user 1 you lost by choosing',options[0]
				play = False
		elif option2 == options[0]: #if player 2 is "rock"
			if option1 == options[2]: #if player 1 is "scissors"
				print 'user 2 wins with',options[0]
				print 'user 1 you lost by choosing',options[2]
				play = False
			elif option1 == options[1]:
				print user1, 'you win! you chose ',options[1]
				print user2, 'you lost by choosing',options[0]
				play = False 
		

		
	print "thanks for playing"
rockPaperScissors()