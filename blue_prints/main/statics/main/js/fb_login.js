function log_in(){
    FB.api('/me?fields=id,name,email', function (response) {
        var obj = {
            id: response.id,
            email: response.email,
            name: response.name,
        };
        var data_json = JSON.stringify(obj, null, '\t');
        $.ajax({
            type: "POST",
            url: "/fb/fb_login",
            data: data_json,
            contentType: 'application/json;charset=UTF-8',
            success: function(data) {
                location.reload();
            }
        });
    });
}

function check_login_state(){
    FB.login(function(response) {
        if (response.status === 'connected') {
            log_in();
        }
    }, {
        scope: 'public_profile, email',
        return_scopes: true
    });
}

function log_out() {
    $.ajax({
        method: "POST",
        url: "/fb/logout",
        success: function(data) {
            if(data == "true"){
                location.reload()
            }
        },
        error: function(){
			alert("Something went wrong.")
		}
    });
}

function fb_img(){
    FB.getLoginStatus(function (response) {
        if (response.status === 'connected') {
            FB.api('/me?fields=id,name,email', function (response) {
                $('#fb_img').html('<img class="fb_img" src="'+'http://graph.facebook.com/' + response.id + '/picture">');
            });
        }
    });
}

function fb_img(){
    FB.getLoginStatus(function (response) {
        if (response.status === 'connected') {
            FB.api('/me?fields=id,name,email', function (response) {
                $('#fb_img').html('<img class="fb_img" src="'+'http://graph.facebook.com/' + response.id + '/picture">');
            });
        }
    });
}




