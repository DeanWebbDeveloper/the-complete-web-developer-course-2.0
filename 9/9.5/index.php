<?php

    $link = mysqli_connect("Insert Server Hosting Address", "Insert Database Name", "Insert Password Key", "Insert Database Name");   //Available at ecowebhosting.co.uk

    if(mysqli_connect_error()) {

        die ("Could not connect to database");

    }

    $query = "SELECT * FROM users";

    if ($result = mysqli_query($link, $query)) {

        $row = mysqli_fetch_array($result);

        echo ("Your email is " . $row["email"] . ".<br /><br />");
        echo ("Your password is " . $row["password"] . ".");

    }

?>
