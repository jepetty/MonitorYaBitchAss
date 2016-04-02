import json
from pprint import pprint

with open('data.json') as data_file:    
    data = json.load(data_file)

this = data["document_tone"]["tone_categories"][0]["tones"][0]
#pprint(data)
# print(
# if( data["document_tone"]["tone_categories"][0]["tones"][0]["tone_name"] == "Anger"):
if(this["score"] >= .50):
	# if (this["tone_name"] == "Anger"):
	print("Wow you sound really really angry! Chill? ")
elif (.50 > this["score"] >= .25):	
	print("angry much?")	
elif (.25 > this["score"] >= .15):	
	print("Are you sure?")		
else: 
	print("You arent mad.")



	# )