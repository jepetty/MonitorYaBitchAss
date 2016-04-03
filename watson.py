import json
from credentials import watsonUser, watsonPassword
import watson_developer_cloud

def analyze_tone(txt):
	tone_analyzer = ToneAnalyzerV3Beta(
		username = watsonUser,
		password = watsonPassword,
		version = '2016-02-11')
	tone = json.dumps(tone_analyzer.tone(text=txt), indent=2)
	print(tone)
	return tone

if __name__ == "main":
	txt = "Jessica is the best thing ever!! She is so cool!!! I love her so much!!! <3 <3 <3"
	print(txt)
	analyze_tone(txt)