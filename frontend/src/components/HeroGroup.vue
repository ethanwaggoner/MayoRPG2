<script setup>
import { useRouter } from 'vue-router'

const props = defineProps({
  heroes: {
    type: Array,
    default: () => []
  },
  groupNumber: {
    type: Number,
    required: true
  }
})

const router = useRouter()

function routeToNewHero() {
  router.push({ name: 'ChooseHero' })
}
</script>

<template>
  <div class="hero-container">
    <h2>Hero Group {{ groupNumber }}</h2>
    <div class="row">
      <div v-for="index in 3" :key="index" class="hero-square">
        <template v-if="heroes.length >= index && heroes[index - 1].image">
          <div class="hero-card">
            <p class="hero-name">{{ heroes[index - 1].name }}</p>
            <p class="hero-level">
              Level: {{ heroes[index - 1].level }} {{ heroes[index - 1].heroClass }}
            </p>
            <img :src="heroes[index - 1].image" alt="Hero" class="hero-image" />
          </div>
        </template>
        <i
          v-else
          class="fas fa-plus plus-icon"
          @click="routeToNewHero"
          title="Create New Hero"
        ></i>
      </div>
    </div>
    <div class="row">
      <div v-for="index in 2" :key="index + 3" class="hero-square">
        <template v-if="heroes.length >= index + 3 && heroes[index + 2].image">
          <div class="hero-card">
            <p class="hero-name">{{ heroes[index + 2].name }}</p>
            <p class="hero-level">
              Level: {{ heroes[index + 2].level }} {{ heroes[index + 2].heroClass }}
            </p>
            <img :src="heroes[index + 2].image" alt="Hero" class="hero-image" />
          </div>
        </template>
        <i
          v-else
          class="fas fa-plus plus-icon"
          @click="routeToNewHero"
          title="Create New Hero"
        ></i>
      </div>
    </div>
  </div>
</template>

<style scoped>
.hero-container {
  display: flex;
  flex-direction: column;
  align-items: center;
  width: 100%;
  max-width: 900px;
  font-family: 'Press Start 2P', cursive;
  color: #dac9a6;
}
h2 {
  font-size: 1.5rem;
  margin-bottom: 0.5rem;
  text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.6);
}
.row {
  display: flex;
  justify-content: space-around;
  width: 100%;
  margin-bottom: 1rem;
}
.hero-square {
  position: relative;
  width: 25%;
  padding-bottom: 40%;
  margin: 0.5rem;
  border: 2px solid #c2a368;
  border-radius: 12px;
  background: rgba(57, 38, 25, 0.85);
  box-shadow: 0 4px 10px rgba(194, 163, 104, 0.3);
  transition: transform 0.3s ease, background 0.3s ease, border 0.3s ease;
  display: flex;
  align-items: center;
  justify-content: center;
}
.hero-square:hover {
  background: rgba(79, 56, 39, 0.85);
  transform: scale(1.05) translateY(-5px);
  border-color: #c2a368;
}
.hero-card {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  padding: 2px;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: space-between;
  background: rgba(36, 21, 11, 0.8);
  border-radius: 12px;
}
.hero-name {
  font-size: 0.9rem;
  margin: 2px 0;
  text-align: center;
  text-shadow: 1px 1px 2px #000;
}
.hero-level {
  font-size: 0.6rem;
  margin: 2px 0;
  text-align: center;
  text-shadow: 1px 1px 2px #000;
}
.hero-image {
  width: 100%;
  height: 75%;
  flex-grow: 1;
  object-fit: cover;
  border-radius: 8px;
  margin-top: 2px;
}
.plus-icon {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  font-size: 3.5rem;
  color: #dac9a6;
  opacity: 0.8;
  transition: transform 0.3s, opacity 0.3s;
  cursor: pointer;
  animation: pulse 2s infinite;
}
.hero-square:hover .plus-icon {
  transform: translate(-50%, -50%) scale(1.1);
  opacity: 1;
}
@keyframes pulse {
  0% {
    transform: translate(-50%, -50%) scale(1);
  }
  50% {
    transform: translate(-50%, -50%) scale(1.2);
  }
  100% {
    transform: translate(-50%, -50%) scale(1);
  }
}
</style>
