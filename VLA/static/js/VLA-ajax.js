$(document).ready(function() {

    $('#definition_suggestion').keyup(function(){
        var query;
        query = $(this).val();
        $.get('/VLA/suggest_definition/', {definition_suggestion: query}, function(data){
         $('#defs').html(data);
        });
    }); 

});
