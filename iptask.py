import random
import os
		# Add texts here: # 
listtexts = ['hey how are you', 'k.', 'We need to talk', 'Call me as soon as possible', "I'm so sorry.", 'im sorry', 'luv u', 'I love you', 'heyyyyyy', 'REALlY??', 'really.', 'where r u', 'Where are you??', 'how ya doin', 'sooo excited.', 'I cant wait!', 'im so happy fr u', 'Im so happy for you!', 'congratz.', 'happy bday']
random.shuffle(listtexts)
os.system('clear')

print "Text Analyzer version 1.0"
		# The following feature won't work in this implementation, I need access to databases and such to keep increasing my list # 
# new_text = raw_input("To begin, please copy and paste one text you have received: ")
# listtexts.append(new_text)

os.system('clear')

def question(onetext):
	print "Text message: " + onetext 
	print
	print "Please choose the emotion that best fits this text: "
	print
	print("A. Angry")
	print("B. Sad")
	print("C. Happy")
	print("D. Anxious")
	print("E. Surprised")
	print("F. Afraid")
	print("G. Lust")
	print("H. No emotion")

score = 0
for i in range(0, len(listtexts)):
	templist = []
	for j in range(0, 2):
		print 'Player ' + str(j%2 + 1) + ' turn'
		question(listtexts[i])
		answer = raw_input("Answer: ").lower()
		templist.append(answer)
		os.system('clear')  
	if templist[0] == templist[1]:
		score +=1 

print "You and your partner agreed on " + str(score) + " out of " + str(len(listtexts)) +  " texts!"
