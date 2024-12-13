// Маска для телефонных номеров
document.addEventListener("DOMContentLoaded", function() {
    // Выбираем все элементы с name="phone_number"
    const elements = document.querySelectorAll('input[name="phone_number"]');
    const maskOptions = {
        mask: '+{7} (000) 000-00-00'
    };

    // Применяем маску ко всем элементам
    elements.forEach(function(element) {
        IMask(element, maskOptions);
    });
});