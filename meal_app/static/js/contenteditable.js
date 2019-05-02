$('td[contenteditable=true]').blur(function () {
    $(this).parent('tr').find('button').removeAttr('disabled');

});
$('button').click(function () {
    var contents = $(this).parents().find('td[contenteditable=true]');
    var contentArray = [];
    for (i = 0; i < contents.length; i++) {
        contentArray[i] = contents[i];
    }
    console.log(contentArray);
    $.post("test.php", contentArray);
});
