<?php

    $salt = "djhsdbjhsdbjh37978qw3y98dq90";

    $row['id'] = 73;

    echo md5(md5($row['id'])."password");

?>
