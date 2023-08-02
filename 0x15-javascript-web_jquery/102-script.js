$(function () {
  $('#btn_translate').on('click', function () {
    const languageCode = $('#language_code').val();

    // Use $.get() to fetch the translation
    $.get('https://www.fourtonfish.com/hellosalut/hello/', { lang: languageCode }, function (data) {
      // Update the content of the <div> tag with the translation
      $('#hello').text(data.hello);
    }).fail(function () {
      // Handle the case when the request fails
      $('#hello').text('Error fetching translation.');
    });
  });
});
