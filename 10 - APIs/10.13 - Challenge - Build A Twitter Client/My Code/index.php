<?php

require "twitteroauth/autoload.php";

use Abraham\TwitterOAuth\TwitterOAuth;

$consumer_key         = "1aJM7MpTDePN8U1CvyslP3lto";
$consumer_secret      = "QVvAmHwsYrzDyLsWZXe08KcwvujE9O1feufaGR1sIoncWP0nY2";
$access_token         = "732875185783746560-ewCzfOio1P12nOClbwttshOka418FMi";
$access_token_secret  = "H5a82QBvALmS2ozQHmYBegeVWBjqitQU66k9lreWxBXI8";

$connection = new TwitterOAuth($consumer_key, $consumer_secret, $access_token, $access_token_secret);
$content = $connection->get("account/verify_credentials");

$statuses = $connection->get("statuses/home_timeline", ["count" => 25, "exclude_replies" => true]);

//foreach($statuses as $tweet) {
//  if($tweet->favorite_count >= 100) {
//      echo("<p>" . $value->text . "</p>");
//  };
//};

//Based on after watching lecture, way of displaying tweets

foreach($statuses as $tweet) {
  if($tweet->favorite_count >= 100) {
      $status = $connection->get("statuses/oembed", ["id" => $tweet->id]);
      echo($status->html);
  };
};

?>
