<script setup>

</script>

<template>
  <div class="battle-container">
    <h2 class="battle-text">To Battle!</h2>
    <img src="../assets/items/tile131.png" alt="To Battle" class="battle-image"/>
  </div>
</template>

<style scoped>
.battle-container {
  text-align: center;
  padding: 10px;
  margin-bottom: 50px;
}

.battle-container:hover {
  cursor: pointer;
}

.battle-image, .battle-text {
  animation: breathe 2s ease-in-out infinite;
}

@keyframes breathe {
  0%, 100% {
    transform: scale(1);
  }
  50% {
    transform: scale(1.1);
  }
}

.battle-image {
  max-width: 100%;
  height: auto;
  display: block;
  margin: 0 auto;
  scale: 2.5;
}

.battle-text {
  font-size: 1em;
  color: #dac9a6;
  margin-bottom: 6rem;
}
</style>