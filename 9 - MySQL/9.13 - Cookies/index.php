<?php

    setcookie("customerID", "1234", time() + 60 * 60 * 24);

    $_COOKIE["customerID"] = "test";

    echo $_COOKIE["customerID"];

?>
