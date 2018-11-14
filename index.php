<?php
if(isset($_GET["pin"]) && !empty($_GET["pin"]))
{
	$pin = $_GET["pin"];
	if($pin == "0504")
	{
		echo "welcome";
	}
	else
	{
		echo "go away";
	}
}
else
{
	include("form.html");
}
#EOF