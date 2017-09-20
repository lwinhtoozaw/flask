function load(){
	$.ajax({
		url:"/a_block",
		method: "POST",
		success: function(data){
			$('#a_block').html(data);
		},
		error: function(){
			alert("Something went wrong.")
		}
	});
}