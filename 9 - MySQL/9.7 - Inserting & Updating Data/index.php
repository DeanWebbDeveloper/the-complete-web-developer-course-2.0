<?php

    $link = mysqli_connect("shareddb1a.hosting.stackcp.net", "cl59-users-ato", "d!CrF.cyx", "cl59-users-ato");

    if(mysqli_connect_error()) {

        die ("Could not connect to database");

    }

    //$query =  "INSERT INTO `users` (`email`, `password`)
    //          VALUES ('jane.doe@email.com','squarecircle555')";

    $query = "UPDATE `users` SET `password` = 'Super_Secure-Password12345' WHERE `email` LIKE 'johnnysmith@email.com' LIMIT 1";

    mysqli_query($link, $query);

    $query = "SELECT * FROM `users`";

    if ($result = mysqli_query($link, $query)) {

        $row = mysqli_fetch_array($result);

        echo ("Your email is " . $row["email"] . ".<br /><br />");
        echo ("Your password is " . $row["password"] . ".");

    }

?>
