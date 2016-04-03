import json
from credentials import watsonUser, watsonPassword
from watson_developer_cloud import ToneAnalyzerV3Beta

def analyze_tone(txt):
	tone_analyzer = ToneAnalyzerV3Beta(
		username = watsonUser,
		password = watsonPassword,
		version = '2016-02-11')
	tone = json.dumps(tone_analyzer.tone(text=txt), indent=2)
	print(tone)
	return tone

analyze_tone(txt)