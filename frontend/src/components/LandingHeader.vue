<script setup>

</script>

<template>
  <header class="header">
    <div class="container">
      <router-link to="/">
        <div class="logo">
          <img src="../assets/logo-no-background.png" alt="MayoRPG Logo" class="logo-image" />
          <span class="logo-text">MayoRPG</span>
        </div>
      </router-link>
      <nav>
        <ul class="nav-links">
          <li><a href="/news">News</a></li>
          <li><a href="#features">Features</a></li>
          <li><a href="#gallery">Gallery</a></li>
          <li><a href="#hero">Play Now</a></li>
        </ul>
      </nav>
      <div class="mobile-menu-toggle" @click="toggleMenu">
        <span class="bar"></span>
        <span class="bar"></span>
        <span class="bar"></span>
      </div>
    </div>
    <div :class="['mobile-nav', { 'mobile-nav-active': isMenuActive }]">
      <ul class="mobile-nav-links">
        <li><a href="#hero" @click="toggleMenu">Home</a></li>
        <li><a href="#features" @click="toggleMenu">Features</a></li>
        <li><a href="#gallery" @click="toggleMenu">Gallery</a></li>
        <li><a href="#download" @click="toggleMenu">Download</a></li>
      </ul>
    </div>
  </header>
</template>

<style scoped>
.header {
  color: #f8facc;
  font-family: 'Press Start 2P', cursive;
  position: fixed;
  top: 0;
  width: 100%;
  backdrop-filter: blur(10px);
  background: rgba(18, 18, 18, 0.8);
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.5);
  z-index: 1000;
  transition: background 0.3s ease;
}

.container {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 1rem 2rem;
  max-width: 1200px;
  margin: 0 auto;
}

.logo {
  display: flex;
  align-items: center;
  gap: 0.5rem;
}

.logo-image {
  width: 50px;
  height: 50px;
  filter: drop-shadow(0 0 10px #f59e0b);
  transition: transform 0.3s ease;
}

.logo-image:hover {
  transform: scale(1.1);
}

.logo-text {
  font-size: 1.5rem;
  font-weight: bold;
  color: #f59e0b;
  text-shadow: 0 0 10px #f59e0b;
  transition: color 0.3s ease, text-shadow 0.3s ease;
}

.logo-text:hover {
  color: #ffffff;
  text-shadow: 0 0 15px #ffffff;
}

.nav-links {
  list-style: none;
  display: flex;
  gap: 2rem;
}

.nav-links a {
  color: #ffffff;
  text-decoration: none;
  font-size: 1rem;
  position: relative;
  transition: color 0.3s ease;
}

.nav-links a::after {
  content: '';
  position: absolute;
  width: 0%;
  height: 2px;
  background: #f59e0b;
  left: 0;
  bottom: -4px;
  transition: width 0.3s ease;
}

.nav-links a:hover::after {
  width: 100%;
}

.nav-links a:hover {
  color: #f59e0b;
}

.mobile-menu-toggle {
  display: none;
  flex-direction: column;
  gap: 5px;
  cursor: pointer;
}

.bar {
  width: 25px;
  height: 3px;
  background-color: #ffffff;
  border-radius: 2px;
  transition: all 0.3s ease;
}

.mobile-nav {
  display: none;
}

.mobile-nav-active {
  display: block;
  position: fixed;
  top: 70px;
  right: 0;
  width: 100%;
  height: calc(100% - 70px);
  background: rgba(18, 18, 18, 0.95);
  backdrop-filter: blur(5px);
  transition: transform 0.3s ease;
}

.mobile-nav-links {
  list-style: none;
  display: flex;
  flex-direction: column;
  gap: 2rem;
  align-items: center;
  margin-top: 3rem;
}

.mobile-nav-links a {
  color: #ffffff;
  text-decoration: none;
  font-size: 1.5rem;
  transition: color 0.3s ease;
}

.mobile-nav-links a:hover {
  color: #f59e0b;
}

/* Responsive Styling */
@media (max-width: 768px) {
  .nav-links {
    display: none;
  }

  .mobile-menu-toggle {
    display: flex;
  }
}
</style>