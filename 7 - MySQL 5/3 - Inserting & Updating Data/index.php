<?php

    $link = mysqli_connect("localhost", "cl59-users-ato", "d!CrF.cyx", "cl59-users-ato");

    if(mysqli_connect_error()) {

        die ("Could not connect to database");

    }

    //$query = "INSERT INTO `users` (`email`, `password`)
    //VALUES ('halibut@live.co.uk', 'pidgeon')";

    $query = "UPDATE `users` SET password = '123456@gmail.com' WHERE email = 'webb.christopher@live.co.uk' LIMIT 1";

    mysqli_query($link, $query);

    $query = "SELECT * FROM users";

    if ($result = mysqli_query($link, $query)) {

        $row = mysqli_fetch_array($result);

        echo ("Your email is " . $row["email"] . ".<br /><br />");
        echo ("Your password is " . $row["password"] . ".");

    }

?>
