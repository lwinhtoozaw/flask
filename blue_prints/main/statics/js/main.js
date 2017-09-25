function load(){
    $.ajax({
        type: "POST",
        url: "/a_block",
        success: function(data){
            $('#a_block').html(data);
        }
    });
}

