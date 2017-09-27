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
        document.getElementById("mySidenav").style.width = "300px";
        document.body.style.backgroundColor = "rgba(0,0,0,0.1)";
        $('#slide').text("open");
    }else if(status == "open"){
        document.getElementById("mySidenav").style.width = "0px";
        document.body.style.backgroundColor = "white";
        $('#slide').text("close");
    }
}