$(document).ready(function() {

    $('#definition_suggestion').keyup(function(){
        var query;
        query = $(this).val();
        $.get('/VLA/suggest_definition/', {definition_suggestion: query}, function(data){
         $('#defs').html(data);
        });
    });
    
    $('#question_suggestion').keyup(function(){
        var query;
        query = $(this).val();
        $.get('/VLA/suggest_question/', {question_suggestion: query}, function(data){
         $('#ques').html(data);
        });
    });
    
    $('#question_suggestion2').keyup(function(){
        var query;
        query = $(this).val();
        $.get('/VLA/suggest_question/', {question_suggestion: query}, function(data){
         $('#ques2').html(data);
        });
    });

});

