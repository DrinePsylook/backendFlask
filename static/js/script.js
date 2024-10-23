$('#onglet1').on("click", function(event) {
    if ($(this).hasClass('active')) {
        event.preventDefault();  // Empêche le rafraîchissement
        return; 
    }
});

$('#onglet2').on("click", function(event) {
    if ($(this).hasClass('active')) {
        event.preventDefault();  
        return; 
    }
});

$('#onglet3').on("click", function(event) {
    if ($(this).hasClass('active')) {
        event.preventDefault(); 
        return; 
    }
});

$('#onglet4').on("click", function(event) {
    if ($(this).hasClass('active')) {
        event.preventDefault(); 
        return; 
    }
});

$('#onglet5').on("click", function(event) {
    if ($(this).hasClass('active')) {
        event.preventDefault(); 
        return; 
    }
});