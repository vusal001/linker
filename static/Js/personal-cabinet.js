
// seting iconuna click zamani

function showCabinetBook(){
    let cabinetBookDropdown = document.querySelector(".cabinet-book-dropdown");
    cabinetBookDropdown.classList.toggle("cabinet-book-dropdown-active");
}


// pen e click zamani ad soyad yazma aktiv olmasi

function falseDisabled(e){
    e.parentElement.children[0].disabled = false;
    e.parentElement.children[0].focus();
    var val = e.parentElement.children[0].value; //store the value of the element
    e.parentElement.children[0].value = ''; //clear the value of the element
    e.parentElement.children[0].value = val;
    e.parentElement.children[2].style.display = "block";
}

function trueDisabled(e){
    e.parentElement.children[0].disabled = true;
    e.parentElement.children[2].style.display = "none";
}