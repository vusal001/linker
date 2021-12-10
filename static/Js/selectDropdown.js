
// drop downda click zamani drowdownun acilmasi
let lastClicked = "none";
function toggleElement(e){
    e.classList.toggle("active-dropdown");
}
// drop downda click zamani elementin secilmesi
function selectDropdownElement(e){  
    toggleElement(e.children[2]);
    selectElement(e.children[2].children);

    if(lastClicked != "none" && e.children[2] != lastClicked){
        lastClicked.classList.remove("active-dropdown");
    }
    lastClicked = e.children[2];
}


function selectElement(e){
    for(let i = 0;i < e.length; i++ ){
        e[i].onclick = function(){
            e[i].parentElement.parentElement.children[0].value = e[i].innerHTML;
        }
    }
}