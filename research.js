
document.addEventListener('DOMContentLoaded', async () => {
    const track = document.getElementById('research-carousel');
    const prevBtn = document.getElementById('research-prev');
    const nextBtn = document.getElementById('research-next');
    const indicators = document.getElementById('carousel-indicators');

    if (!track) return;

    let posts = [];
    let currentIndex = 0;

    // Fetch posts from data/processed_posts.json
    try {
        const response = await fetch('data/processed_posts.json');
        if (!response.ok) throw new Error('Failed to load posts');
        posts = await response.json();

        // Take latest 6 posts
        posts = posts.slice(0, 6);

        renderCarousel();
        window.addEventListener('resize', updateCarousel);
    } catch (error) {
        console.error('Error loading research posts:', error);
        track.innerHTML = '<div class="loader">Unable to load insights.</div>';
    }


    function renderCarousel() {
        if (posts.length === 0) return;

        // Render cards
        track.innerHTML = posts.map((post, index) => {
            const primaryTag = post.tags && post.tags.length > 0 ? post.tags[0] : 'Insight';

            // Determine action text (Read More, Listen, View)
            let actionText = 'Read More';
            if (post.tags && post.tags.some(t => t.toLowerCase().includes('podcast'))) {
                actionText = 'Listen';
            } else if (post.tags && post.tags.some(t => t.toLowerCase().includes('video'))) {
                actionText = 'Watch';
            }

            return `
                <div class="research-card">
                    <div class="research-card-accent accent-yellow">
                        <span>${primaryTag}</span>
                        <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                            <line x1="7" y1="17" x2="17" y2="7"></line>
                            <polyline points="7 7 17 7 17 17"></polyline>
                        </svg>
                    </div>
                    <div class="research-card-body">
                        <h3 class="research-card-title">${post.title}</h3>
                        <div class="research-card-footer">
                            <span class="research-date">${formatDate(post.date)}</span>
                            <a href="article.html?slug=${post.slug}" class="research-read-more">
                                ${actionText}
                                <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                                    <line x1="7" y1="17" x2="17" y2="7"></line>
                                    <polyline points="7 7 17 7 17 17"></polyline>
                                </svg>
                            </a>
                        </div>
                    </div>
                    <img src="${post.image}" alt="${post.title}" class="research-card-bg">
                </div>
            `;
        }).join('');

        // Render indicators
        indicators.innerHTML = posts.map((_, index) =>
            `<div class="indicator-dot ${index === 0 ? 'active' : ''}" data-index="${index}"></div>`
        ).join('');

        // Add events to indicators
        document.querySelectorAll('.indicator-dot').forEach(dot => {
            dot.addEventListener('click', () => {
                const index = parseInt(dot.dataset.index);
                goToSlide(index);
            });
        });

        updateCarousel();
    }

    function formatDate(dateStr) {
        const options = { year: 'numeric', month: 'long', day: 'numeric' };
        return new Date(dateStr).toLocaleDateString('en-US', options).toUpperCase();
    }

    function updateCarousel() {
        if (posts.length === 0) return;

        const cardWidth = track.querySelector('.research-card').offsetWidth;
        const gap = parseInt(window.getComputedStyle(track).gap) || 0;
        const offset = currentIndex * (cardWidth + gap);

        track.style.transform = `translateX(-${offset}px)`;

        // Update indicators
        document.querySelectorAll('.indicator-dot').forEach((dot, index) => {
            dot.classList.toggle('active', index === currentIndex);
        });

        // Update buttons
        prevBtn.disabled = currentIndex === 0;
        nextBtn.disabled = currentIndex === posts.length - 1;
    }

    function goToSlide(index) {
        currentIndex = index;
        updateCarousel();
    }

    prevBtn.addEventListener('click', () => {
        if (currentIndex > 0) {
            currentIndex--;
            updateCarousel();
        }
    });

    nextBtn.addEventListener('click', () => {
        if (currentIndex < posts.length - 1) {
            currentIndex++;
            updateCarousel();
        }
    });

    // Handle touch/swipe for mobile
    let startX = 0;
    let isDragging = false;

    track.addEventListener('touchstart', e => {
        startX = e.touches[0].clientX;
        isDragging = true;
    });

    track.addEventListener('touchmove', e => {
        if (!isDragging) return;
        const x = e.touches[0].clientX;
        const diff = startX - x;
        if (Math.abs(diff) > 50) {
            if (diff > 0 && currentIndex < posts.length - 1) {
                currentIndex++;
                updateCarousel();
            } else if (diff < 0 && currentIndex > 0) {
                currentIndex--;
                updateCarousel();
            }
            isDragging = false;
        }
    });

    track.addEventListener('touchend', () => {
        isDragging = false;
    });
});
