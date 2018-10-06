<?php

  $link = mysqli_connect("shareddb1e.hosting.stackcp.net", "twitter-36372588", "fM8Ef5XVN3kF", "twitter-36372588");

  if(mysqli_connect_errno()) {

    print_r(mysqli_connect_error());
    exit();

  };

?>
