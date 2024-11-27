window.onscroll = function() {
    scrollFunction()
};

function scrollFunction() {
    let navElement = document.querySelector(".container-nav");

    if (document.body.scrollTop > 50 || document.documentElement.scrollTop > 50) {
        document.querySelector(".container-nav").classList.add("scroll");
    } else if (!navElement.classList.contains(".click-background")) {
        document.querySelector(".container-nav").classList.remove("scroll");
    }
}

function openbox() {

    let navElement = document.querySelector(".container-nav"); 
    let buttonElements = document.getElementsByClassName('button-nav-block'); 
    let navListElements = document.getElementsByClassName('nav-list');

    if (navElement.classList.contains("click-background")) {
        navElement.classList.remove("click-background");
        buttonElements[0].classList.remove("visible");
        buttonElements[1].classList.remove("visible");
        navListElements[0].classList.remove("visible");

    } else {
        navElement.classList.add("click-background");
        buttonElements[0].classList.add("visible");
        buttonElements[1].classList.add("visible");
        navListElements[0].classList.add("visible");
    }
}

var curpath = location.pathname.match(/^\/[^/]+/);
if (curpath === null) {
    document.getElementsByClassName('linehover1')[0].style.opacity = "1";
} else if (curpath[0] === "/lang") {
    document.getElementsByClassName('linehover2')[0].style.opacity = "1";
} else if (curpath[0] === "/cinema") {
    document.getElementsByClassName('linehover6')[0].style.opacity = "1";
} else if (curpath[0] === "/blog") {
    document.getElementsByClassName('linehover4')[0].style.opacity = "1";
}
