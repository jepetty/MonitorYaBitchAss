package Watson;

import com.ibm.watson.developer_cloud.tone_analyzer.v3.ToneAnalyzer;
import com.ibm.watson.developer_cloud.tone_analyzer.v3.model.ToneAnalysis;

/** Class to analyze tone of messages using IBM Watson **/ 
public class WatsonTone {
	public static String getText(String input) {
		String Text = input;
		return Text;
	}
	public static void main(String[] args) {
		
		ToneAnalyzer service = new ToneAnalyzer(ToneAnalyzer.VERSION_DATE_2016_02_11);
		service.setUsernameAndPassword(credentials.watsonUser,credentials.watsonPassword);
		String text = getText(args[0]);
		System.out.println(text);
		//text = "Innapropriate content";
		ToneAnalysis tone = service.getTone(text);
		System.out.println(tone);
	}

}
