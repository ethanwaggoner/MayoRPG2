<script setup>
import slotBackground from '@/assets/items/tile1008.png'
</script>

<template>
  <div class="inventory-container">
    <h2 class="inventory-title">Loot</h2>
    <div class="grid">
      <div v-for="item in 44" :key="item" class="grid-item"></div>
    </div>
  </div>
</template>

<style scoped>
.inventory-container {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  width: 100%;
  height: 100%;
  background-size: cover;
  padding: 20px;
  border-radius: 10px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.3);
}

.inventory-title {
  font-size: 2rem;
  color: #dac9a6;
  margin-bottom: 1rem;
  text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.5);
  font-family: 'Press Start 2P', cursive;
}

.grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(50px, 1fr));
  grid-gap: 10px;
  width: 100%;
  height: auto;
}

.grid-item {
  width: 50px;
  height: 50px;
  background: url("@/assets/items/tile1008.png") no-repeat center center;
  background-size: cover;
  border: 2px solid #444;
  border-radius: 5px;
  box-shadow: 0 2px 5px rgba(0, 0, 0, 0.2);
  transition: transform 0.3s, box-shadow 0.3s;
}

.grid-item:hover {
  transform: scale(1.1);
  box-shadow: 0 4px 10px rgba(255, 255, 255, 0.5);
}
</style>
