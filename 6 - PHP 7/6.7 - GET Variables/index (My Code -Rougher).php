<?php

    $numerator = $_GET["number"];

    if ($numerator == "") {

        echo "You have not entered a number below";

    } else {

        $denominator = 2;

        while ($denominator < $numerator && is_int($numerator/$denominator) == false) {

            $division = $numerator/$denominator;
            $denominator++;
        }

        if ($numerator == 1) {

              echo "The number, ". $numerator. ", is a not prime number!";

        } elseif ($numerator == 2) {

            echo "The number, ". $numerator. ", is a prime number!";

        } else {

            if ($denominator == $numerator) {

                echo "The number, ". $numerator. ", is a prime number!";

            } else {

                echo "The number, ". $numerator. ", is a not prime number!";

            }

        }

    }

 ?>

<p>Is the number Prime?</p>

<form>

<input name="number" type="number" placeholder="Select a number">
<input type="submit" value="Go!">

</form>
