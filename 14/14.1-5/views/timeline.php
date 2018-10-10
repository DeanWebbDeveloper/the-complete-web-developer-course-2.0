<div class="container mainContainer">
  <div class="row p-0 m-0">
    <div class="col-md-8">
      <h2>Tweets For You</h2>

      <?php displayTweets('isFollowing'); ?>

    </div>
    <div class="col-md-4">

      <?php displaySearch() ?>

      <hr />

      <?php displayTweetBox() ?>

    </div>
  </div>
</div>
