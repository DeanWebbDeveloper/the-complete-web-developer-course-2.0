<footer class="footer">
  <div class="container">
    <p>&copy;My Website 2018</p>
  </div>
</footer>

<!-- jQuery first, then Popper.js, then Bootstrap JS -->
<script src="https://code.jquery.com/jquery-3.3.1.min.js" integrity="sha256-FgpCb/KJQlLNfOu91ta32o/NMZxltwRo8QtmkMRdAu8=" crossorigin="anonymous"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.12.9/umd/popper.min.js" integrity="sha384-ApNbgh9B+Y1QKtv3Rn7W3mgPxhU9K/ScQsAP7hUibX39j7fakFPskvXusvfa0b4Q" crossorigin="anonymous"></script>
<script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js" integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl" crossorigin="anonymous"></script>

<!-- Modal -->
<div class="modal fade" id="exampleModalCenter" tabindex="-1" role="dialog" aria-labelledby="exampleModalCenterTitle" aria-hidden="true">
  <div class="modal-dialog modal-dialog-centered" role="document">
    <div class="modal-content">
      <div class="modal-header">
        <h5 class="modal-title" id="loginModalTitle">Login</h5>
        <button type="button" class="close" data-dismiss="modal" aria-label="Close">
          <span aria-hidden="true">&times;</span>
        </button>
      </div>
      <div class="modal-body">
        <div class="alert alert-danger" id="loginAlert"></div>
        <form>
          <input type="hidden" id="loginActive" name="loginActive" value="1" />
          <div class="form-group">
            <label for="email">Email</label>
            <input type="email" class="form-control" id="email" placeholder="Email address">
          </div>
          <div class="form-group">
            <label for="password">Password</label>
            <input type="password" class="form-control" id="password" placeholder="Password">
          </div>
        </form>
      </div>
      <div class="modal-footer">
        <a id="toggleLogin">Sign up</a>
        <button type="button" class="btn btn-secondary" data-dismiss="modal">Close</button>
        <button type="button" id="loginSignupButton" class="btn btn-primary">Login</button>
      </div>
    </div>
  </div>
</div>

<script>

  $("#toggleLogin").click(function() {

    if($("#loginActive").val() == "1") {

      $("#loginActive").val("0");
      $("#loginModalTitle").html("Sign Up");
      $("#loginSignupButton").html("Sign Up");
      $("#toggleLogin").html("Login");

    } else {

      $("#loginActive").val("1");
      $("#loginModalTitle").html("Login");
      $("#loginSignupButton").html("Login");
      $("#toggleLogin").html("Sign Up");

    };

  });

  $("#loginSignupButton").click(function() {

    $.ajax({
      type:     "POST",
      url:      "actions.php?action=loginSignup",
      data:     "email=" + $("#email").val() +
                "&password=" + $("#password").val() +
                "&loginActive=" + $("#loginActive").val(),
      success:  function(result) {
                  if (result == "1") {
                    window.location.assign("https://www.deanwebbdeveloper.com/the_sandbox");
                  } else {
                    $("#loginAlert").html(result).show();
                  };
                }
    });

  });

  $(".toggleFollow").click(function() {

    var id = $(this).attr("data-userId")

    $.ajax({
      type:     "POST",
      url:      "actions.php?action=toggleFollow",
      data:     "userID=" + id,
      success:  function(result) {
                  if (result == "1") {

                    $("a[data-userId='" + id + "']").html("Follow");
                    
                  } else if (result == "2") {

                    $("a[data-userId='" + id + "']").html("Unfollow");

                  }
                }
    });

  });

</script>

</body>
</html>
