var testdata;
$(".item").click(function () {
  var id = $(this).get(0).id;
  console.log(id)
  $.ajax({
    url: 'ajax/',
    data: {
      'id': id
    },
    dataType: 'json',

    success: function (data) {
      console.log(data);
      testdata = JSON.parse(data);
      $("#json_test").text(data);
    }
  });
});
