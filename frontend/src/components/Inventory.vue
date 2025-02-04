<script setup>
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
  margin-top: 1.5rem;
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
  color: #f8facc;
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
  background: linear-gradient(145deg, #6e7075, #8a8c90);
  border: 2px solid #444;
  display: flex;
  align-items: center;
  justify-content: center;
  height: 50px;
  transition: transform 0.3s, box-shadow 0.3s;
  border-radius: 5px;
  box-shadow: 0 2px 5px rgba(0, 0, 0, 0.2);
}

.grid-item:hover {
  transform: scale(1.1);
  box-shadow: 0 4px 10px rgba(255, 255, 255, 0.5);
  background: linear-gradient(145deg, #8a8c90, #6e7075);
}
</style>