$(document).ready(function () {
  $('#btn_translate').click(translate);
  $('#language_code').on('keypress', function (event) {
    if (event.which === 13) {
      translate();
    }
  });
});

function translate() {
  const url = 'https://www.fourtonfish.com/hellosalut/hello/';
  const langCode = $('#language_code').val();

  $.get(url, { lang: langCode }, function (response) {
    $('#hello').text(response.hello);
  });
}
