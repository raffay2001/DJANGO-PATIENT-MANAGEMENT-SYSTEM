/* 
All scripts extends here to all the pages
*/

// 1) if no patient is found :(
$(document).ready(function() {
    var verify = $('#chk_td').length;
    if (verify == 0){
        $('#no-data').html('No Patient Found');
    }
});


// 2) Time Running at Real Time 
setInterval(function(){
    var date = new Date();
    $('#clock').html(
        (date.getHours() < 10 ? '0' : '') + date.getHours() +  ':' + (date.getMinutes() < 10 ? '0' : '') + date.getMinutes() +  ':' + (date.getSeconds() < 10 ? '0' : '') + date.getSeconds()
    );
}, 500);
