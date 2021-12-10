//  ureye click zamani iconun deyishmesi

function changeFavorite(e){
    if(e.getAttribute("src") == "../Icons/favorite_border.svg") e.setAttribute("src","../Icons/favorite.svg");
    else e.setAttribute("src","../Icons/favorite_border.svg");
}