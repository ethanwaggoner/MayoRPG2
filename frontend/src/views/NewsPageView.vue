<script setup>
import { ref } from 'vue'
import LandingItemScroller from "@/components/LandingItemScroller.vue";
import LandingHeader from "@/components/LandingHeader.vue";
import StartHeroSpawner from "@/components/StartHeroSpawner.vue";

const newsItems = ref([
  {
    id: 1,
    title: "Welcome to MayoRPG Alpha Test 1",
    date: "2025-02-10",
    content:
      "Greetings, players of MayoRPG! I'm thrilled to announce that Alpha Test 1 is now live. Log in, sign up, create your town, and choose your heroes as you explore this new game. Your feedback is super valuable and will help shape the future of MayoRPG!"
  },

])
</script>

<template>
  <LandingHeader />
  <LandingItemScroller />
  <div class="news-page">
    <h1 class="page-title">MayoRPG News</h1>
    <p class="intro">
      Welcome, players! Here you’ll find the latest updates and announcements as we build the world of MayoRPG.
    </p>
    <div class="news-list">
      <div v-for="news in newsItems" :key="news.id" class="news-item">
        <h2 class="news-title">{{ news.title }}</h2>
        <p class="news-date">{{ news.date }}</p>
        <p class="news-content">{{ news.content }}</p>
      </div>
    </div>
  </div>
  <StartHeroSpawner />
</template>

<style scoped>
.news-page {
  min-height: 100vh;
  background: rgba(18, 18, 18, 0.9);
  backdrop-filter: blur(5px);
  color: #f8facc;
  padding: 40px 20px;
  font-family: 'Press Start 2P', cursive;
  margin-left: 10rem;
  margin-right: 10rem;
  margin-top: 5rem;
}

.page-title {
  text-align: center;
  font-size: 2.5rem;
  margin-bottom: 20px;
  color: #fff;
}

.intro {
  text-align: center;
  font-size: 1rem;
  margin-bottom: 40px;
  color: #b8b9cf;
}

.news-list {
  display: flex;
  flex-direction: column;
  gap: 24px;
}

.news-item {
  background: rgba(255, 255, 255, 0.05);
  border: 1px solid rgba(255, 255, 255, 0.1);
  padding: 24px;
  border-radius: 16px;
  box-shadow: 0 4px 12px rgba(92, 107, 192, 0.2);
  transition: transform 0.2s, box-shadow 0.2s;
}

.news-item:hover {
  transform: translateY(-2px);
  box-shadow: 0 8px 16px rgba(92, 107, 192, 0.3);
}

.news-title {
  font-size: 1.5rem;
  margin-bottom: 8px;
  color: #fff;
}

.news-date {
  font-size: 0.8rem;
  color: #b8b9cf;
  margin-bottom: 16px;
}

.news-content {
  font-size: 0.9rem;
  color: #f8facc;
}
</style>
