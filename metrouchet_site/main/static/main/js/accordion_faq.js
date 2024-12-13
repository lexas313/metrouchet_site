// Аккордеон FAQ

const accordionContainers = document.querySelectorAll('.container');

accordionContainers.forEach((container) => {
  container.addEventListener('click', () => {
    container.classList.toggle('active');
    const content = container.querySelector('.content');
    if (container.classList.contains('active')) {
      content.style.height = content.scrollHeight + 'px';
    } else {
      content.style.height = '0px';
    }
  });
});