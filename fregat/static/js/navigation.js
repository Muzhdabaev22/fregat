window.onscroll = function() {
    scrollFunction()
};

function scrollFunction() {
    if (document.body.scrollTop > 100 || document.documentElement.scrollTop > 100) {
        document.querySelector(".container-nav").classList.add("scroll");
    } else {
        document.querySelector(".container-nav").classList.remove("scroll");
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
