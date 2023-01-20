function myFunction(id) {
    var dots = document.getElementById("dots-"+id);
    var moreText = document.getElementById("more-"+id);
    var btnText = document.getElementById("myBtn-"+id);

    if (dots.style.display === "none") {
        dots.style.display = "inline";
        btnText.innerHTML = "Read more"; 
        moreText.style.display = "none";
    } else {
        dots.style.display = "none";
        btnText.innerHTML = "Read less"; 
        moreText.style.display = "inline";
    }
}

const hamburger = document.querySelector('.hamburger');
const navLinks = document.querySelector('.top-nav-links');

hamburger.addEventListener('mouseover', () => {
    navLinks.classList.add('show-nav');
});

navLinks.addEventListener('mouseleave', () => {
    navLinks.classList.remove('show-nav');
});
