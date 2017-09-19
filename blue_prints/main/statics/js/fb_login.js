function check_login_state(){
    FB.login(function(response) {
        if (response.status === 'connected') {
            // Logged into your app and Facebook.
            FB.api('/me?fields=id,name,email', function (response) {
                console.log(response)
            });
        }else {
            var obj = {
                id : response.authResponse.userID
            };
            var data_json = JSON.stringify(obj, null, '\t');
            $.ajax({
                type: "POST",
                url: "/fb/fb_login",
                data: data_json,
                contentType: 'application/json;charset=UTF-8',
                success: function(data) {
                    $('#error').html(data)
                }
            });
        }
    }, {
        scope: 'public_profile, email',
        return_scopes: true
    });
}


