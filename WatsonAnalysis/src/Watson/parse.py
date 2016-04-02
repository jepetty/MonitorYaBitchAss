import json
import random
from pprint import pprint
import datetime
import sys

with open('data.json') as data_file:    
    data = json.load(data_file)
messages=""

#These are the time ranges we can bug people about. 

now = datetime.datetime.now()
nowtest = now.replace(hour=4, minute=20, second=0, microsecond=0)
#print(nowtest)

today8am = now.replace(hour=8, minute=0, second=0, microsecond=0)

today11pm = now.replace(hour=23, minute=0, second=0, microsecond=0)
today1159pm = now.replace(hour=23, minute=59, second=0, microsecond=0)

today12am = now.replace(hour=0, minute=0, second=0, microsecond=0)
today1259am = now.replace(hour=0, minute=59, second=0, microsecond=0)

today1am = now.replace(hour=1, minute=0, second=0, microsecond=0)
today230am = now.replace(hour=2, minute=30, second=0, microsecond=0)

today231am = now.replace(hour=2, minute=31, second=0, microsecond=0)
today5am = now.replace(hour=5, minute=0, second=0, microsecond=0)

today501am = now.replace(hour=5, minute=01, second=0, microsecond=0)
today630am = now.replace(hour=6, minute=3, second=0, microsecond=0)


sentenceOrdinalArray = ['first', 'second', 'third', 'fourth', 'fifth', 'sixth', 'seventh', 'eighth', 'ninth', 'tenth']

#Arrays for the messages that could be presented when a certain emotion is present, chosen at random

angerArray = ["you might come off a bit angry", "you might need to chill.", "you might need to take it down a notch.", "you sound a bit angry.", "you sound sort of moody."]
disgustArray = ["try to be nicer", "A?", "you do not sound very enthused"]
joyArray =["What a happy message", "happy2"]
fearArray=["fear1", "fear2","fear3"]
sadnessArray=["sad1","sad2","sad3","sad4"]

#These are the time ranges we can bug people about. 

if (today11pm < nowtest< today1159pm):
	messages = messages + "Business hours are over, are you sure? "
elif (today12am < nowtest < today1259am):
	messages = messages + "Should you be texting this person this late "
elif (today1am < nowtest< today230am):
	messages = messages + "Heading back from the bars? Just checking. Proceed? "
elif (today231am < nowtest< today5am):
	messages = messages + "This is not an hour to text someone, you can probably wait a couple of hours, proceed? "
elif (today501am < nowtest< today630am):
	messages = messages + "It'a pretty early this person is probably sleeping, are you sure? "
#else: 
#	print("else")

def strip(uglystring):
	return str(uglystring).replace('[','').replace("'",'').replace("'",'').replace(']','')


numberofsentences = len(data["sentences_tone"])

i=0

for y in range(0, numberofsentences):

	this = data["sentences_tone"][y]["tone_categories"][0]["tones"]
	sentencenumber = y + 1
	# hardcoded tones within "Emotional Sentiment"
	for x in range(0, 4):
		sentiment = this[x]
		
	# print(
	# if( data["document_tone"]["tone_categories"][0]["tones"][0]["tone_name"] == "Anger"):

		if ((sentiment["tone_name"] == "Anger") and (sentiment["score"] >= .10)):
			i=i+1
			angerChoice = strip(random.sample(angerArray,  1))
			messages = messages + "In the " + sentenceOrdinalArray[sentencenumber] + " sentence " + angerChoice + " "

		elif((sentiment["tone_name"] == "Disgust") and (sentiment["score"] >= .10)):	
			i=i+1
			disgustChoice = strip(random.sample(disgustArray,  1))
			messages = messages + "In the " + sentenceOrdinalArray[sentencenumber] + " sentence " + disgustChoice + " "

		elif((sentiment["tone_name"] == "Fear") and (sentiment["score"] >= .10)):	
			i=i+1
			fearChoice = strip(random.sample(fearArray,  1))
			messages = messages + "In the " + sentenceOrdinalArray[sentencenumber] + " sentence " + fearChoice + " "


		elif((sentiment["tone_name"] == "Joy") and (sentiment["score"] >= .10)):	
			i=i+1
			joyChoice = strip(random.sample(joyArray,  1) )
			messages = messages + "In the " + sentenceOrdinalArray[sentencenumber] + " sentence " + joyChoice + " "

		elif((sentiment["tone_name"] == "Sadness") and (sentiment["score"] >= .10)):	
			i=i+1
			sadnessChoice = strip(random.sample(sadnessArray,  1) )
			pmessages = messages + "In the " + sentenceOrdinalArray[sentencenumber] + " sentence " + sadnessChoice " "

docTone = data["document_tone"]["tone_categories"][0]["tones"]
if(i==0 or i>2):

	for b in range(0, 4):
		sentiment2 = docTone[b]
		text= "In your text"
		
		if ((sentiment2["tone_name"] == "Anger") and (sentiment2["score"] >= .20)):
			messages = messages + text +" " + angerChoice + " "
		elif((sentiment2["tone_name"] == "Disgust") and (sentiment2["score"] >= .20)):	
			messages = messages + text +" " + disgustChoice " "
		elif((sentiment2["tone_name"] == "Fear") and (sentiment2["score"] >= .40)):	
			messages = messages + text + " " +fearhoice " "
		elif((sentiment2["tone_name"] == "Joy") and (sentiment2["score"] >= .40)):	
			messages = messages + text + " " +joyChoice + " "
		elif((sentiment2["tone_name"] == "Sadness") and (sentiment2["score"] >= .40)):	
			messages = messages + text + " " +sadnessChoice " "
# print(i)
#firebase field = messages	


	# Disgusted = ["You don't sound very enthused", "try to be nicer", "Are you breaking up with me?"]
