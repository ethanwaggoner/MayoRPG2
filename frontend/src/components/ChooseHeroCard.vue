<script setup>
import {computed} from "vue";

import FireAttackIcon from "@/assets/items/tile096.png";
import WaterAttackIcon from "@/assets/items/tile032.png";
import DarkAttackIcon from "@/assets/items/tile064.png";
import LightAttackIcon from "@/assets/items/tile000.png";

import AttackSpeedIcon from "@/assets/items/tile118.png";

import FireDefenseIcon from "@/assets/items/tile117.png";
import WaterDefenseIcon from "@/assets/items/tile053.png";
import DarkDefenseIcon from "@/assets/items/tile085.png";
import LightDefenseIcon from "@/assets/items/tile021.png";

import HealthIcon from "@/assets/items/tile403.png";

const icons = {
  "Fire Attack": FireAttackIcon,
  "Water Attack": WaterAttackIcon,
  "Dark Attack": DarkAttackIcon,
  "Light Attack": LightAttackIcon,
  "Attack Speed": AttackSpeedIcon,
  "Fire Defense": FireDefenseIcon,
  "Water Defense": WaterDefenseIcon,
  "Dark Defense": DarkDefenseIcon,
  "Light Defense": LightDefenseIcon,
  "Health": HealthIcon
};

const props = defineProps({
  hero: Object,
  isSelected: Boolean
});

const offenseKeys = [
  "Fire Attack",
  "Water Attack",
  "Light Attack",
  "Dark Attack",
  "Attack Speed"
];

const defenseKeys = [
  "Fire Defense",
  "Water Defense",
  "Light Defense",
  "Dark Defense"
];

const offenseStats = computed(() => {
  return props.hero.stats
      ? Object.entries(props.hero.stats).filter(([key, value]) => offenseKeys.includes(key))
      : [];
});

const defenseStats = computed(() => {
  return props.hero.stats
      ? Object.entries(props.hero.stats).filter(([key, value]) => defenseKeys.includes(key))
      : [];
});

const passiveDescription = computed(() => props.hero.passive.description);
</script>

<template>
  <div class="hero-card">
    <h2>{{ props.hero.name }}</h2>
    <div class="hero-image-container">
      <img :src="props.hero.image" :alt="props.hero.name" class="hero-image"/>
      <div v-if="passiveDescription" class="passive-description">
        {{ passiveDescription }}
      </div>
    </div>
    <div class="health" v-if="props.hero.stats">
      <img :src="icons.Health" class="stat-icon"/>
      <span class="stat-label">Health:</span>
      <span class="stat-value">{{ props.hero.stats.Health }}</span>
    </div>
    <div class="hero-stats" v-if="props.hero.stats">
      <div class="stat-column">
        <div
            v-for="([key, value]) in offenseStats"
            :key="'offense-' + key"
            class="stat-row"
        >
          <img :src="icons[key]" class="stat-icon"/>
          <span class="stat-label">{{ key }}:</span>
          <span class="stat-value">{{ value }}</span>
        </div>
      </div>
      <div class="stat-column">
        <div
            v-for="([key, value]) in defenseStats"
            :key="'defense-' + key"
            class="stat-row"
        >
          <img :src="icons[key]" class="stat-icon"/>
          <span class="stat-label">{{ key }}:</span>
          <span class="stat-value">{{ value }}</span>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
.hero-card {
  background-image: linear-gradient(135deg, #6d5648 0%, #3e312d 100%);
  border-radius: 12px;
  padding: 20px;
  text-align: center;
  font-size: 0.7rem;
  color: #f8facc;
  font-family: "Press Start 2P", cursive;
  width: 400px;
  height: 450px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.3);
  transition: transform 0.3s ease, box-shadow 0.3s ease;
}

.hero-card:hover {
  transform: scale(1.05);
  box-shadow: 0 8px 16px rgba(0, 0, 0, 0.4);
}

.hero-image-container {
  position: relative;
}

.hero-image {
  width: 100px;
  height: 100px;
  object-fit: contain;
  margin-bottom: 15px;
  border-radius: 50%;
  border: 3px solid #fff;
}

.passive-description {
  position: absolute;
  top: 110%;
  left: 50%;
  transform: translateX(-50%);
  background-color: rgba(0, 0, 0, 0.8);
  color: #f8facc;
  padding: 10px;
  border-radius: 8px;
  width: 200px;
  text-align: center;
  font-size: 0.8rem;
  display: none;
}

.hero-image-container:hover .passive-description {
  display: block;
}

.health {
  margin-bottom: 20px;
}

.hero-stats {
  display: flex;
  justify-content: space-between;
  margin-bottom: 20px;
}

.stat-column {
  display: flex;
  flex-direction: column;
  flex: 1;
  padding: 0 10px;
}

.stat-row {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 8px;
}

.stat-icon {
  width: 24px;
  height: 24px;
  margin-right: 10px;
}

.stat-label {
  flex: 1;
  text-align: left;
}

.stat-value {
  flex: 1;
  text-align: right;
}

.passive {
  margin-left: 10px;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: start;
  gap: 0;
}
</style>
