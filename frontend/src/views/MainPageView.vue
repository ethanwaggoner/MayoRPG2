<script setup>
import SideBarMenu from "@/components/SideBarMenu.vue";
import Inventory from "@/components/Inventory.vue";
import HeroGroup from "@/components/HeroGroup.vue";
import TopBarStats from "@/components/TopBarStats.vue";
import BattleButton from "@/components/BattleButton.vue";
import PlayerLevelBar from "@/components/PlayerLevelBar.vue";

import { useHeroStore } from "@/stores/HeroStore.js";
import { useTownStore } from "@/stores/TownStore.js";
import { computed, onMounted } from "vue";
import { useRouter } from "vue-router";
import LandingItemScroller from "@/components/LandingItemScroller.vue";

const heroStore = useHeroStore();
const townStore = useTownStore();
const router = useRouter();

const heroes1 = computed(() => heroStore.HeroGroup1);
const heroes2 = computed(() => heroStore.HeroGroup2);

onMounted(async () => {
  await townStore.loadTowns();
  if (townStore.currentTown) {
    await heroStore.loadHeroData(townStore.currentTown.uuid);
  } else {
    console.error("No current town available");
  }
});

</script>

<template>
  <LandingItemScroller />
  <div class="container">
    <div class="row">
      <div class="col-4">
        <SideBarMenu />
      </div>
      <div class="col-8">
        <div class="row">
          <div class="col-12">
            <TopBarStats />
          </div>
        </div>
        <div class="row">
          <div class="col-6">
            <HeroGroup :heroes="heroes1" :group-number="1" />
          </div>
          <div class="col-6">
            <HeroGroup :heroes="heroes2" :group-number="2" />
          </div>
        </div>
        <div class="row">
          <div class="col-12">
            <PlayerLevelBar />
          </div>
        </div>
        <div class="row">
          <div class="col-10">
            <Inventory />
          </div>
          <div class="col-2 align-self-end">
            <BattleButton />
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
.container {
  width: 100%;
  height: 100%;
  display: flex;
  flex-direction: column;
  position: relative;
  z-index: 1;
  background: rgba(36, 21, 11, 0.8);
  border: 2px solid #c2a368;
  border-radius: 10px;
  box-shadow: 0 0 15px rgba(194, 163, 104, 0.3);
  padding: 10px;
  font-family: 'Press Start 2P', cursive;
  color: #dac9a6;
}
</style>
