// Toggle navbar links on small screens
document.querySelector('.navbar h1').addEventListener('click', function () {
    document.querySelector('.navbar-links').classList.toggle('show');
});

// Initialize AOS
AOS.init({
    duration: 1000,  // Adjust this value (default is 300)
    offset: 150,    // Adjust this value (default is 120)
});

// Initialize Typed.js
var typed = new Typed('#typed-text', {
    strings: ['Hello, I\'m Bizay Karki'],
    typeSpeed: 200,
    backSpeed: 100,
    startDelay: 500,
    backDelay: 500,
    showCursor: true,
    cursorChar: '|',
    loop: false
});
