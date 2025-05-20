'use strict';

const switcher = document.querySelector('.btn');

if (switcher) {
    switcher.addEventListener('click', () => {
        // Verifica se o body já tem 'dark-theme'
        if (document.body.classList.contains('dark-theme')) {
            document.body.classList.remove('dark-theme');
            document.body.classList.add('light-theme');
            switcher.textContent = 'Dark'; // Botão muda para Dark
        } else {
            document.body.classList.remove('light-theme');
            document.body.classList.add('dark-theme');
            switcher.textContent = 'Light'; // Botão muda para Light
        }
    });
}
