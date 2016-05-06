

$(document).ready(function(){
    
    
    $('#sellmycarform').on('submit', function(evt){
        ///this gets called when someone submits the form
        
        
        ///stop the form from doing the default submit action, instead do nothing
        evt.preventDefault();
        
        
        var title = $('#Title').val();
        var name = $('#name').val();
        var email = $('#email').val();
        var telephone = $('#telephone').val();
        var make = $('#make').val();
        var model = $('#model').val();
        var registration = $('#registration').val();
        var date = $('#date').val();
        var comment = $('#comment').val();
        
        
        var params = {title: title, name: name, email: email, telephone: telephone
                            , make: make, model: model, registration: registration
                            , date: date, comment: comment};
        
        $.ajax({"url": '/SellMyCar.html', "method": "post", "data":params, "dataType": 'json'})
            .done(function(response){
                
                // response['things']
                
                
                alert(response['message']);
                
            });
        
        
        
        
    });
    
    
    
});






