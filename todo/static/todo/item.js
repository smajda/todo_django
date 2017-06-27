//CHange selected item
$(".item").click(function () {
  $("#todo_item").css('background-color', '##ca0000ff')
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

      $("#todo_item").css('background-color', '#ecececff')
    }
  });
});


//Show/hide overlay form for new items

$("#add").click(function (){
  $("#new_item").css('display', 'block');
});
$("#cancel_button").click(function (){
  $("#new_item").css('display', 'none');
});

/*
// https://stackoverflow.com/questions/2457246/jquery-click-function-exclude-children
$("#new_item").click(function (){
  $("#new_item").css('display', 'none');
}).children().click(function(e) {
  return false;
});
*/
