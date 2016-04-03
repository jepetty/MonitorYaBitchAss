import json
import random
from sys import argv
from pprint import pprint
from firebase import firebase
from credentials import watsonUser, watsonPassword
from watson_developer_cloud import ToneAnalyzerV3Beta
import datetime
import sys

firebase = firebase.FirebaseApplication('https://sigjesus.firebaseio.com/', None)
firebase.delete('/messages', None)

# input_string is the string the user gives you to analyze
script, input_string = argv
messages=""
#print input_string
tone_analyzer = ToneAnalyzerV3Beta(
	username = watsonUser,
	password = watsonPassword,
	version = '2016-02-11')

data = tone_analyzer.tone(text=input_string)
#print data
#These are the time ranges we can bug people about. 

now = datetime.datetime.now()
nowtest = now.replace(hour=4, minute=20, second=0, microsecond=0)

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

angerArray = ["you might come off a bit angry...", "you may or may not sound like a dick.", "you might need to chill.", \
"you might need to take it down a notch.", "you sound a bit angry.", "you sound sort of moody."]
disgustArray = ["you might want to try to be nicer.", "you could rub someone the wrong way.", "you do not sound very enthused."]
joyArray =["you say some nice things.", "you are very positive."]
fearArray=["you sound a little uneasy.", "you are being somewhat paranoid."]
sadnessArray=["it sounds like something is wrong... Are you ok?","you sound a little bit under the weather.", \
"it sounds like you haz the sadz."]
angerImages=["Images/Angry/AngryBird.jpg","Images/Angry/Cat.jpg","Images/Angry/Challenged.jpg","Images/Angry/Chicken.jpg","Images/Angry/Hate everything.jpg"]
disgustImages = ["Images/Disgust/FreshPrince.jpg","Images/Disgust/MontyPython.jpg","Images/Disgust/Picard.jpg","Images/Disgust/dsgstd.gif","Images/Disgust/kristen-wiig-target-lady-grossed-out.gif"]
fearImages = ["Images/Fear/Bread.jpg","Images/Fear/Dog.jpg","Images/Fear/PoolShark.jpg","Images/Fear/Turtle.jpg","Images/Fear/WaterBallon.jpg"]
joyImages = ["Images/Joy/Elephant.jpg","Images/Joy/hedgehog.jpg","Images/Joy/Rabbits.jpg","Images/Joy/Seal.jpg","Images/Joy/Turtle.jpg","Images/Joy/laughing-baby.jpg"]
sadImages = ["Images/Sad/Frog.jpg","Images/Sad/SadCat.jpg","Images/Sad/Sheldon.jpg","Images/Sad/StarWars.jpg","Images/Sad/Trex.jpg"]
#These are the time ranges we can bug people about. 

if (today11pm < nowtest< today1159pm):
	messages = messages + "Business hours are over, it might be a little late. "
elif (today12am < nowtest < today1259am):
	messages = messages + "Should you be texting this person this late. "
elif (today1am < nowtest< today230am):
	messages = messages + "Heading back from the bars? Just checking. "
elif (today231am < nowtest< today5am):
	messages = messages + "This is not an hour to text someone, you can probably wait a couple of hours. "
elif (today501am < nowtest< today630am):
	messages = messages + "It'a pretty early, this person is probably sleeping, are you sure? "

def strip(uglystring):
	return str(uglystring).replace('[','').replace("'",'').replace("'",'').replace(']','')
i=0
if ("sentences_tone" in data):
	numberofsentences = len(data["sentences_tone"])

	

	for y in range(0, numberofsentences):

		this = data["sentences_tone"][y]["tone_categories"][0]["tones"]
		sentencenumber = y + 1
		# hardcoded tones within "Emotional Sentiment"
		for x in range(0, 4):
			sentiment = this[x]
			
		# print(
		# if( data["document_tone"]["tone_categories"][0]["tones"][0]["tone_name"] == "Anger"):

			if ((sentiment["tone_name"] == "Anger") and (sentiment["score"] >= .40)):
				i=i+1
				angerChoice = strip(random.sample(angerArray,  1))
				messages = messages + "In the " + sentenceOrdinalArray[sentencenumber] + " sentence " + angerChoice + " "

			elif((sentiment["tone_name"] == "Disgust") and (sentiment["score"] >= .40)):	
				i=i+1
				disgustChoice = strip(random.sample(disgustArray,  1))
				messages = messages + "In the " + sentenceOrdinalArray[sentencenumber] + " sentence " + disgustChoice + " "

			elif((sentiment["tone_name"] == "Fear") and (sentiment["score"] >= .40)):	
				i=i+1
				fearChoice = strip(random.sample(fearArray,  1))
				messages = messages + "In the " + sentenceOrdinalArray[sentencenumber] + " sentence " + fearChoice + " "


			elif((sentiment["tone_name"] == "Joy") and (sentiment["score"] >= .40)):	
				i=i+1
				joyChoice = strip(random.sample(joyArray,  1) )
				messages = messages + "In the " + sentenceOrdinalArray[sentencenumber] + " sentence " + joyChoice + " "

			elif((sentiment["tone_name"] == "Sadness") and (sentiment["score"] >= .40)):	
				i=i+1
				sadnessChoice = strip(random.sample(sadnessArray,  1) )
				messages = messages + "In the " + sentenceOrdinalArray[sentencenumber] + " sentence " + sadnessChoice + " "

docTone = data["document_tone"]["tone_categories"][0]["tones"]

if(i<2):
	flag = 0
	for b in range(0, 5):
		if(flag==0):
			sentiment2 = docTone[b]
			text= "In your text"
			
			if ((sentiment2["tone_name"] == "Anger") and (sentiment2["score"] >= .20)):
				flag = 1
				angerChoice = strip(random.sample(angerArray, 1))
				messages = messages + text + " " + angerChoice + " "
			elif((sentiment2["tone_name"] == "Disgust") and (sentiment2["score"] >= .20)):
				flag = 1
				disgustChoice = strip(random.sample(disgustArray, 1))
				messages = messages + text + " " + disgustChoice + " "
			elif((sentiment2["tone_name"] == "Fear") and (sentiment2["score"] >= .40)):
				flag = 1
				fearChoice = strip(random.sample(fearArray, 1))
				messages = messages + text + " " + fearChoice + " "
			elif((sentiment2["tone_name"] == "Joy") and (sentiment2["score"] >= .40)):	
				flag = 1
				joyChoice = strip(random.sample(joyArray, 1))
				messages = message + text + " " + joyChoice + " "
			elif((sentiment2["tone_name"] == "Sadness") and (sentiment2["score"] >= .30)):
				flag = 1
				sadnessChoice = strip(random.sample(sadnessArray, 1))
				messages = messages + text + " " + sadnessChoice + " "
	
	if(flag==0):
		messages = messages + "The overall tone of your message was neutral."
	
print(messages)
messageJson = {'messages': messages}
messages = firebase.post("/messages", messageJson)
