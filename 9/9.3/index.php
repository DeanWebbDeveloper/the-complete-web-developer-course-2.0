<?php

    mysqli_connect("Insert Server Hosting Address", "Insert Database Name", "Insert Password Key");   //Available at ecowebhosting.co.uk

    if(mysqli_connect_error()) {

        echo ("Could not connect to database");

    } else {

        echo ("Connection to database was successful");

    };

?>
