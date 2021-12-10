
let packages = document.querySelectorAll(".package");

function selectedPackage1(e){
    packages[1].classList.remove("selected");
    e.classList.add("selected");
}

function selectedPackage2(e){
    e.classList.add("selected");
    packages[0].classList.remove("selected");
}

