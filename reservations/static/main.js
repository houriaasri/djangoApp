$(document).ready(function() {
    console.log("main.js loaded");

    $("#yourFormId").submit(function(e) {
        console.log("Form submitted");
        e.preventDefault();

        $.ajax({
            type: 'POST',
            url: '/api/make-reservation/',
            data: {
                first_name: $('#name').val(),
                reservation_date: $('#reservation_date').val(),
                reservation_slot: $('#reservation_time').val(),
                csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val()  // Ajoutez ceci pour inclure le token CSRF
            },
            success: function(response) {
                 
            
                let newBooking = '<p>' + $('#name').val() + ' - ' + $('#reservation_time').val() + '</p>';
                $('#bookingsContainer').append(newBooking);
            },
            
            
            error: function(error) {
                console.error("Erreur lors de la réservation:", error.responseText);
            }
            
        });
        
    });
});
