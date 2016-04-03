<!DOCTYPE html>
<html>
<?php require'/firebase-php/src/firebaseLib.php';?>

<head>
<meta charset="UTF-8"> 
<title>Bitchyness Tracker</title>
<!--Bootstrap-->
<!-- Latest compiled and minified CSS -->
<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/css/bootstrap.min.css" integrity="sha384-1q8mTJOASx8j1Au+a5WDVnPi2lkFfwwEAa8hDDdjZlpLegxhjVME1fgjWPGmkzs7" crossorigin="anonymous">

<!-- Optional theme -->
<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/css/bootstrap-theme.min.css" integrity="sha384-fLW2N01lMqjakBkx3l/M9EahuwpSfeNvV63J5ezn3uZzapT0u7EYsXMjQV+0En5r" crossorigin="anonymous">

</head>
<body>

<style>
	body { padding-top: 70px; 
		   padding-left: 20px;
		}
	.row { padding-top: 70px; 
			padding-bottom: 70px; }
	span.glyphicon {
    font-size: 50px;  
	}
</style>

<nav class="navbar navbar-inverse navbar-fixed-top" id="nav">
  <div class="container">
    <div class="navbar-header">
      <a class="navbar-brand" href="#nav">MonitorYourTexts</a> </div>
  </div>
</nav>

<form class >
<h1>What are you planning on sayinggttggg?</h1>
<textarea class="form-control" rows="3"></textarea>
<button type="submit" class="btn btn-default">Whats the sentiment?</button>
</form>


<?php
	// echo('ripppp');

	CONST DEFAULT_URL = 'https://sigjesus.firebaseio.com/';
	CONST DEFAULT_TOKEN = 'VBCjMRQi5IyEdMb4B2Kt2VFoov8egXyixl5ae4Qw';
	CONST DEFAULT_PATH = '/sigjesus';

	$firebase = new \Firebase\FirebaseLib(DEFAULT_URL, DEFAULT_TOKEN);

	// --- storing an array ---
	// $firebase->set(DEFAULT_PATH . '/' . $dateTime->format('c'), $test);

	// --- storing a string ---
	$message = $firebase->get(DEFAULT_PATH . '/document_tone/messages/gyfutyfgyutfytguh');
	// echo($message);
	// echo(typeof($message));
	echo($message);
	// --- reading the stored string ---
	// $name = $firebase->get(DEFAULT_PATH . '/name/contact001');

?>

<!-- JavaScript files should be linked at the bottom of the page  -->
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.11.3/jquery.min.js"></script>
    <!-- Latest compiled and minified JavaScript -->
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.5/js/bootstrap.min.js"></script>
  </body>
</html>



