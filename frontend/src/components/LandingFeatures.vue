<script>
import CraftingIcon from "@/assets/items/tile924.png";
import GatheringIcon from "@/assets/items/tile849.png";
import HungerIcon from "@/assets/items/tile913.png";

export default {
  name: 'Features',
  data() {
    return {
      featuresData: [
        {
          id: 1,
          icon: CraftingIcon,
          title: 'Incremental Gameplay',
          description:
            "Progress even when you're away. Let your heroes grow and conquer while you take a break.",
        },
        {
          id: 2,
          icon: GatheringIcon,
          title: '2D Pixel Graphics',
          description:
            'Experience a nostalgic pixel art style with modern enhancements for an engaging visual journey.',
        },
        {
          id: 3,
          icon: HungerIcon,
          title: 'Deep Itemization',
          description:
            'Immerse yourself in a rich character build making, where every decision has an effect.',
        },
        // Add more features as needed
      ],
    };
  },
};
</script>

<template>
  <section id="features" class="features-section">
    <div class="container">
      <h2 class="section-title">Features</h2>
      <div class="features-grid">
        <div
          class="feature-card"
          v-for="feature in featuresData"
          :key="feature.id"
        >
          <div class="icon-container">
            <img :src="feature.icon" :alt="feature.title" class="feature-icon" />
          </div>
          <h3 class="feature-title">{{ feature.title }}</h3>
          <p class="feature-description">{{ feature.description }}</p>
        </div>
      </div>
    </div>
  </section>
</template>

<style scoped>
.features-section {
  padding: 5rem 2rem;
  background: linear-gradient(135deg, #1a1a1a, #2c2c2c);
  color: #f8facc;
  font-family: 'Press Start 2P', cursive;
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
  background-color: #f59e0b;
  display: block;
  margin: 1rem auto 0;
  border-radius: 2px;
}

.features-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
  gap: 2.5rem;
  justify-items: center;
}

.feature-card {
  background: rgba(255, 255, 255, 0.05);
  backdrop-filter: blur(10px);
  border-radius: 15px;
  padding: 2rem;
  text-align: center;
  position: relative;
  overflow: hidden;
  transition: transform 0.3s ease, box-shadow 0.3s ease;
}

.feature-card::before {
  content: '';
  position: absolute;
  top: -50%;
  left: -50%;
  width: 200%;
  height: 200%;
  background: radial-gradient(circle at center, rgba(245, 158, 11, 0.2), transparent 70%);
  transform: rotate(45deg);
  transition: opacity 0.3s ease;
  opacity: 0;
}

.feature-card:hover::before {
  opacity: 1;
}

.feature-card:hover {
  transform: translateY(-15px);
  box-shadow: 0 15px 30px rgba(245, 158, 11, 0.3);
}

.icon-container {
  width: 80px;
  height: 80px;
  margin: 0 auto 1.5rem;
  border-radius: 50%;
  background-color: #2c2c2c;
  display: flex;
  align-items: center;
  justify-content: center;
  box-shadow: 0 0 15px rgba(245, 158, 11, 0.5);
  transition: transform 0.3s ease, box-shadow 0.3s ease;
}

.feature-card:hover .icon-container {
  transform: scale(1.1);
  box-shadow: 0 0 25px rgba(245, 158, 11, 0.7);
}

.feature-icon {
  width: 40px;
  height: 40px;
}

.feature-title {
  font-size: 1.75rem;
  margin-bottom: 1rem;
  color: #f59e0b;
}

.feature-description {
  font-size: 1rem;
  color: #d1d5db;
  line-height: 1.6;
}

/* Responsive Adjustments */
@media (max-width: 768px) {
  .section-title {
    font-size: 2.5rem;
  }

  .feature-title {
    font-size: 1.5rem;
  }

  .feature-description {
    font-size: 0.95rem;
  }

  .icon-container {
    width: 70px;
    height: 70px;
  }

  .feature-icon {
    width: 35px;
    height: 35px;
  }
}

@media (max-width: 480px) {
  .section-title {
    font-size: 2rem;
  }

  .features-grid {
    grid-template-columns: 1fr;
  }

  .feature-card {
    padding: 1.5rem;
  }

  .feature-title {
    font-size: 1.25rem;
  }

  .feature-description {
    font-size: 0.9rem;
  }
}
</style>