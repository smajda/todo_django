$( function() {
  $( "#due_date" ).datepicker();
} );
$( function() {
  $( "#add_date" ).datepicker();
} );

$( document ).ready(function() {
  $("#add_date").datepicker("setDate", '+0');
});
