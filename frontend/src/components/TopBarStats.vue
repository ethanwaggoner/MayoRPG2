<script setup>
import resource1 from '@/assets/items/tile499.png';
import resource2 from '@/assets/items/tile509.png';
import resource3 from '@/assets/items/tile631.png';
import resource4 from '@/assets/items/tile721.png';

const fractions = [
  { numerator: 80, denominator: 99, image: resource1 },
  { numerator: 112, denominator: 5476, image: resource2 },
  { numerator: 56, denominator: 789, image: resource3 },
  { numerator: 44, denominator: 55, image: resource4 }
];
</script>

<template>
  <div class="fraction-menu">
    <div class="fraction" v-for="(fraction, index) in fractions" :key="index">
      <img :src="fraction.image" alt="Resource" class="fraction-image" />
      <div class="fraction-text">
        <p class="numerator">{{ fraction.numerator }}</p>
        <p class="denominator">/ {{ fraction.denominator }}</p>
      </div>
    </div>
  </div>
</template>

<style scoped>
.fraction-menu {
  display: flex;
  justify-content: space-around;
  align-items: center;
  padding: 10px 0;
  border: 2px solid #444;
  border-radius: 10px;
  background: linear-gradient(135deg, #1a1a1a, #000);
  box-shadow: 0 0 15px rgba(0, 255, 255, 0.3);
}

.fraction {
  display: flex;
  align-items: center;
  gap: 20px;
  font-family: 'Press Start 2P', cursive;
  color: #f8facc;
  padding: 5px 10px;
  border-radius: 8px;
  transition: background 0.3s, transform 0.3s;
}

.fraction:hover {
  background: rgba(0, 255, 255, 0.1);
  transform: translateY(-3px);
}

.fraction-image {
  width: 50px;
  height: 50px;
  border-radius: 50%;
  filter: drop-shadow(0 0 5px rgba(0, 255, 255, 0.7));
}

.fraction-text {
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  line-height: 2;
}

.numerator {
  font-size: 16px;
  margin: 0;
  text-shadow: 1px 1px 2px #000;
}

.denominator {
  font-size: 14px;
  margin: 0;
  text-shadow: 1px 1px 2px #000;
}
</style>
