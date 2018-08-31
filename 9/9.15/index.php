<?php

    $salt = "djhsdbjhsdbjh37978qw3y98dq90";   //Safe to keep, testing value

    $row['id'] = 73;

    echo md5(md5($row['id'])."password");

    //md5 is not secure, it is much better to use bcrypt. PHP >= 5.5 has this built-in, so look into using this instead

    $hash = password_hash("rasmuslerdorf", PASSWORD_DEFAULT);

    if (password_verify('rasmuslerdorf', $hash)) {
        echo 'Password is valid!';
    } else {
        echo 'Invalid password.';
    }

?>
