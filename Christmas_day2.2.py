#!/usr/bin/env python3

#--- Part Two ---
#The Elf finishes helping with the tent and sneaks back over to you. "Anyway, the second column says how the round needs to end: X means you need to lose, Y means you need to end the round in a draw, and Z means you need to win. Good luck!"
#The total score is still calculated in the same way, but now you need to figure out what shape to choose so the round ends as indicated. The example above now goes like this:
#In the first round, your opponent will choose Rock (A), and you need the round to end in a draw (Y), so you also choose Rock. This gives you a score of 1 + 3 = 4.
#In the second round, your opponent will choose Paper (B), and you choose Rock so you lose (X) with a score of 1 + 0 = 1.
#In the third round, you will defeat your opponent's Scissors with Rock for a score of 1 + 6 = 7.
#Now that you're correctly decrypting the ultra top secret strategy guide, you would get a total score of 12.

#Following the Elf's instructions for the second column, what would your total score be if everything goes exactly according to your strategy guide?
#A for Rock = 1
#B for Paper = 2
#C for Scissors = 3
#X for lose
#Y for draw
#Z for win


# Advent day 2
def score(a, b) :
	# b is rock and 1 score
	if (a == "B" and b == "X" ) or (a == "A" and b == "Y" ) or (a == "C" and b == "Z" ):
		c = 1
	# b is paper and 2 score
	elif (a == "C" and b == "X" ) or (a == "B" and b == "Y" ) or (a == "A" and b == "Z" ) :
		c = 2
	# b is scissors and 3 score
	else :
		c = 3
	return c

hand = open('input2.txt')

totscore = 0


for line in hand :
	line = line.rstrip()
	a, b = line.split()
	print(a, b)
	if  b == "Y" :
		print('draw')
		print(score(a, b))
		totscore = totscore + 3 + score(a, b)
	elif b == "Z" :
		print('won')
		print(score(a, b))
		totscore = totscore + 6 + score(a, b)
	else :   # b == X
		print('lost')
		print(score(a, b))
		totscore = totscore + score(a, b)

print('Total score is :', totscore)
