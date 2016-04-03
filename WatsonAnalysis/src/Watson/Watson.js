console.log('hello, world!');
getString('Hey! my name is Jessica! Im super awesome most of the time except when Im not. Be my friend!');

function getString(txt) {
	var watson = require('watson-developer-cloud');

    var exports = require('./credentials.js');

    var tone_analyzer = watson.tone_analyzer({
	    username: exports.watson_username,
	    password: exports.watson_password,
	    version: 'v3-beta',
	    version_date: '2016-02-11'
    });

    tone_analyzer.tone({ text: txt },
    	function(err, tone) {
    		watsonTone = '';
    		if (err)
    			console.log(err);
    		else 
    			watsonTone = JSON.stringify(tone, null, 2);

    	    return callback(watsonTone);
    	});

   /* statement.get(function(err, col) {
         temp = col;
         callback(temp);
     });*/

function callback(param) {
	// invoke python script with json as command line argument, do this in python function
	console.log(param);
    return param;
}

    return watsonTone;
}







		/*String text = getText(args[0]);
		System.out.println(text);
		//text = "Innapropriate content";
		ToneAnalysis tone = service.getTone(text);
		System.out.println(tone);
		String pypath = "parse.py";
		String[] cmd = new String[3];
		cmd[0] = "python";
		cmd[1] = pypath;
		cmd[2] = tone;*/