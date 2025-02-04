<script setup>
import { useRouter } from 'vue-router';

import blacksmith from "@/assets/items/tile975.png";
import alchemist from "@/assets/items/tile786.png";
import tavern from "@/assets/items/tile956.png";
import mine from "@/assets/items/tile661.png";
import farms from "@/assets/items/tile894.png";
import exit from "@/assets/items/tile924.png";

const menuItems = [
  { label: 'Tavern', icon: tavern, route: '/tavern' },
  { label: 'Mines', icon: mine, route: '/mines' },
  { label: 'Farms', icon: farms, route: '/farms' },
  { label: 'Blacksmith', icon: blacksmith, route: '/blacksmith' },
  { label: 'Alchemist', icon: alchemist, route: '/alchemist' },
  { label: 'Exit', icon: exit, route: '/' }
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
        <img :src="item.icon" :alt="item.label" class="icon" />
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
  background: linear-gradient(135deg, #1a1a1a, #000);
  border: 2px solid #444;
  border-radius: 15px;
  box-shadow: 0 0 20px rgba(0, 255, 255, 0.3);
  display: flex;
  justify-content: center;
  align-items: center;
}

.sidebar ul {
  list-style: none;
  padding: 0;
  margin: 0;
  width: 100%;
  /* Use flex layout to evenly distribute the menu items */
  display: flex;
  flex-direction: column;
  height: 100%;
}

.sidebar li {
  display: flex;
  align-items: center;
  justify-content: flex-start;
  padding: 15px 20px;
  border-radius: 10px;
  cursor: pointer;
  transition: background 0.3s, transform 0.3s;
  background: rgba(255, 255, 255, 0.05);
  flex: 1;
  margin: 4px 0;
}

.sidebar li:hover {
  background: rgba(0, 255, 255, 0.1);
  transform: translateX(5px);
}

.icon {
  width: 40px;
  height: 40px;
  margin-right: 20px;
  filter: drop-shadow(0 0 5px rgba(0, 255, 255, 0.7));
}

.sidebar span {
  font-size: 1.8rem;
  color: #f8facc;
  font-family: 'Press Start 2P', cursive;
  text-shadow: 1px 1px 2px #000;
}
</style>
