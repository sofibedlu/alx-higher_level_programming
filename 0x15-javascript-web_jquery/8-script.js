$.ajax({
  url: 'https://swapi-api.alx-tools.com/api/films/?format=json',
  type: 'GET',
  success: function (response) {
    const films = response.results;
    for (const film of films) {
      $('#list_movies').append(`<li>${film.title}</li>`);
    }
  },
  error: function (jqXHR, textStatus, errorThrown) {
    console.log(textStatus, errorThrown);
  }
});
