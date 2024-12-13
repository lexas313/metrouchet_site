// Функция для открытия popup
function openPopup() {
    var popup = document.getElementById('form-popup');
    popup.style.display = "block";
}

// Функция для закрытия popup
function closePopup() {
    var popup = document.getElementById('form-popup');
    popup.style.display = "none";
}

// Закрытие popup при нажатии на крестик
document.querySelector('.close-popup').addEventListener('click', function() {
    closePopup();
});

// Закрытие popup при клике вне его
window.onclick = function(event) {
    var popup = document.getElementById('form-popup');
    if (event.target == popup) {
        closePopup();
    }
}







// Получаем элементы модального окна и изображения
var modal = document.getElementById("imageModal");
var img = document.querySelector(".accreditation-image");
var modalImg = document.getElementById("modalImage");
var span = document.getElementsByClassName("close")[0];

// При клике на изображение открываем модальное окно
img.onclick = function() {
    modal.style.display = "block";
    modalImg.src = this.src; // Устанавливаем источник изображения в модальном окне
}

// При клике на "x" закрываем модальное окно
span.onclick = function() {
    modal.style.display = "none";
}

// Закрытие модального окна при клике вне изображения
window.onclick = function(event) {
    if (event.target == modal) {
        modal.style.display = "none";
    }
}




//// Получаем элементы модального окна для изображения
//var imageModal = document.getElementById("imageModal");
//var imageSpan = imageModal.getElementsByClassName("close")[0];
//
//// Получаем элементы модального окна для заказа
//var orderModal = document.getElementById("orderModal");
//var orderSpan = orderModal.getElementsByClassName("close")[0];
//
//// При клике на изображение открываем модальное окно с изображением
//var image = document.querySelector(".accreditation-image");
//image.onclick = function() {
//    imageModal.style.display = "block";
//    var modalImg = document.getElementById("modalImage");
//    modalImg.src = this.src; // Устанавливаем источник изображения в модальном окне
//}
//
//// При клике на "x" закрываем модальное окно с изображением
//imageSpan.onclick = function() {
//    imageModal.style.display = "none";
//}
//
//// При клике на кнопку "Заказать" открываем модальное окно для заказа
//var orderButton = document.getElementById("orderButton");
//orderButton.onclick = function() {
//    orderModal.style.display = "block";
//}
//
//// При клике на "x" закрываем модальное окно для заказа
//orderSpan.onclick = function() {
//    orderModal.style.display = "none";
//}
//
//// Закрытие модального окна при клике вне изображения или формы заказа
//window.onclick = function(event) {
//    if (event.target === imageModal || event.target.className === 'close') {
//        imageModal.style.display = "none";
//    } else if (event.target === orderModal || event.target.className === 'close') {
//        orderModal.style.display = "none";
//    }
//}

