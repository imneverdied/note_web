var NAME = [];
var CONTENT = [];


$(document).ready(function () {
    $.ajaxSetup({ cache: false });
    $.getJSON('note.json', function (data) {
        Gdata = data;

        /* loop through array */
        $.each(data, function (index, d) {
            NAME.push(d.NAME);
            CONTENT.push(d.CONTENT);
        });


        for (i = 0; i < NAME.length; i++) {
            $(id_name).append('<label id ="name"><strong>' + NAME[i] + '</strong></label></br>');
            $(id_name).append('<label id ="content">' + CONTENT[i] + '</label></br>');
        }

        //========================
    });
});
