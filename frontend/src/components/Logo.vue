<script setup>
import logo from '@/assets/logo-no-background.png';
</script>

<template>
  <div class="logo-container">
    <router-link to="/">
      <img class="logo" :src="logo" alt="Logo" />
    </router-link>
  </div>
</template>

<style scoped>
.logo {
  width: 100px;
  height: auto;
  transition: transform 0.3s ease-in-out;
}

.logo:hover {
  transform: scale(1.1);
}
</style>