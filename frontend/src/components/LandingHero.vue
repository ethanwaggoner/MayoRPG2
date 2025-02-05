<script>
import { onMounted, ref } from 'vue';
import { gsap } from 'gsap';

export default {
  name: 'Hero',
  setup() {
    const title = ref(null);
    const description = ref(null);
    const button = ref(null);

    onMounted(() => {
      gsap.from(title.value, { y: -50, opacity: 0, duration: 1, ease: 'power3.out' });
      gsap.from(description.value, { y: 50, opacity: 0, duration: 1, delay: 0.5, ease: 'power3.out' });
    });

    const scrollToFeatures = () => {
      const features = document.getElementById('features');
      if (features) {
        features.scrollIntoView({ behavior: 'smooth' });
      }
    };

    return { title, description, button, scrollToFeatures };
  },
};
</script>

<template>
  <section id="hero" class="hero-section">
    <div class="hero-overlay"></div>
    <div class="hero-content">
      <h1 ref="title" class="hero-title">Welcome to MayoRPG</h1>
      <p ref="description" class="hero-description">
        Embark on an epic pixelated adventure.
      </p>
      <router-link to="/login">
        <button ref="button" class="play-now-button">
          Play Now
        </button>
      </router-link>
    </div>
    <div class="animated-background">
      <span class="circle"></span>
      <span class="circle"></span>
      <span class="circle"></span>
    </div>
  </section>
</template>

<style scoped>
.hero-section {
  position: relative;
  min-height: 100vh;
  background-image: url("@/assets/backgrounds/StartBackground.gif");
  background-size: cover;
  background-position: center;
  background-repeat: no-repeat;
  display: flex;
  align-items: center;
  justify-content: center;
  overflow: hidden;
  color: #f8facc;
  font-family: 'Press Start 2P', cursive;
}

.hero-overlay {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: rgba(18, 18, 18, 0.85);
  backdrop-filter: blur(5px);
  z-index: 1;
}

.hero-content {
  position: relative;
  z-index: 2;
  text-align: center;
  padding: 0 1rem;
  color: #ffffff;
}

.hero-title {
  font-size: 4rem;
  margin-bottom: 1rem;
  color: #ffffff;
  text-shadow: 0 4px 10px rgba(0, 0, 0, 0.7);
}

.hero-description {
  font-size: 1.5rem;
  margin-bottom: 3rem;
  color: #d1d5db;
  max-width: 700px;
  margin-left: auto;
  margin-right: auto;
  text-shadow: 0 2px 5px rgba(0, 0, 0, 0.5);
}

.play-now-button {
  position: relative;
  background-color: #f59e0b;
  color: #121212;
  padding: 0.75rem 2.5rem;
  border: none;
  border-radius: 50px;
  font-size: 1.25rem;
  font-weight: bold;
  cursor: pointer;
  transition: all 0.3s ease;
  box-shadow: 0 0 20px rgba(245, 158, 11, 0.6);
  overflow: hidden;
  z-index: 2;
  animation: pulse 2s infinite;
}

.play-now-button::before {
  content: '';
  position: absolute;
  top: 50%;
  left: -75%;
  width: 150%;
  height: 300%;
  background: rgba(255, 255, 255, 0.2);
  transform: rotate(45deg) translate(-50%, -50%);
  transition: all 0.5s ease;
}

.play-now-button:hover::before {
  left: 125%;
}

.play-now-button:hover {
  background-color: #eab308;
  transform: scale(1.05);
}

.play-now-button:focus {
  outline: none;
  box-shadow: 0 0 25px rgba(245, 158, 11, 0.8);
}

@keyframes pulse {
  0% {
    box-shadow: 0 0 10px rgba(245, 158, 11, 0.6);
  }
  50% {
    box-shadow: 0 0 20px rgba(245, 158, 11, 1);
  }
  100% {
    box-shadow: 0 0 10px rgba(245, 158, 11, 0.6);
  }
}

.animated-background {
  position: absolute;
  top: 10%;
  right: 15%;
  width: 200px;
  height: 200px;
  z-index: 0;
}

.animated-background .circle {
  position: absolute;
  width: 100px;
  height: 100px;
  background: rgba(245, 158, 11, 0.3);
  border-radius: 50%;
  animation: float 6s ease-in-out infinite;
}

.animated-background .circle:nth-child(1) {
  top: 0;
  left: 50%;
  transform: translateX(-50%);
  animation-delay: 0s;
}

.animated-background .circle:nth-child(2) {
  top: 50%;
  left: 0;
  transform: translateY(-50%);
  animation-delay: 2s;
}

.animated-background .circle:nth-child(3) {
  top: 100%;
  left: 50%;
  transform: translate(-50%, -100%);
  animation-delay: 4s;
}

@keyframes float {
  0% {
    transform: translate(-50%, -50%) scale(1);
    opacity: 0.3;
  }
  50% {
    transform: translate(-50%, -60%) scale(1.2);
    opacity: 0.6;
  }
  100% {
    transform: translate(-50%, -50%) scale(1);
    opacity: 0.3;
  }
}

/* Responsive Adjustments */
@media (max-width: 1024px) {
  .hero-title {
    font-size: 3.5rem;
  }

  .hero-description {
    font-size: 1.3rem;
  }

  .play-now-button {
    padding: 0.7rem 2rem;
    font-size: 1.1rem;
  }
}

@media (max-width: 768px) {
  .hero-title {
    font-size: 2.5rem;
  }

  .hero-description {
    font-size: 1.1rem;
    margin-bottom: 2rem;
  }

  .play-now-button {
    padding: 0.6rem 1.8rem;
    font-size: 1rem;
  }

  .animated-background {
    display: none;
  }
}

@media (max-width: 480px) {
  .hero-title {
    font-size: 2rem;
  }

  .hero-description {
    font-size: 1rem;
  }

  .play-now-button {
    padding: 0.5rem 1.5rem;
    font-size: 0.9rem;
  }
}
</style>