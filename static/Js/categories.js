

// categories list items add start
// NOT sen sadece bura hansi kateqoriyalar var yazarsan kod ozu html e yerleshdirecek 

// let categories = [
//     "Hamısı",
//     "Klassik",
//     "Dedektiv",
//     "Psixologiya",
//     "Tarix",
//     "Hüquq",
//     "Bioqrafiya",
//     "Dərslikər/Testlər",
//     "Şəxsi İnkişaf",
//     "Digər",
//     "Bədii Ədəbiyyat",
//     "Uşaq ədəbiyyatı"
// ]


// function myFunction(){
//     let screenWidth = window.innerWidth;
//     let categoriesList = document.querySelector("#categories .categories ul");
//     categoriesMenu = document.querySelector("#categories .categories-menu");

//     if(screenWidth < 576){
//         categoriesMenu.innerHTML = " ";
//         categoriesList.innerHTML = " ";
//         for(let i = 0;i < categories.length;i++){
//             if(i < 5)
//                 categoriesList.innerHTML += "<li>"+ categories[i] +"</li>";
//             else{
//                 categoriesMenu.innerHTML += "<li class='list-group-item list-group-item-action cursor-pointer'>"+ categories[i] +"</li>";
//             }
//         }
//     }
//     else if(screenWidth < 768){
//         categoriesMenu.innerHTML = " ";
//         categoriesList.innerHTML = " ";
//         for(let i = 0;i < categories.length;i++){
//             if(i < 7)
//                 categoriesList.innerHTML += "<li>"+ categories[i] +"</li>";
//             else{
//                 categoriesMenu.innerHTML += "<li class='list-group-item list-group-item-action cursor-pointer'>"+ categories[i] +"</li>";
//             }
//         }
//     }
//     else{
//         categoriesMenu.innerHTML = " ";
//         categoriesList.innerHTML = " ";
//         for(let i = 0;i < categories.length;i++){
//             if(i < 10)
//                 categoriesList.innerHTML += "<li>"+ categories[i] +"</li>";
//             else{
//                 categoriesMenu.innerHTML += "<li class='list-group-item list-group-item-action cursor-pointer'>"+ categories[i] +"</li>";
//             }
//         }
//     }
// }

// window.onresize = myFunction;

// window.onload = function(){
//     myFunction();
//     // // material icons problem solution
//     // mI = document.querySelectorAll('.material-icons');
//     // for(let j = 0;j< mI.length;j++)
//     //     mI[j].style.opacity = "1";
// }

// // end

// // categories menu show hidden
// categoriesMenu = document.querySelector("#categories .categories-menu");
// function showCategoriesMenu(){
//     console.log(categoriesMenu)
//     categoriesMenu.classList.toggle("active-menu");
// }


// categoriya lefte click zamani 

function categoriyaScrollLeft(){
    let categoriesList = document.querySelector("#categories .categories .categories-list");
    categoriesList.scrollLeft -= 350;
}

// categoriya righta click zamani 

function categoriyaScrollRight(){
    let categoriesList = document.querySelector("#categories .categories .categories-list");
    categoriesList.scrollLeft += 350;
}




