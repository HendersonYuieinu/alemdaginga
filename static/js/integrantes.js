document.addEventListener('DOMContentLoaded', () => {
      const cards = document.querySelectorAll('.integrante-card');
      const modal = document.getElementById('bioModal');
      const btnClose = document.querySelector('.modal-close');
      
      const modalImg = document.getElementById('modalImg');
      const modalName = document.getElementById('modalName');
      const modalGraduacao = document.getElementById('modalGraduacao');
      const modalBio = document.getElementById('modalBio');
      const modalSocials = document.getElementById('modalSocials');

      cards.forEach(card => {
        card.addEventListener('click', () => {
          // Extrair informações do card clicado
          const imgElement = card.querySelector('img');
          const name = card.querySelector('h4').innerText;
          const grad = card.querySelector('.graduacao') ? card.querySelector('.graduacao').innerText : '';
          const fullBio = card.getAttribute('data-bio') || "Biografia não disponível no momento.";
          const socialsHTML = card.querySelector('.integrante-sociais').innerHTML;

          // Preencher o modal com os dados
          modalImg.src = imgElement.src;
          // Copia as classes da imagem (como a borda verde do mestre) para o modal
          modalImg.className = imgElement.className; 
          
          modalName.innerText = name;
          modalGraduacao.innerText = grad;
          modalBio.innerText = fullBio;
          modalSocials.innerHTML = socialsHTML;

          // Exibir modal
          modal.classList.add('ativo');
          document.body.style.overflow = 'hidden'; // Impede rolagem do fundo
        });
      });

      // Função para fechar o modal
      const fecharModal = () => {
        modal.classList.remove('ativo');
        document.body.style.overflow = ''; // Restaura rolagem
      };

      // Fechar no clique do botão (X)
      btnClose.addEventListener('click', fecharModal);

      // Fechar clicando fora da caixa de conteúdo (no fundo escuro)
      modal.addEventListener('click', (e) => {
        if (e.target === modal) fecharModal();
      });

      // Fechar apertando a tecla ESC
      document.addEventListener('keydown', (e) => {
        if (e.key === 'Escape' && modal.classList.contains('ativo')) {
          fecharModal();
        }
      });
    });