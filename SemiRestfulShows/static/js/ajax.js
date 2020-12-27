$(document).ready(function(){
    $('#showtitle').keyup(function(){
        var data = $("#showform").serialize()   // capture all the data in the form in the variable data
        $.ajax({
            method: "GET",   // we are using a post request here, but this could also be done with a get
            // url: {% url 'title_check' %},
            data: data
        })
        .done(function(res){
             $('#titlemsg').html(res)  // manipulate the dom when the response comes back
        })
    })
})