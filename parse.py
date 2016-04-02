import json
import random
from pprint import pprint
import datetime

with open('data.json') as data_file:    
    data = json.load(data_file)

now = datetime.datetime.now()
nowtest = now.replace(hour=4, minute=20, second=0, microsecond=0)
print(nowtest)

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

disgustArray = ["You don't sound very enthused", "try to be nicer", "Are you breaking up with me?"]




if (today11pm < nowtest< today1159pm):
	print("11:00 PM range")
elif (today12am < nowtest < today1259am):
	print("It's late")
elif (today1am < nowtest< today230am):
	print("heading back from the bars?")
elif (today231am < nowtest< today5am):
	print("It's the middle of the night")
elif (today501am < nowtest< today630am):
	print("It's kinda early don't you think?")
else: 
	print("else")

#sentence length
# print(%S)
numberofsentences = len(data["sentences_tone"])
print(numberofsentences)
#print ("First list length : ", lastSentence)

i=0

for y in range(0, numberofsentences):

	this = data["sentences_tone"][y]["tone_categories"][0]["tones"]
	sentencenumber = y + 1
	# hardcoded tones within "Emotional Sentiment"
	for x in range(0, 4):
		sentiment = this[x]
		
	# print(
	# if( data["document_tone"]["tone_categories"][0]["tones"][0]["tone_name"] == "Anger"):

		if ((sentiment["tone_name"] == "Anger") and (sentiment["score"] >= .20)):
			i=i+1
			print("Anger   " + str(sentiment["score"]))
			print("Sentence "+ str(sentencenumber) + " sounds angry" )
		elif((sentiment["tone_name"] == "Disgust") and (sentiment["score"] >= .10)):	
			i=i+1
			disgustChoice = str(random.sample(disgustArray,  1) )
			print("Disgust " + str(sentiment["score"]))
			print("Sentence "+ str(sentencenumber) + disgustChoice)
		elif((sentiment["tone_name"] == "Fear") and (sentiment["score"] >= .40)):	
			i=i+1
			print("Fear " + str(sentiment["score"]))
		elif((sentiment["tone_name"] == "Joy") and (sentiment["score"] >= .40)):	
			i=i+1
			print("Joy " + str(sentiment["score"]))
		elif((sentiment["tone_name"] == "Sadness") and (sentiment["score"] >= .40)):	
			i=i+1
			print("Sadness ")

docTone = data["document_tone"]["tone_categories"][0]["tones"]
if(i==0 or i>2):

	for b in range(0, 4):
		sentiment2 = docTone[b]
		
		if ((sentiment2["tone_name"] == "Anger") and (sentiment2["score"] >= .20)):
			print("Anger   " + str(sentiment2["score"]))
		elif((sentiment2["tone_name"] == "Disgust") and (sentiment2["score"] >= .20)):	
			print("Disgust " + str(sentiment2["score"]))
		elif((sentiment2["tone_name"] == "Fear") and (sentiment2["score"] >= .40)):	
			print("Fear " + str(sentiment2["score"]))
		elif((sentiment2["tone_name"] == "Joy") and (sentiment2["score"] >= .40)):	
			print("Joy " + str(sentiment2["score"]))
		elif((sentiment2["tone_name"] == "Sadness") and (sentiment2["score"] >= .40)):	
			print("Sadness ")
print(i)
	


	# Disgusted = ["You don't sound very enthused", "try to be nicer", "Are you breaking up with me?"]
