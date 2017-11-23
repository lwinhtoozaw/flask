$(document).ready(function() {
    $('#login_form').submit(function (e) {
        $.ajax({
            type: "POST",
            url: "/login_go/",
            data: $('#login_form').serialize(), // serializes the form's elements.
            success: function(data) {
                $("#response").html(data)
                setTimeout(function() {
                    $('#error').remove();
                },4000);
            }
        });
        e.preventDefault(); // block the traditional submission of the form.
    });
});