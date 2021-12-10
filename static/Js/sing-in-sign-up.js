
//  goz isharesine click zamani parolun gorunmesi

function showPassword(e){
    let eAttr = e.getAttribute("src");
    if(eAttr == "../Icons/invisible.svg"){
        e.setAttribute("src","../Icons/visibility.svg");
        e.parentElement.children[0].setAttribute("type","text");
    }
    else{
        e.setAttribute("src","../Icons/invisible.svg");
        e.parentElement.children[0].setAttribute("type","password");
    }
}
