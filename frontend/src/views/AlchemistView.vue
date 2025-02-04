<script setup>
import { storeToRefs } from "pinia";
import { useAlchemistStore } from "@/stores/AlchemistStore.js";
import AlchemistPath from "@/components/AlchemistPath.vue";


const store = useAlchemistStore();
const { skillTreeData, availablePoints } = storeToRefs(store);
</script>

<template>
  <div class="skill-tree-container">
    <div class="points-display">
      Available Points: {{ availablePoints }}
    </div>
    <div class="skill-tree">
      <div
        v-for="(pathData, pathKey) in skillTreeData"
        :key="pathKey"
        class="skill-path-container"
      >
        <h2 class="path-title">{{ pathData.title }}</h2>
        <AlchemistPath :path-data="pathData" :path-key="pathKey" />
      </div>
    </div>
  </div>
</template>

<style scoped>
.skill-tree-container {
  padding: 2rem;
  background: #121212;
  min-height: 100vh;
  color: #f5f5f5;
}

.points-display {
  position: fixed;
  top: 1rem;
  right: 1rem;
  background-color: #2a2a2a;
  padding: 0.75rem 1rem;
  border-radius: 4px;
  font-size: 1.2rem;
  box-shadow: 0 2px 6px rgba(0, 0, 0, 0.5);
}

.skill-tree {
  display: flex;
  flex-direction: column;
  gap: 4rem;
  margin-left: 4rem;
}

.skill-path-container {
  position: relative;
  margin-bottom: 2rem;
}

.path-title {
  position: absolute;
  left: -3rem;
  top: 50%;
  transform: translateY(-50%);
  writing-mode: vertical-lr;
  text-orientation: mixed;
  font-size: 1.5rem;
  margin: 0;
  padding: 1rem;
  color: #bbb;
}
</style>
