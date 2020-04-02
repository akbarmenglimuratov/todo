jQuery(function($){

	$('input:checkbox').click(function(){
		value = $(this).attr('value');
		$.ajax({
			url: '/note/done/' + value,
			data: {},
			dataType: 'json',
			success: function(data, textStatus, jqXHR) {
				if (data.success == true) {
					alert(data.message);
				} else {
					alert(data.message);
				}
			}
		});
	});
});