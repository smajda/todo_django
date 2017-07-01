$(function() {
  id = $( ".item:first" ).get(0).id
  item_ajax(id)
});

function item_ajax(id) {
  $("#todo_item").fadeTo(400, 0, function() {
    $("#todo_item").delay(400);
    $("#todo_item").fadeTo(400, 1);
  })
  setTimeout(function(){
    $.ajax({
      url: 'ajax/',
      data: {
        'id': id
      },
      dataType: 'json',

      success: function (data) {
        data = JSON.parse(data);
        $("#json_title_text").text(data['title_text']);
        $("#json_desc_text").text(data['desc_text']);
        $("#json_impact_text").text(data['impact_text']);
        $("#json_start_date").text(data['start_date']);
        var due_date = data['due_date'].split('-');
        var due_date = due_date[1] + '/' + due_date[2].slice(0,2) + '/' + due_date[0]
        $("#json_due_date").text(due_date);
        $("#json_add_date").text(data['add_date']);
        $("#json_complete").text(data['complete']);
        // $("#json_priority").text('Priority: ' + data['priority']);

        //setTimeout(function(){ $("#todo_item").css('background-color', '#ecececff') }, 400)
        //setTimeout(function(){ $("#todo_item").css('color', 'black') }, 400)
      }
    });
  }, 600);
}

//Change selected item
$(".item").click(function () {

  var id = $(this).get(0).id;
  item_ajax(id)
});

//Show/hide overlay form for new items
$("#add").click(function (){
  $("#new_item").css('display', 'block');
});
$("#cancel_button").click(function (){
  $("#new_item").css('display', 'none');
});
