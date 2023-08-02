$(document).ready(function() {
	$.get('https://swapi-api.alx-tools.com/api/films/?format=json', function(data){
		$.each(data.results, function(index, movie) {
			const $li = $('<li>').text(movie.title);
			const $ul = $('#list_movies');


      // Append the li element to the ul
      		$ul.append($li);
		});
	});
});
