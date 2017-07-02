//On document load, populate the left-hand side with the first item from
//the right-hand side.
$(function() {
  //item_id is equivalent to the item's pk in the database.
  item_id = $( ".item:first" ).get(0).id
  item_ajax(item_id)
});

//Retrive an item from the right-hand side list based on item_id
//item_id is equivalent to items'pk in the database.
function item_ajax(item_id) {
  //Animation. #todo_item holds the elements that display the item's information
  //Begin with a fade to 0 opacity (disappear), wait a bit and then
  //reappear with fade to 1 opacity
  $("#todo_item").fadeTo(400, 0, function() {
    $("#todo_item").delay(400);
    $("#todo_item").fadeTo(400, 1);
  })

  //In order to give time for the animation, delay the ajax request by 600 ms
  setTimeout(function(){
    //Setup the ajax request and send it off - handled by urls.py
    $.ajax({
      url: 'show_item/',
      data: {
        'id': item_id
      },
      dataType: 'json',

      //When it returns, populate the fields in #todo_item
      success: function (data) {
        //Parse the data as JSON and begin assigning attributes to the elements
        data = JSON.parse(data);
        $("#json_title_text").text(data['title_text']);

        $("#json_desc_text").text(data['desc_text']);
        $("#json_impact_text").text(data['impact_text']);

        //Instead of everything, just get the month, date and year
        $("#json_due_date").text(date_format(data['due_date']));
        $("#json_start_date").text(date_format(data['start_date']));
        $("#json_add_date").text(date_format(data['add_date']));

        //Retrive the checkbox element.
        //If the item is complete, then check it
        //If the item is not complete, do not check it.
        var checkbox = $('input[name="item_complete"]')
        if (data['complete'] == false) {
          checkbox.prop('checked', false);
        } else if (data['complete'] == true) {
          checkbox.prop('checked', true);
        } else {
          alert("ERROR WITH CHECKBOX")
        }
        //Assign an pk to the checkbox this is used when the user clicks the
        //checkbox and the record in the database needs to be updated.
        checkbox.attr('id', item_id);
      }
    });
  }, 600);
}

function date_format(datetime){
  var date = datetime.split('-');
  return date[1] + '/' + date[2].slice(0,2) + '/' + date[0]
}

//When an item is clicked on from the right-hand side lists, display that item
//on the left-hand side.
$(".item").click(function () {
  //Retrive the elements id, equivalent to the item's pk in the database
  var id = $(this).get(0).id;
  item_ajax(id)
});


//When the checkbox is clicked, this function is called.
//Two things are accomplished: 1) The database is updated
//2) The item's complete status on the right-hand side is updated
$('input[name="item_complete"]').on('change', function () {
  //Retrive the checkbox element
  var checkbox = $('input[name="item_complete"]')
  //Get it's item_id, equivalent to item's pk in database
  var item_id = checkbox.get(0).id;
  var complete = checkbox.is(':checked');

  //Setup the ajax request and send it off - handled by urls.py
  $.ajax({
    url: 'complete_item/',
    data: {
      'id': item_id,
      'complete': complete
    },
    dataType: 'json',

    //When it returns, the database has been updated. Now the frontend
    //neeeds to be updated. Find the item from the right-hand side and
    //assign the appropriate html markup depending on if it is complete
    //or not complete
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
