$(function() {
  $("#json_title_text").text('Please select an item to the right...');
});

//Change selected item
$(".item").click(function () {
  // $("#todo_item").css('background-color', '#ca0000ff')
  //$("#todo_item").css('color', '#ca0000ff')

  $("#todo_item").fadeTo(400, 0, function() {
    $("#todo_item").delay(400);
    $("#todo_item").fadeTo(400, 1);
  })
  var id = $(this).get(0).id;
  setTimeout(function(){
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
        var due_date = data['due_date'].split('-');
        var due_date = due_date[1] + '/' + due_date[2].slice(0,2) + '/' + due_date[0]
        $("#json_due_date").text('Due Date: ' + due_date);
        $("#json_add_date").text('Add Date: ' + data['add_date']);
        // $("#json_priority").text('Priority: ' + data['priority']);

        //setTimeout(function(){ $("#todo_item").css('background-color', '#ecececff') }, 400)
        //setTimeout(function(){ $("#todo_item").css('color', 'black') }, 400)
      }
    });
  }, 600);
});

//Show/hide overlay form for new items
$("#add").click(function (){
  $("#new_item").css('display', 'block');
});
$("#cancel_button").click(function (){
  $("#new_item").css('display', 'none');
});
