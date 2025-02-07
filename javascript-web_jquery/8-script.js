$.get('https://swapi-api.alx-tools.com/api/films/?format=json', function (data, textStatus) {
  $('UL#list_movies').append(data.results.map(film => `<li>${film.title}</li>`));
});
