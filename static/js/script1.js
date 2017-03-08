$(function() {
     $('input[type=submit]').click(function(){
        var roadid = $('#txtRoadid').val();
        var direction = $('#txtDirection').val();
        var day = $('#txtDay').val();
        var time = $('#txtTime').val();
        $.ajax({
            url: '/predictdata',
            data: $('form').serialize(),
            type: 'POST',
            success: function(response) {
                console.log(response);
            },
            error: function(error) {
                console.log(error);
            }
        });
    });
});