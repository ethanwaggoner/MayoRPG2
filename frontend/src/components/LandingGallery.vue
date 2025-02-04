<script>
import Gallery1 from '@/assets/gallery1.png';
import Gallery2 from '@/assets/gallery2.png';
import Gallery3 from '@/assets/gallery3.png';

export default {
  name: 'Gallery',
  data() {
    return {
      images: [
        { id: 1, src: Gallery1, alt: 'Epic Battle', title: '' },
        { id: 2, src: Gallery2, alt: 'Mystic Forest', title: '' },
        { id: 3, src: Gallery3, alt: 'Dungeon Depths', title: '' },
      ],
    };
  },
};
</script>

<template>
  <section id="gallery" class="gallery-section">
    <div class="container">
      <h2 class="section-title">Gallery</h2>
      <div class="gallery-grid">
        <div
          class="gallery-card"
          v-for="image in images"
          :key="image.id"
        >
          <div class="image-container">
            <img :src="image.src" :alt="image.alt" class="gallery-image" />
            <div class="overlay">
              <span class="overlay-text">{{ image.title }}</span>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<style scoped>
.gallery-section {
  color: #f8facc;
  font-family: 'Press Start 2P', cursive;
  padding: 5rem 2rem;
  background: linear-gradient(135deg, #1a1a1a, #2c2c2c);
}

.container {
  max-width: 1200px;
  margin: 0 auto;
}

.section-title {
  font-size: 3rem;
  margin-bottom: 4rem;
  text-align: center;
  position: relative;
  display: inline-block;
}

.section-title::after {
  content: '';
  width: 60px;
  height: 4px;
  display: block;
  margin: 1rem auto 0;
  border-radius: 2px;
}

.gallery-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
  gap: 2.5rem;
  justify-items: center;
}

.gallery-card {
  background: rgba(255, 255, 255, 0.05);
  backdrop-filter: blur(10px);
  border-radius: 15px;
  padding: 1rem;
  position: relative;
  overflow: hidden;
  transition: transform 0.3s ease, box-shadow 0.3s ease;
}

.gallery-card::before {
  content: '';
  position: absolute;
  top: -50%;
  left: -50%;
  width: 200%;
  height: 200%;
  transform: rotate(45deg);
  transition: opacity 0.3s ease;
  opacity: 0;
}


.image-container {
  position: relative;
  border-radius: 12px;
  overflow: hidden;
}

.gallery-image {
  width: 100%;
  height: 200px;
  object-fit: cover;
  transition: transform 0.3s ease;
}

.gallery-card:hover .gallery-image {
  transform: scale(1.05);
}

.overlay {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  opacity: 0;
  display: flex;
  justify-content: center;
  align-items: center;
  transition: opacity 0.3s ease;
}

.gallery-card:hover .overlay {
  opacity: 1;
}

.overlay-text {
  color: #121212;
  font-size: 1.5rem;
  font-weight: bold;
  text-shadow: 0 2px 4px rgba(0, 0, 0, 0.5);
}

@media (max-width: 768px) {
  .section-title {
    font-size: 2.5rem;
  }

  .gallery-image {
    height: 150px;
  }

  .overlay-text {
    font-size: 1.2rem;
  }

  .gallery-card {
    padding: 0.8rem;
  }
}

@media (max-width: 480px) {
  .section-title {
    font-size: 2rem;
  }

  .gallery-grid {
    grid-template-columns: 1fr;
  }

  .gallery-image {
    height: 120px;
  }

  .overlay-text {
    font-size: 1rem;
  }
}
</style>