<script setup>
import { useRouter } from 'vue-router';

import blacksmith from "@/assets/items/tile975.png";
import alchemist from "@/assets/items/tile786.png";
import tavern from "@/assets/items/tile956.png";
import mine from "@/assets/items/tile661.png";
import farms from "@/assets/items/tile894.png";
import exit from "@/assets/items/tile924.png";

const menuItems = [
  {label: 'Tavern', icon: tavern, route: '/tavern'},
  {label: 'Mines', icon: mine, route: '/mines'},
  {label: 'Farms', icon: farms, route: '/farms'},
  {label: 'Blacksmith', icon: blacksmith, route: '/blacksmith'},
  {label: 'Alchemist', icon: alchemist, route: '/alchemist'},
  {label: 'Exit', icon: exit, route: '/'}
];

const router = useRouter();

function navigate(route) {
  router.push(route);
}
</script>

<template>
  <div class="sidebar">
    <ul>
      <li
          v-for="item in menuItems"
          :key="item.label"
          @click="navigate(item.route)"
      >
        <img :src="item.icon" :alt="item.label" class="icon"/>
        <span>{{ item.label }}</span>
      </li>
    </ul>
  </div>
</template>

<style scoped>
.sidebar {
  width: 100%;
  height: 100%;
  padding: 1rem;
  background: rgba(36, 21, 11, 0.8);
  border: 2px solid #c2a368;
  border-radius: 15px;
  box-shadow: 0 0 20px rgba(194, 163, 104, 0.3);
  display: flex;
  justify-content: center;
  align-items: center;
}

.sidebar ul {
  list-style: none;
  padding: 0;
  margin: 0;
  width: 100%;
  display: flex;
  flex-direction: column;
  height: 100%;
}

.sidebar li {
  display: flex;
  align-items: center;
  justify-content: flex-start;
  padding: 15px 20px;
  margin: 4px 0;
  border-radius: 10px;
  cursor: pointer;
  background: rgba(57, 38, 25, 0.85);
  border: 2px solid transparent;
  transition: background 0.3s, transform 0.3s, border 0.3s;
  flex: 1;
}

.sidebar li:hover {
  background: rgba(79, 56, 39, 0.85);
  border: 2px solid #c2a368;
  transform: translateX(5px);
}

.icon {
  width: 40px;
  height: 40px;
  margin-right: 20px;
  filter: drop-shadow(0 0 5px rgba(194, 163, 104, 0.7));
}

.sidebar span {
  font-size: 1.8rem;
  color: #dac9a6;
  font-family: 'Press Start 2P', cursive;
  text-shadow: 1px 1px 2px #000;
}
</style>
