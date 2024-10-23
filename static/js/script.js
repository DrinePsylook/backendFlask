$('#onglet1').on("click", function(event) {
    event.preventDefault();
    console.log('Onglet 1 cliqué');
    $('.active').removeClass('active'); //Si on a cliqué avant sur un autre onglet, on les enlève tous pour ne pas avoir à chercher lequel a la class "active"
    $(this).addClass('active');
});

$('#onglet2').on("click", function(event) {
    event.preventDefault();
    console.log('Onglet 2 cliqué');
    $('.active').removeClass('active');
    $(this).addClass('active');
});

$('#onglet3').on("click", function(event) {
    event.preventDefault();
    console.log('Onglet 3 cliqué');
    $('.active').removeClass('active');
    $(this).addClass('active');
});

$('#onglet4').on("click", function(event) {
    event.preventDefault();
    console.log('Onglet 4 cliqué');
    $('.active').removeClass('active');
    $(this).addClass('active');
});

$('#onglet5').on("click", function(event) {
    event.preventDefault();
    console.log('Onglet 5 cliqué');
    $('.active').removeClass('active');
    $(this).addClass('active');
});