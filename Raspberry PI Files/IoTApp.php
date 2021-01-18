<?php

if(isset($_POST['connect'])){
	
	system("cmd /c START broker.bat");
}
if(isset($_POST['submit'])){
	if($_POST['p1'] == "mqtt" && $_POST['p2']== "coap"){
		system("cmd /c START broker1.bat");
	}
	if($_POST['p1'] == "coap" && $_POST['p2']== "mqtt"){
		system("cmd /c START broker2.bat");

	}
}

?>
<html>
<head>
<title> IoT Data Communication</title>
</head>
<body>
<form action="#" method="post">
<h1><center> IoT Data Communication</center></h1>
<table align="center" border="0">
<tr><td colspan =4><hr><br></td></tr>
<tr><td colspan =4><hr><br></td></tr>
<tr>
<td colspan =2 align="center">Host Address: </td>
<td colspan=2> 
<input type="text" name="host" id="host"></td>
</tr>


<tr>
<td colspan =2 align="center">Port Number:</td>
<td colspan=2> <input type="text" name="port" id="port"></td>
</tr>


<tr>
<td colspan =4> <hr> <br><center>  
<input type="submit" name="connect" value="Connect" ></center><br><hr>
</td>
</tr>
</table>
</form>


<form action="#" method="post">
<table align="center">
<tr>
<td>Sender Protocol:</td><td> <select name="p1">
			<option value="mqtt"> MQTT </option>
			<option value="coap"> CoAP </option>
		</select></td>
<td align="right">Receiver Protocol:</td><td> <select name="p2">
			<option value="coap"> CoAP </option>
			<option value="mqtt"> MQTT </option>
		</select>
</td>
</tr>

<tr>
<td colspan =2 align="center">Topic:</td>
<td colspan=2> <input type="text" name="topic" id="topic">
</td>
</tr>

<tr>
<td colspan =2 align="center" valign="top">Message: 
</td>
<td colspan=2> <textarea name="r_message" id="r_message" rows="5" cols="22"> </textarea></td>
</tr>

<tr>
<td colspan =4><hr> <br><center> <input type="submit" name="submit" value="Send Message" ></center><br><hr></td>
</tr>
</table>
</form>


<form action="#" method="post">
<table align="center">
<tr>
<td colspan =2 align="center" valign="top">Received Message:</td>
<td colspan=2> <textarea name="r_message" id="r_message" rows="5" cols="22"></textarea><br></td>
</tr>

<tr><td colspan =4><hr><br></td></tr>

</table>
</form>
</body>
</html>
