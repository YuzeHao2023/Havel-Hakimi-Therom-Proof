// Language switching functionality
(function() {
    // Default language is Chinese
    let currentLanguage = localStorage.getItem('selectedLanguage') || 'cn';

    // Initialize on page load
    function init() {
        setLanguage(currentLanguage);
        setupLanguageButtons();
    }

    // Setup language switching buttons
    function setupLanguageButtons() {
        const buttons = document.querySelectorAll('.lang-btn');
        buttons.forEach(btn => {
            btn.addEventListener('click', function() {
                const lang = this.getAttribute('data-lang');
                setLanguage(lang);
                localStorage.setItem('selectedLanguage', lang);
            });
        });
    }

    // Set the language for the entire page
    function setLanguage(lang) {
        currentLanguage = lang;

        // Update active button
        const buttons = document.querySelectorAll('.lang-btn');
        buttons.forEach(btn => {
            btn.classList.remove('active');
            if (btn.getAttribute('data-lang') === lang) {
                btn.classList.add('active');
            }
        });

        // Update page language
        document.documentElement.lang = lang === 'en' ? 'en' : 'zh-CN';

        // Update all translatable elements
        const elements = document.querySelectorAll('[data-cn][data-en]');
        elements.forEach(el => {
            if (lang === 'en') {
                el.textContent = el.getAttribute('data-en');
            } else {
                el.textContent = el.getAttribute('data-cn');
            }
        });

        // Update all link elements
        const links = document.querySelectorAll('a[data-cn][data-en]');
        links.forEach(link => {
            if (lang === 'en') {
                link.textContent = link.getAttribute('data-en');
            } else {
                link.textContent = link.getAttribute('data-cn');
            }
        });

        // Update button text
        const btnTexts = document.querySelectorAll('.btn-text');
        btnTexts.forEach(btn => {
            const cnText = btn.getAttribute('data-cn');
            const enText = btn.getAttribute('data-en');
            if (lang === 'en' && enText) {
                btn.textContent = enText;
            } else if (cnText) {
                btn.textContent = cnText;
            }
        });

        // Trigger MathJax to re-render formulas
        if (window.MathJax && window.MathJax.typeset) {
            setTimeout(() => {
                MathJax.typeset();
            }, 100);
        }

        // Update game status messages
        updateGameStatusMessages(lang);
    }

    // Update game status messages based on language
    function updateGameStatusMessages(lang) {
        const gameStatus = document.getElementById('game-status');
        if (gameStatus && gameStatus.classList.contains('success')) {
            if (lang === 'en') {
                gameStatus.textContent = '🎉 Congratulations! You successfully constructed the graph matching the degree sequence!';
            } else {
                gameStatus.textContent = '🎉 太棒了！你成功构造了满足度序列的图！';
            }
        }
    }

    // Expose getCurrentLanguage function to game.js
    window.getCurrentLanguage = function() {
        return currentLanguage;
    };

    // Initialize when DOM is ready
    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', init);
    } else {
        init();
    }
})();
