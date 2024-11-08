document.addEventListener('DOMContentLoaded', function() {
    // Toggle menu mobile avec animation
    const mobileMenuButton = document.getElementById('mobile-menu-button');
    const mobileMenu = document.getElementById('mobile-menu');

    mobileMenuButton.addEventListener('click', function() {
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
    document.querySelectorAll('.animate-on-scroll').forEach((elem, index) => {
        elem.dataset.delay = index * 100;
        elem.classList.add('opacity-0', 'translate-y-10', 'transition-all', 'duration-700');
        observer.observe(elem);
    });

    // Mode sombre amélioré
    const darkModeToggle = document.createElement('button');
    darkModeToggle.innerHTML = '<i class="fas fa-moon"></i>';
    darkModeToggle.className = 'fixed bottom-4 right-4 p-3 rounded-full bg-white/80 dark:bg-gray-800/80 shadow-lg backdrop-blur-sm text-gray-800 dark:text-white hover:bg-gray-100 dark:hover:bg-gray-700 transition-all duration-300 transform hover:scale-110';
    
    document.body.appendChild(darkModeToggle);

    darkModeToggle.addEventListener('click', () => {
        document.documentElement.classList.toggle('dark');
        const isDark = document.documentElement.classList.contains('dark');
        darkModeToggle.innerHTML = isDark ? '<i class="fas fa-sun"></i>' : '<i class="fas fa-moon"></i>';
        
        // Animation de rotation
        darkModeToggle.classList.add('rotate-180');
        setTimeout(() => darkModeToggle.classList.remove('rotate-180'), 300);
    });

    // Initialisation des animations
    animateSkills();
    animateStats();

    // Animation des badges technologiques
    const techBadges = document.querySelectorAll('.tech-badge');
    techBadges.forEach((badge, index) => {
        badge.style.animationDelay = `${index * 200}ms`;
        badge.classList.add('animate-fade-in');
    });
}); 