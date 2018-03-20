<?php

$user = "Chris";

$family = array("Anthony", "Chris", "Katherine", "Daniel", "Peter");

foreach($family as $key => $value) {

    $family[$key] = $value." Webb";
    echo "Array item $key is $value<br>";

}

for ($i = 0; $i < sizeof($family); $i++) {

    echo $family[$i]."<br>";

}

for ($i = 10; $i >= 0; $i--) {

    echo $i."<br>";

}

 ?>
