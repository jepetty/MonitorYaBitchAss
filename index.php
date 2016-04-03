<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8"> 
<title>Bitchyness Tracker</title>

<script src="https://cdn.firebase.com/js/client/2.4.2/firebase.js"></script>


<!--Bootstrap-->
<!-- Latest compiled and minified CSS -->
<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/css/bootstrap.min.css" integrity="sha384-1q8mTJOASx8j1Au+a5WDVnPi2lkFfwwEAa8hDDdjZlpLegxhjVME1fgjWPGmkzs7" crossorigin="anonymous">

<!-- Optional theme -->
<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/css/bootstrap-theme.min.css" integrity="sha384-fLW2N01lMqjakBkx3l/M9EahuwpSfeNvV63J5ezn3uZzapT0u7EYsXMjQV+0En5r" crossorigin="anonymous">

<script src="http://ajax.googleapis.com/ajax/libs/jquery/1.7.2/jquery.min.js"></script>
 <script>
 
    $(function(){   
       $('#submit').click(function(){
          var myString = $('#myString').val()
          window.alert(myString)
                    $.ajax({
                        url: "parse.py",
                        type: "post",
                        datatype:"json",
                        data: {'myString': 'myString'},

                         success: function(response){
                             alert(response.message);
                             alert(response.keys);
                        }
                    });
                });
            });
 	
   </script>
   
  <script>
    var ref = new Firebase("https://sigjesus.firebaseio.com/")

    ref.child('messages').on('value', function(snapshot){
       snapshot.forEach(function(messages){
          var key = messages.val();
          console.log(key)
          })
       })
 </script>
 
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

<form>
<h1>What are you planning on saying?</h1>
<textarea class="form-control" rows="3" value="What is the message you are thinking of sending?" id="myString" type="text"></textarea>
<button id="submit" type="submit"class="btn btn-default">Whats the sentiment?</button>

</form>

<!-- JavaScript files should be linked at the bottom of the page  -->
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.11.3/jquery.min.js"></script>
    <!-- Latest compiled and minified JavaScript -->
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.5/js/bootstrap.min.js"></script>
  </body>
</html>



