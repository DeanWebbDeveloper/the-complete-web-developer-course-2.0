<?php

    mysqli_connect("localhost", "cl59-users-ato", "d!CrF.cyx");

    if(mysqli_connect_error()) {

        echo ("Could not connect to database");

    } else {

        echo ("Connection to database was successful");

    };

?>
