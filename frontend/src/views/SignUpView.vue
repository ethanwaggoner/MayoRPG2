<script setup>

import SignUp from "@/components/SignUp.vue";
import StartHeroSpawner from "@/components/StartHeroSpawner.vue";
import LandingHeader from "@/components/LandingHeader.vue";
import LandingItemScroller from "@/components/LandingItemScroller.vue";
</script>

<template>
  <transition name="fade" appear>
    <div>
        <LandingItemScroller />
        <LandingHeader />
        <SignUp />
        <StartHeroSpawner />
    </div>
  </transition>

</template>

<style scoped>
.fade-enter-active,
.fade-leave-active,
.fade-appear-active {
  transition: opacity .5s ease;
}

.fade-enter-from,
.fade-leave-to,
.fade-appear-from {
  opacity: 0;
}

.fade-enter-to,
.fade-leave-from,
.fade-appear-to {
  opacity: 1;
}
</style>