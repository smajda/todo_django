var testdata;
$(".item").click(function () {
  var id = $(this).get(0).id;
  $.ajax({
    url: 'ajax/',
    data: {
      'id': id
    },
    dataType: 'json',

    success: function (data) {
      data = JSON.parse(data);
      $("#json_title_text").text('Title: ' + data['title_text']);
      $("#json_desc_text").text('Description: ' + data['desc_text']);
      $("#json_impact_text").text('Impact: ' + data['impact_text']);
      $("#json_start_date").text('Start Date: ' + data['start_date']);
      $("#json_due_date").text('Due Date: ' + data['due_date']);
      $("#json_add_date").text('Add Date: ' + data['add_date']);
      $("#json_priority").text('Priority: ' + data['priority']);
    }
  });
});
