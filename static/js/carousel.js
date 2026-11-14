// // Drop lateral
const imagens = document.querySelectorAll('img');
const lightbox = document.getElementById('lightbox');
const lightboxImg = document.getElementById('lightbox-img');

imagens.forEach(img => {
  img.addEventListener('click', () => {
    lightboxImg.src = img.src;
    lightbox.style.display = 'flex'; // mostra no centro
  });
});

lightbox.addEventListener('click', () => {
  lightbox.style.display = 'none'; // fecha ao clicar fora
});

