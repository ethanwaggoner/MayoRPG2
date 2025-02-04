<script setup>

import LandingHeader from "@/components/LandingHeader.vue";
import LandingHero from "@/components/LandingHero.vue";
import LandingFeatures from "@/components/LandingFeatures.vue";
import LandingGallery from "@/components/LandingGallery.vue";
import LandingFooter from "@/components/LandingFooter.vue";
import StartHeroSpawner from "@/components/StartHeroSpawner.vue";
import LandingItemScroller from "@/components/LandingItemScroller.vue";
import {onMounted} from "vue";
import {useUserStore} from "@/stores/UserStore.js";

const userStore = useUserStore()
</script>

<template>
  <div class="landing">
    <LandingHeader />
    <LandingHero />
    <LandingFeatures />
    <LandingGallery />
    <LandingFooter />
    <LandingItemScroller side="left"/>
    <LandingItemScroller side="right"/>
    <StartHeroSpawner class="heroes"/>
  </div>
</template>

<style scoped>
.landing {
  padding-top: 4rem;
  background-color: #121212;
  color: #ffffff;
  font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
}
.heroes {
  z-index: 1;
}
</style>