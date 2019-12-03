$(document).ready(function(){
    var ajaxForm = $(".form_ajax")
    ajaxForm.submit(function(event){
        event.preventDefault();
        console.log("form is not sending");
        var thisForm =$(this);
        var actionEndpoint = thisForm.attr("action")
        var httpMethod = thisForm.attr("method") ;
        var formData = thisForm.serialize();

        $.ajax({
            url: actionEndpoint,
            method: httpMethod,
            data: formData,
            success: function(response){
                alert(response)
            }
        })
    })
})