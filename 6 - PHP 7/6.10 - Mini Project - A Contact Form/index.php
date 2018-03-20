<!doctype html>

<html>

<head>

    <title>PHP Mini Project - Bootstrap Contact Form</title>

    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0-alpha.5/css/bootstrap.min.css" integrity="sha384-AysaV+vQoT3kOAXZkl02PThvDr8HYKPZhNT5h/CXfBThSRXQ6jW5DO2ekP5ViFdi" crossorigin="anonymous">

    <script src="https://code.jquery.com/jquery-2.2.3.min.js" integrity="sha256-a23g1Nt4dtEYOj7bR+vTu7+T8VP13humZFBJNIYoEJo=" crossorigin="anonymous"></script>
    <script src="https://code.jquery.com/ui/1.12.0-rc.2/jquery-ui.min.js" integrity="sha256-55Jz3pBCF8z9jBO1qQ7cIf0L+neuPTD1u7Ytzrp2dqo=" crossorigin="anonymous"></script>
    <script type="text/javascript" src="https://cdnjs.cloudflare.com/ajax/libs/tether/1.3.2/js/tether.min.js"></script>
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0-alpha.2/js/bootstrap.min.js" integrity="sha384-vZ2WRJMwsjRMW/8U7i6PWi6AlO1L79snBrmgiDpgIWJ82z8eA5lenwvxbMV1PAh7" crossorigin="anonymous"></script>

    <script>

    $(document).ready(function() {

        $("form").submit(function(event) {

                var error = "";

            if($("#email_input").val() == "") {

                error += "The email field is required.<br />";

            };

            if($("#subject_input").val() == "") {

                error += "The subject field is required.<br />";

            };

            if($("#email_content").val() == "") {

                error += "The content field is required.<br />";

            };

            if (error != "") {

                $("#alert_box").html('<div id="error" class="alert alert-danger"><strong>There were error(s) in your form:</strong><br />' + error + '</div>');

                return false;

            } else {

                return true;

            };

        });

    });


    </script>

</head>

<body>

    <?php

        $error = "";
        $success = "";

        if($_POST) {

            if (!$_POST["email"]) {

              $error .= "The email field is required.<br />";

            };

            if ($_POST["email"] && filter_var($_POST["email"], FILTER_VALIDATE_EMAIL) === false) {

                $error .= "The email address provided is invalid.<br />";

            };

            if (!$_POST["subject"]) {

                $error .= "The subject field is required.<br />";

            };

            if (!$_POST["message"]) {

                $error .= "The message field is required.<br />";

            };

            if ($error != "") {

                $error = ('<div id="error" class="alert alert-danger"><strong>There were error(s) in your form:</strong><br />' . $error . '</div>');

            } else {

                $emailTo = "dean@deanwebbdeveloper.com";

                $subject = $_POST["subject"];

                $body = $_POST["message"];

                $headers = "From: ". $_POST["email"];

                if (mail($emailTo, $subject, $body, $headers)) {

                    $success = ('<div id="success" class="alert alert-success">Your message has been sent, we\'ll get back to you ASAP!</div>');

                } else {

                    $error = ('<div id="error" class="alert alert-danger"><strong>The email could not be sent. We apologise for the inconvenience</strong><br /></div>');

                };

            };

        };

    ?>

    <div class="container">

        <h1>Get in Touch!</h1>

        <br />

        <div id="alert_box" name="alert_box"><?php echo $error; echo $success; ?></div>

        <form method="post">

            <div class="form-group">

                <label>Email address</label>

                <input class="form-control" type=email id="email_input" name="email" placeholder="Enter email">

                <small class="text-muted">We'll never share your email with anyone else.</small>

            </div>


            <div class="form-group">

                <label>Subject</label>

                <input class="form-control" type=text id="subject_input" name="subject">

            </div>


            <div class="form-group">

                <label>What would you like to ask us?</label>

                <textarea class="form-control" id="email_content" name="message" rows=6></textarea>

            </div>

            <button type="submit" class="btn btn-primary">Submit</button>

        </form>

    </div>

</body>

</html>
