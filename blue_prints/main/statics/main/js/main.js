function load(){
    $.ajax({
        type: "POST",
        url: "/a_block",
        success: function(data){
            $('#a_block').html(data);
        }
    });
}


function slide() {
    var status = $('#slide').text();
    if(status == "close"){
        document.getElementById("mySidenav").style.width = "100%";
        $('#slide').text("open");
    }else if(status == "open"){
        document.getElementById("mySidenav").style.width = "0";
        $('#slide').text("close");
    }
}