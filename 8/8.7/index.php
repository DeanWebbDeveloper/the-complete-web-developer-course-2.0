<?php

$myArray = array("Chris", "Anthony", "Joe", "Brian");

$myArray[] = "Katie";

print_r($myArray);

echo $myArray[2];

echo "<br><br>";

$anotherArray[0] = "pizza";

$anotherArray[1] = "yoghurt";

$anotherArray[5] = "coffee";

$anotherArray["myFavouriteFood"] = "ice cream";

print_r ($anotherArray);

echo "<br><br>";

$thirdArray = array(
    "France" => "French",
    "USA" => "English",
    "Germany" => "German");

unset($thirdArray["France"]);

print_r($thirdArray);

echo sizeof($thirdArray);

 ?>
