$(document).ready(function () {
  $.ajax({
    url: 'https://hellosalut.stefanbohacek.dev/?lang=fr',
    method: 'GET',
    success: function (obj) {
      $('#hello').text(obj.hello);
    }
  });
});
