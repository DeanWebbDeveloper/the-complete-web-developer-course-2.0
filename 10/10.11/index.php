<?php

require "twitteroauth/autoload.php";

use Abraham\TwitterOAuth\TwitterOAuth;

$consumer_key         = "Insert Consumer Key, available at apps.twitter.com";
$consumer_secret      = "Insert Consumer Secret Key, available at apps.twitter.com";
$access_token         = "Insert Access Token Key, available at apps.twitter.com";
$access_token_secret  = "Insert Access Token Secret Key, available at apps.twitter.com";

$connection = new TwitterOAuth($consumer_key, $consumer_secret, $access_token, $access_token_secret);
$content = $connection->get("account/verify_credentials");

$statues = $connection->post("statuses/update", ["status" => "If this is available, it was posted from the Twitter API, available at deanwebbdeveloper.com/the_sandbox"]);

$statuses = $connection->get("statuses/home_timeline", ["count" => 25, "exclude_replies" => true]);

print_r($statuses);

?>
