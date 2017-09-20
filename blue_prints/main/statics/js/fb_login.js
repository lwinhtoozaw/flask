function login(){
    FB.api('/me?fields=id,name,email', function (response) {
        var obj = {
            id: response.id
        };
         var data_json = JSON.stringify(obj, null, '\t');
        $.ajax({
            type: "POST",
            url: "/fb/fb_login",
            data: data_json,
            contentType: 'application/json;charset=UTF-8',
            success: function(data) {
                $('#error').html(data)
                $('#email').html(response.email)
            }
        });
    });
}

function check_login_state(){
    FB.login(function(response) {
        if (response.status === 'connected') {
            login();
        }
    }, {
        scope: 'public_profile, email',
        return_scopes: true
    });
}


