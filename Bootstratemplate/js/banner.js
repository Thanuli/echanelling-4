const slides = document.querySelectorAll('.carousel-slide');

let currentIndex = 0;

function showSlide(index) {
  slides.forEach((slide, i) => {
    if (i === index) {
      slide.style.display = 'block';
    } else {
      slide.style.display = 'none';
    }
  }
  );
}

function nextSlide() {
  currentIndex = (currentIndex + 1) % slides.length;
  showSlide(currentIndex);
}

function startCarousel() {
  setInterval(nextSlide, 2000); // Change slide every 2 seconds
}

// Initialize the carousel
showSlide(currentIndex);
startCarousel();
