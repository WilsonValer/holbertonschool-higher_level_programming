$(document).ready(function(){
	$.get('https://swapi-api.hbtn.io/api/films/?format=json', function(data)
	{
		$.each(data.results, function(index, value) {
			$('#list_movies').append(`<li>${data.results[index].title}</li>`);
			console.log(`${index}: ${data.results[index].title}`);
		});
	});
});
