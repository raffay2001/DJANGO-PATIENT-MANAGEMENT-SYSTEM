/* 
All scripts extends here to all the pages
*/

// 1) if no patient is found :(
$(document).ready(function() {
    var verify = $('#chk_td').length;
    if (verify == 0){
        $('#no-data').html('No Patient Found !!');
    }
});


// 2) Time Running at Real Time 
setInterval(function(){
    var date = new Date();
    $('#clock').html(
        (date.getHours() < 10 ? '0' : '') + date.getHours() +  ':' + (date.getMinutes() < 10 ? '0' : '') + date.getMinutes() +  ':' + (date.getSeconds() < 10 ? '0' : '') + date.getSeconds()
    );
}, 500);


function validateEmail(email){
    var regex = ' /^([a-zA-Z0-9_.+-])+\@(([a-zA-Z0-9-])+\.)+([a-zA-Z0-9]{2,4})+$/';
    return regex.test(email);
}

function validateAll(){
    var name = $('#name').val();
    var phone = $('#phone').val();
    var email = $('#email').val();
    var age = $('#age').val();
    var gender = $('#gender').val();

    if ( name == '' ){
        swal('Oopsss !', 'Name field cannot be empty', 'error');
        return false;
    }

    else if ( name == name.toUpperCase() ){
        swal('Oopsss !', 'Name cannot be in uppercase.', 'error');
        $('#name').val('');
        return false;
    }

    else if ( name.split(' ').length < 2 ){
        swal('Oopsss !', 'Put atleast the last name', 'error');
        return false;
    }


    else if ( phone == '' ){
        swal('Oopsss !', 'Phone field cannot be empty', 'error');
        return false;
    }

    else if ( email == '' ){
        swal('Oopsss !', 'Email field cannot be empty', 'error');
        return false;
    }

    else if ( !(validateEmail(email)) ){
        swal('Oopsss !', 'Put a valid email address', 'error');
        $('#email').val('');
        return false;
    }

    else if ( age == '' ){
        swal('Oopsss !', 'Age field cannot be empty', 'error');
        return false;
    }

    else if ( gender == '' ){
        swal('Oopsss !', 'Gender field cannot be empty', 'error');
        return false;
    }

    else{
        return true;
    }

}

$('#btn-add').bind('click', validateAll);


$(document).ready(function() {
    jQuery('input[name="name"]').keyup(function (){
        var letter = jQuery(this).val();
        var allow = letter.replace(/[^a-zA-Z _]/g, '');
        jQuery(this).val(allow);
    });
    // Prevent starting space 
    $('input').on('keypress', function (e){
        if (e.which === 32 && !this.value.length){
            e.preventDefault();
        }
    });   
});


$(document).ready(function(){
    $('name').keyup( function(){
    var name = $('#name').val();
    if (name.split(' ').length === 3){
        swal('Oopsss !', 'Only Name and Last Name', 'info');
        $('#name').val('');
        return false;
    }
});
});

$('#name').keyup(function(){
    var txt = $(this).val();
    $(this).val(txt.replace(/^(.)|\s(.)/g, function($1){
        return $1.toUpperCase();
    }));
});


$(document).ready(function(){
    $('#phone').inputmask("(99) 99999-9999", {"onicomplete": function(){
        swal('Oopsss !', 'incomplete phone. Please review !', 'info');
        $('#phone').val('');
        return false;
    }
    });
});


$(document).ready(function(){
    $('#email').keyup(function(){
        this.value = this.value.toLowerCase();
    });
});


$(document).ready(function(){
    $('#age').keyup(function(){
        var age = $('#age').val();
        if (age > 100){
            swal('Denied !', 'The maximum value is 100 years old.', 'error');
            $('#age').val('');
            return false;
        }
    });
});

$('#age').keyup(function(){
   if (!/^[0-9]*$/.test(this.value)) {
       this.value = this.value.split(/[^0-9]/).join('');
   }
});


$('#age').on("input", function(){
    if (/^0/.test(this.value)){
        this.value = this.value.replace(/^0/, "");
    }
});