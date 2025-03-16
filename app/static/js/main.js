document.addEventListener('DOMContentLoaded', function() {
    // Préchargeur
    const pageLoader = document.getElementById('page-loader');
    window.addEventListener('load', function() {
        pageLoader.style.opacity = '0';
        setTimeout(() => {
            pageLoader.style.display = 'none';
        }, 500);
    });

    // Curseur personnalisé
    const customCursor = document.getElementById('custom-cursor');
    const links = document.querySelectorAll('a, button');
    
    // Vérifier si le navigateur prend en charge les préférences de mouvement réduit
    const prefersReducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
    
    if (!prefersReducedMotion && window.innerWidth > 768) {
        document.addEventListener('mousemove', (e) => {
            customCursor.style.left = e.clientX + 'px';
            customCursor.style.top = e.clientY + 'px';
        });
        
        links.forEach(link => {
            link.addEventListener('mouseenter', () => {
                customCursor.style.transform = 'translate(-50%, -50%) scale(1.5)';
                customCursor.style.backgroundColor = 'rgba(59, 130, 246, 0.3)';
            });
            
            link.addEventListener('mouseleave', () => {
                customCursor.style.transform = 'translate(-50%, -50%) scale(1)';
                customCursor.style.backgroundColor = 'rgba(59, 130, 246, 0.5)';
            });
        });
    } else {
        // Désactiver le curseur personnalisé si l'utilisateur préfère les mouvements réduits
        customCursor.style.display = 'none';
    }
    
    // Bouton de retour en haut
    const backToTopButton = document.getElementById('back-to-top');
    
    window.addEventListener('scroll', () => {
        if (window.scrollY > 300) {
            backToTopButton.classList.remove('opacity-0', 'invisible');
            backToTopButton.classList.add('opacity-100', 'visible');
        } else {
            backToTopButton.classList.add('opacity-0', 'invisible');
            backToTopButton.classList.remove('opacity-100', 'visible');
        }
    });
    
    backToTopButton.addEventListener('click', () => {
        window.scrollTo({
            top: 0,
            behavior: prefersReducedMotion ? 'auto' : 'smooth'
        });
    });

    // Toggle menu mobile avec animation
    const mobileMenuButton = document.getElementById('mobile-menu-button');
    const mobileMenu = document.getElementById('mobile-menu');

    mobileMenuButton.addEventListener('click', function() {
        const isExpanded = mobileMenu.classList.contains('hidden') ? false : true;
        mobileMenuButton.setAttribute('aria-expanded', !isExpanded);
        
        mobileMenu.classList.toggle('hidden');
        if (!mobileMenu.classList.contains('hidden')) {
            mobileMenu.style.maxHeight = mobileMenu.scrollHeight + "px";
        } else {
            mobileMenu.style.maxHeight = "0";
        }
    });

    // Animation au scroll améliorée
    const observerOptions = {
        root: null,
        threshold: 0.1,
        rootMargin: '0px'
    };

    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                // Ajoute un délai basé sur l'index de l'élément
                const delay = entry.target.dataset.delay || '0';
                entry.target.style.transitionDelay = `${delay}ms`;
                entry.target.classList.add('opacity-100', 'translate-y-0');
                entry.target.classList.remove('opacity-0', 'translate-y-10');
            }
        });
    }, observerOptions);

    // Animation des compétences
    const animateSkills = () => {
        document.querySelectorAll('.skill-bar').forEach((bar, index) => {
            const percentage = bar.dataset.percentage;
            setTimeout(() => {
                bar.style.width = percentage;
            }, index * 200);
        });
    };

    // Animation des statistiques
    const animateStats = () => {
        document.querySelectorAll('.stat-number').forEach((stat) => {
            const target = parseInt(stat.dataset.target);
            let current = 0;
            const increment = target / 50;
            const timer = setInterval(() => {
                current += increment;
                if (current >= target) {
                    clearInterval(timer);
                    current = target;
                }
                stat.textContent = Math.round(current);
            }, 40);
        });
    };

    // Observer pour les animations au scroll
    if (!prefersReducedMotion) {
        document.querySelectorAll('.animate-on-scroll').forEach((elem, index) => {
            elem.dataset.delay = index * 100;
            elem.classList.add('opacity-0', 'translate-y-10', 'transition-all', 'duration-700');
            observer.observe(elem);
        });
    } else {
        // Si l'utilisateur préfère les mouvements réduits, afficher directement les éléments
        document.querySelectorAll('.animate-on-scroll').forEach((elem) => {
            elem.classList.add('opacity-100');
        });
    }

    // Mode sombre amélioré
    const darkModeToggle = document.createElement('button');
    darkModeToggle.innerHTML = '<i class="fas fa-moon"></i>';
    darkModeToggle.className = 'fixed bottom-4 right-4 p-3 rounded-full bg-white/80 dark:bg-gray-800/80 shadow-lg backdrop-blur-sm text-gray-800 dark:text-white hover:bg-gray-100 dark:hover:bg-gray-700 transition-all duration-300 transform hover:scale-110 z-50 no-print';
    darkModeToggle.setAttribute('aria-label', 'Basculer le mode sombre');
    
    document.body.appendChild(darkModeToggle);

    // Vérifier le mode préféré de l'utilisateur
    if (localStorage.getItem('darkMode') === 'true' || 
        (localStorage.getItem('darkMode') === null && 
         window.matchMedia('(prefers-color-scheme: dark)').matches)) {
        document.documentElement.classList.add('dark');
        darkModeToggle.innerHTML = '<i class="fas fa-sun"></i>';
    }

    darkModeToggle.addEventListener('click', () => {
        document.documentElement.classList.toggle('dark');
        const isDark = document.documentElement.classList.contains('dark');
        darkModeToggle.innerHTML = isDark ? '<i class="fas fa-sun"></i>' : '<i class="fas fa-moon"></i>';
        
        // Sauvegarder la préférence
        localStorage.setItem('darkMode', isDark);
        
        // Animation de rotation
        if (!prefersReducedMotion) {
            darkModeToggle.classList.add('rotate-180');
            setTimeout(() => darkModeToggle.classList.remove('rotate-180'), 300);
        }
    });

    // Initialisation des animations
    animateSkills();
    animateStats();

    // Animation des badges technologiques
    if (!prefersReducedMotion) {
        const techBadges = document.querySelectorAll('.tech-badge');
        techBadges.forEach((badge, index) => {
            badge.style.animationDelay = `${index * 200}ms`;
            badge.classList.add('animate-fade-in');
        });
    }
    
    // Animation des cartes de projet
    document.querySelectorAll('.project-card').forEach(card => {
        card.classList.add('card-hover');
    });
    
    // Effet de parallaxe pour les images d'arrière-plan
    if (!prefersReducedMotion && window.innerWidth > 768) {
        document.addEventListener('mousemove', (e) => {
            const parallaxElements = document.querySelectorAll('.parallax');
            const mouseX = e.clientX / window.innerWidth - 0.5;
            const mouseY = e.clientY / window.innerHeight - 0.5;
            
            parallaxElements.forEach(el => {
                const speed = el.dataset.speed || 20;
                const x = mouseX * speed;
                const y = mouseY * speed;
                el.style.transform = `translate(${x}px, ${y}px)`;
            });
        });
    }
    
    // Fonctionnalité d'impression
    const printButton = document.getElementById('print-button');
    const mobilePrintButton = document.getElementById('mobile-print-button');
    
    if (printButton) {
        printButton.addEventListener('click', () => {
            window.print();
        });
    }
    
    if (mobilePrintButton) {
        mobilePrintButton.addEventListener('click', () => {
            window.print();
        });
    }
    
    // Panneau d'accessibilité
    const accessibilityToggle = document.getElementById('accessibility-toggle');
    const accessibilityOptions = document.getElementById('accessibility-options');
    const fontSizeSelect = document.getElementById('font-size');
    const highContrastCheckbox = document.getElementById('high-contrast');
    const reduceMotionCheckbox = document.getElementById('reduce-motion');
    
    // Charger les préférences d'accessibilité
    if (localStorage.getItem('fontSize')) {
        const savedFontSize = localStorage.getItem('fontSize');
        document.documentElement.style.fontSize = savedFontSize;
        fontSizeSelect.value = savedFontSize === '1rem' ? 'normal' : savedFontSize === '1.25rem' ? 'large' : 'x-large';
    }
    
    if (localStorage.getItem('highContrast') === 'true') {
        document.documentElement.classList.add('high-contrast');
        highContrastCheckbox.checked = true;
    }
    
    if (localStorage.getItem('reduceMotion') === 'true' || prefersReducedMotion) {
        document.documentElement.classList.add('reduce-motion');
        reduceMotionCheckbox.checked = true;
    }
    
    // Toggle du panneau d'accessibilité
    accessibilityToggle.addEventListener('click', () => {
        const isExpanded = accessibilityOptions.classList.contains('hidden') ? false : true;
        accessibilityToggle.setAttribute('aria-expanded', !isExpanded);
        accessibilityOptions.classList.toggle('hidden');
    });
    
    // Changer la taille de la police
    fontSizeSelect.addEventListener('change', (e) => {
        const fontSize = e.target.value === 'normal' ? '1rem' : e.target.value === 'large' ? '1.25rem' : '1.5rem';
        document.documentElement.style.fontSize = fontSize;
        localStorage.setItem('fontSize', fontSize);
    });
    
    // Activer/désactiver le contraste élevé
    highContrastCheckbox.addEventListener('change', (e) => {
        if (e.target.checked) {
            document.documentElement.classList.add('high-contrast');
            localStorage.setItem('highContrast', 'true');
        } else {
            document.documentElement.classList.remove('high-contrast');
            localStorage.setItem('highContrast', 'false');
        }
    });
    
    // Activer/désactiver la réduction des animations
    reduceMotionCheckbox.addEventListener('change', (e) => {
        if (e.target.checked) {
            document.documentElement.classList.add('reduce-motion');
            localStorage.setItem('reduceMotion', 'true');
        } else {
            document.documentElement.classList.remove('reduce-motion');
            localStorage.setItem('reduceMotion', 'false');
        }
        
        // Recharger la page pour appliquer les changements
        window.location.reload();
    });
    
    // Ajouter des raccourcis clavier pour l'accessibilité
    document.addEventListener('keydown', (e) => {
        // Alt+A pour ouvrir le panneau d'accessibilité
        if (e.altKey && e.key === 'a') {
            accessibilityOptions.classList.toggle('hidden');
            accessibilityToggle.setAttribute('aria-expanded', !accessibilityOptions.classList.contains('hidden'));
        }
        
        // Alt+D pour basculer le mode sombre
        if (e.altKey && e.key === 'd') {
            darkModeToggle.click();
        }
        
        // Alt+P pour imprimer
        if (e.altKey && e.key === 'p') {
            window.print();
        }
    });
}); 