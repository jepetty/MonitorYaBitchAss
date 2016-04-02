import json
from pprint import pprint

with open('data.json') as data_file:    
    data = json.load(data_file)

#sentence length
numberofsentences = len(data["sentences_tone"])
print(numberofsentences)
#print ("First list length : ", lastSentence)

i=0

for y in range(0, numberofsentences):

	this = data["sentences_tone"][y]["tone_categories"][0]["tones"]

	# hardcoded tones within "Emotional Sentiment"
	for x in range(0, 4):
		sentiment = this[x]
		#pprint(data)
	# print(
	# if( data["document_tone"]["tone_categories"][0]["tones"][0]["tone_name"] == "Anger"):

		if ((sentiment["tone_name"] == "Anger") and (sentiment["score"] >= .40)):
			i=i+1
			print("Anger   " + str(sentiment["score"]))
		elif((sentiment["tone_name"] == "Disgust") and (sentiment["score"] >= .40)):	
			i=i+1
			print("Disgust " + str(sentiment["score"]))
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
		#pprint(data)
	# print(
	# if( data["document_tone"]["tone_categories"][0]["tones"][0]["tone_name"] == "Anger"):

		if ((sentiment2["tone_name"] == "Anger") and (sentiment2["score"] >= .20)):
			i=i+1
			print("Anger   " + str(sentiment2["score"]))
		elif((sentiment2["tone_name"] == "Disgust") and (sentiment2["score"] >= .20)):	
			i=i+1
			print("Disgust " + str(sentiment2["score"]))
		elif((sentiment2["tone_name"] == "Fear") and (sentiment2["score"] >= .40)):	
			i=i+1
			print("Fear " + str(sentiment2["score"]))
		elif((sentiment2["tone_name"] == "Joy") and (sentiment2["score"] >= .40)):	
			i=i+1
			print("Joy " + str(sentiment2["score"]))
		elif((sentiment2["tone_name"] == "Sadness") and (sentiment2["score"] >= .40)):	
			i=i+1
			print("Sadness ")


	# if (this["tone_name"] == "Anger"):
	# 	if(this["score"] >= .50):
	# 		print("Wow you sound really really angry! Chill? ")
	# 	elif (.50 > this["score"] >= .25):	
	# 		print("mad bro?")	
	# 	elif (.25 > this["score"] >= .15):	
	# 		print("Are you sure?")		
	# 	else: 
	# 		print("You arent mad.")

	# if (this["tone_name"] == "Disgust"):
	# 	if(this["score"] >= .50):
	# 		print(" ")
	# 	elif (.50 > this["score"] >= .25):	
	# 		print(" ")	
	# 	elif (.25 > this["score"] >= .15):	
	# 		print(" ")		
	# 	else: 
	# 		print(" ")