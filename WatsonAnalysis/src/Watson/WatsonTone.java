package Watson;

import com.ibm.watson.developer_cloud.tone_analyzer.v3.ToneAnalyzer;

/** Class to analyze tone of messages using IBM Watson **/ 
public class WatsonTone {
	
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		System.out.println("Jess is the best!");
		
		ToneAnalyzer service = new ToneAnalyzer(ToneAnalyzer.VERSION_DATE_2016_02_11);
		System.out.println(credentials.watsonUser);
	}

}
