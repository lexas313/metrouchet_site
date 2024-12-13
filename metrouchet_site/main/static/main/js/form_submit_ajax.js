// Отправка формы на заказ консультации
document.getElementById('callBackForm').addEventListener('submit', function(event) {
    event.preventDefault();  // Предотвращаем стандартную отправку формы

    var form = this;
    var formData = new FormData(form);  // Собираем данные формы

    // Отправляем данные формы через XHR
    var xhr = new XMLHttpRequest();
    xhr.open('POST', form.action, true);
    xhr.setRequestHeader('X-CSRFToken', '{{ csrf_token }}');  // Добавляем CSRF токен в заголовки

    xhr.onload = function() {
        var response = JSON.parse(xhr.responseText);  // Парсим JSON-ответ

        if (xhr.status >= 200 && xhr.status < 300) {
            // Успешная отправка формы
            if (response.success) {
                document.getElementById('form-message').innerHTML = '<p>' + response.message + '</p>';
                form.reset();  // Очищаем форму
                clearErrors();  // Очищаем сообщения об ошибках

                // Открываем popup
                openPopup();
            }
        } else if (xhr.status >= 400 && xhr.status < 500) {  // Обработка ошибок валидации
            clearErrors();  // Очищаем предыдущие ошибки

            // Проверяем, есть ли ошибки в ответе
            if (response.errors) {
                var errors = response.errors;
                for (var field in errors) {
                    if (errors.hasOwnProperty(field)) {
                        var errorMessage = errors[field][0]['message'];
                        var fieldElement = form.querySelector('[name=' + field + ']');
                        if (fieldElement) {
                            var errorElement = document.createElement('div');
                            errorElement.classList.add('error-message');
                            errorElement.innerHTML = errorMessage;
                            fieldElement.parentNode.appendChild(errorElement);
                        }
                    }
                }
            } else {
                console.error('Ошибка при отправке формы: нет ошибок в ответе.');
            }
        } else {
            console.error('Ошибка при отправке формы: ' + xhr.status);
        }
    };

    xhr.onerror = function() {
        console.error('Ошибка при попытке соединения с сервером.');
    };

    xhr.send(formData);
});


// Отправка формы на заказ услуги
document.getElementById('orderServiceForm').addEventListener('submit', function(event) {
    event.preventDefault();  // Предотвращаем стандартную отправку формы

    var form = this;
    var formData = new FormData(form);  // Собираем данные формы

    // Отправляем данные формы через XHR
    var xhr = new XMLHttpRequest();
    xhr.open('POST', form.action, true);
    xhr.setRequestHeader('X-CSRFToken', '{{ csrf_token }}');  // Добавляем CSRF токен в заголовки

    xhr.onload = function() {
        var response = JSON.parse(xhr.responseText);  // Парсим JSON-ответ

        if (xhr.status >= 200 && xhr.status < 300) {
            // Успешная отправка формы
            if (response.success) {
                document.getElementById('form-message').innerHTML = '<p>' + response.message + '</p>';
                form.reset();  // Очищаем форму
                clearErrors();  // Очищаем сообщения об ошибках

                // Открываем popup
                openPopup();
            }
        } else if (xhr.status >= 400 && xhr.status < 500) {  // Обработка ошибок валидации
            clearErrors();  // Очищаем предыдущие ошибки

            // Проверяем, есть ли ошибки в ответе
            if (response.errors) {
                var errors = response.errors;
                for (var field in errors) {
                    if (errors.hasOwnProperty(field)) {
                        var errorMessage = errors[field][0]['message'];
                        var fieldElement = form.querySelector('[name=' + field + ']');
                        if (fieldElement) {
                            var errorElement = document.createElement('div');
                            errorElement.classList.add('error-message');
                            errorElement.innerHTML = errorMessage;
                            fieldElement.parentNode.appendChild(errorElement);
                        }
                    }
                }
            } else {
                console.error('Ошибка при отправке формы: нет ошибок в ответе.');
            }
        } else {
            console.error('Ошибка при отправке формы: ' + xhr.status);
        }
    };

    xhr.onerror = function() {
        console.error('Ошибка при попытке соединения с сервером.');
    };

    xhr.send(formData);
});


// Функция для очистки сообщений об ошибках
function clearErrors() {
    var errorMessages = document.querySelectorAll('.error-message');
    errorMessages.forEach(function(message) {
        message.remove();
    });
}