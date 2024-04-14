document.addEventListener("DOMContentLoaded", function() {
    // Esperar a que se cargue el contenido de la página
    var cards = document.querySelectorAll('.card');

    // Agregar clase 'animate' a cada tarjeta después de un breve retraso
    cards.forEach(function(card, index) {
        setTimeout(function() {
            card.classList.add('animate');
        }, index * 200); // Añadir un retraso creciente para cada tarjeta
    });
});
