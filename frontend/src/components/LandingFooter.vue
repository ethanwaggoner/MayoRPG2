<script setup>

import StartHeroSpawner from "@/components/StartHeroSpawner.vue";
</script>

<template>
  <footer class="footer">
    <div class="container">
      <p class="footer-text">&copy; 2024 MayoRPG. All rights reserved.</p>
      <div class="social-links">
        <a href="#" class="social-link" aria-label="Twitter">Twitter</a>
        <a href="#" class="social-link" aria-label="Discord">Discord</a>
        <a href="#" class="social-link" aria-label="GitHub">GitHub</a>
      </div>
    </div>
  </footer>
</template>

<style scoped>
.footer {
  padding: 2rem;
  background: linear-gradient(135deg, #1a1a1a, #2c2c2c);
  text-align: center;

}

.footer-text {
  font-size: 1rem;
  color: #ffffff;
}

.social-links {
  display: flex;
  justify-content: center;
  gap: 1.5rem;
  margin-top: 1rem;
  margin-bottom: 3rem;
}

.social-link {
  color: #ffffff;
  text-decoration: none;
  font-size: 1rem;
  transition: color 0.3s ease;
}

.social-link:hover {
  color: #f59e0b; /* Yellow-500 */
}

@media (max-width: 768px) {
  .social-links {
    flex-direction: column;
    gap: 1rem;
  }
}
</style>