<!-- Horizontal scroll -->

const container = document.querySelector('.skills-container');
  container.addEventListener('wheel', (e) => {
    e.preventDefault();
    container.scrollLeft += e.deltaY * 3;
  });

  <!-- Scrolling by button -->

  document.querySelectorAll('.scroll-down-one-window').forEach(icon => {
  icon.addEventListener('click',() => {
    window.scrollBy({
        top: window.innerHeight,
        behavior: 'smooth'
    });
        });
            });

  <!-- Big scroll -->

  document.getElementById('scroll-down-to-tools').addEventListener('click', () => {
  window.scrollBy({
    top: window.innerHeight * 1.5,
    behavior: 'smooth'
  });
});

  <!-- Scroll to the end -->

document.querySelectorAll('.scroll-down-to-end').forEach(icon => {
      icon.addEventListener('click',() => {
        window.scrollBy({
            top: document.body.scrollHeight,
            behavior: 'smooth'
        });
      });
    });
