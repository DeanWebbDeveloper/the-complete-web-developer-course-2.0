<!DOCTYPE html>

<html>

    <head>

      <title>Testing loops in MySQL</title>

    </head>

    <body>

        <form method="post">

            <label>Email:</label><br />
            <input type=email name="email" required />

            <br /><br />

            <label>Password:</label><br />
            <input type=password name="password" required />

            <br /><br />

            <input type=submit />

        <!--

        ask email and password

        check email and pass entered

        check email is not already registered

        if okay, sign up, put in database

        -->

        </form>

        <?php

            if (array_key_exists('email', $_POST) OR array_key_exists('password', $_POST)) {

                $error = "";

                if ($_POST["email"] && filter_var($_POST["email"], FILTER_VALIDATE_EMAIL) === false) {

                    $error .= ("The email address provided is invalid. <br/>");

                }

                if ($_POST["email"] == null) {

                    $error .= ("You have not input an email. <br/>");

                }

                if ($_POST["password"] == null) {

                    $error .= ("You have not input a password. <br/>");

                }

                if($error != "") {

                    echo ($error);

                } else {

                    $link = mysqli_connect("Insert Server Hosting Address", "Insert Database Name", "Insert Password Key", "Insert Database Name");   //Available at ecowebhosting.co.uk

                    if(mysqli_connect_error()) {

                        die ("Could not connect to database");

                    };

                    $email_check = "SELECT * FROM users WHERE email = '".mysqli_real_escape_string($link, $_POST["email"])."'";

                    $result = mysqli_query($link, $email_check);

                    if (mysqli_num_rows($result) > 0) {

                        echo ("That email has already been used");

                    } else {

                        $query = "INSERT INTO `users` (email, password) VALUES ('".mysqli_real_escape_string($link, $_POST["email"])."', '".mysqli_real_escape_string($link, $_POST["password"])."')";

                        if (mysqli_query($link, $query)) {

                            echo ("You have been signed up!");

                        } else {

                            echo ("We could not sign you up, please try again later.");

                        };

                    };

                };

            };



        ?>

    </body>

</html>
