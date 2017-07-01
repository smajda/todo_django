$(function() {
  id = $( ".item:first" ).get(0).id
  item_ajax(id)
});

function item_ajax(item_id) {
  //Retrive an item from the right-hand side list

  //Animation stuff
  $("#todo_item").fadeTo(400, 0, function() {
    $("#todo_item").delay(400);
    $("#todo_item").fadeTo(400, 1);
  })
  setTimeout(function(){
    $.ajax({
      url: 'ajax/',
      data: {
        'id': item_id
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
        //$("#json_complete").text(data['complete']);
        //"<input type="checkbox" name="complete" value="True" checked> Complete?")
        var checkbox = $('input[name="item_complete"]')
        if (data['complete'] == false) {
          checkbox.prop('checked', false);
        } else if (data['complete'] == true) {
          checkbox.prop('checked', true);
        } else {
          alert("ERROR WITH CHECKBOX")
        }
        checkbox.attr('id', item_id);
      }
    });
  }, 600);
}

$(".item").click(function () {
  //Change selected item
  var id = $(this).get(0).id;
  item_ajax(id)
});


$('input[name="item_complete"]').on('change', function () {
  var checkbox = $('input[name="item_complete"]')
  var item_id = checkbox.get(0).id;
  var complete = checkbox.is(':checked');
  console.log(item_id)

  $.ajax({
    url: 'complete_item/',
    data: {
      'id': item_id,
      'complete': complete
    },
    dataType: 'json',

    success: function (data) {
      var item_complete_element = $("#" + item_id +".complete_info")
      if (complete){
        item_complete_element.html("<b>Complete:</b> <span style='color: green'>True</span>")
      } else if (!complete){
        item_complete_element.html("<b>Complete:</b> <span style='color: red'>False</span>")
      } else {
        console.log("ERROR WITH CHECKBOX JS")
      }
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
