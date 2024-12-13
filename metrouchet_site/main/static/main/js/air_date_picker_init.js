// Инициализация Air Datepicker для поля с id "id_service_date"
new AirDatepicker('#id_service_date', {
    inline: true, // Календарь всегда отображается
    autoClose: true, // Закрывать календарь после выбора даты (по желанию)
    minDate: new Date(),
});


// Инициализация Air Datepicker для всех полей с name "service_date"
//document.querySelectorAll('input[name="service_date"]').forEach(function(element) {
//    new AirDatepicker(element, {
//        inline: true, // Календарь всегда отображается
//        autoClose: true, // Закрывать календарь после выбора даты (по желанию)
//        minDate: new Date(),
//    });
//});