$('#add_item').on('click', function () {
  const new_element = $('<li>').text('Item');
  $('UL.my_list').append(new_element);
});
