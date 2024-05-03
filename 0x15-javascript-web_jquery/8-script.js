$.ajax({
  url: 'https://swapi-api.alx-tools.com/api/films/?format=json',
  method: 'GET',
  success: function (response) {
    var movies = response.results;
    $.each(movies, function(index, movie) {
      $("#list_movies").append("<li>" + movie.title + "</li>");
    });
  }
});
