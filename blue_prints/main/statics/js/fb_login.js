function check_login_state(){
    FB.login(function(response) {
        if (response.status === 'connected') {
            // Logged into your app and Facebook.
            FB.api('/me?fields=id,name,email', function (response) {
                console.log(response)
            });
        }
    }, {
        scope: 'public_profile, email',
        return_scopes: true
    });
}


