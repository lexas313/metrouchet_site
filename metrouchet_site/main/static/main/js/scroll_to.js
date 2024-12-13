// Прокрутка до блока "Оформить заявку / order-service-form-block"
const headerHeight = document.querySelector('header').offsetHeight;

function scrollToOrderForm() {
    const orderForm = document.getElementById('order-service-form-block');
    const offset = orderForm.offsetTop - headerHeight;
    window.scrollTo({ top: offset, behavior: 'smooth' });
}