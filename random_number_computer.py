import random
random_number=random.randint(1,10)

while True:
	guess =input ("pick a number between 1 and 10:")
	guess =int(guess)
	if guess<random_number:
		print("too loww ")
	elif guess>random_number:
		print("too high")
	else :
		print(f"you won ! u guessed {random_number} correctly ")
		play_again=input("u wanna play again y/n? :")
		print(play_again)
		if play_again=='y':
			random_number=randam.randint(1,10)
			guess=None
		else:
			print("thankyou for playing !")
			break