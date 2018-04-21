<?php

    if ($_POST) {

        $Array = array("Chris", "Dave", "Matt", "Rebecca", "Luke");

        $Name = ($_POST["name"]);

        $i = 0;

        $UserFound = 0;

        while ($i < sizeof($Array) && $UserFound == 0) {

            if ($Name == $Array[$i]) {

                echo "Hello, ". $Name;
                $UserFound = 1;

            }  else {

                $i++;

            }

        }

        if ($UserFound == 0) {

            echo "I don't know you.";

        }

    }



 ?>

<p>What is your name?</p>

<form method="post">

<input name="name" type="text" placeholder="Enter you name">
<input type="submit" value="Go!">

</form>
