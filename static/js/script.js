$(function() {
    $('input[type=submit]').click(function(){
        var roadid = $('#txtRoadid').val();
        var direction = $('#txtDirection').val();
        var day = $('#txtDay').val();
        var time = $('#txtTime').val();
        var trafficstatus = $('#txtTrafficstatus').val();
        console.log("hi")
        $.ajax({
            url: '/storedata',
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