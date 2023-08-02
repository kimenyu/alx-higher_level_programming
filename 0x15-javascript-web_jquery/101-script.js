$(document).ready(function(){
	$('#add_item').click(function() {
		$('li').append('<li>Item</li>');
	});

	$('#remove_item').click(function() {
		const $lastElement = $('li').last();

    // Remove the last <li> element using .remove()
    	$lastElement.remove();
	});

	$('#clear_list').click(function() {
		$('.my_list').empty();
	});
});
