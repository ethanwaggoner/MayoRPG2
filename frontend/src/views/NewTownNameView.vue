<script setup>
import { ref, computed, onMounted } from 'vue'
import router from '@/router.js'
import { useTownStore } from '@/stores/TownStore.js'
import { useUserStore } from '@/stores/UserStore.js'
import StartHeroSpawner from '@/components/StartHeroSpawner.vue'
import { useHeroStore } from "@/stores/HeroStore.js";

const townStore = useTownStore()
const userStore = useUserStore()
const heroStore = useHeroStore()

const showCreateModal = ref(false)
const newTownName = ref('')
const selectedSlotIndex = ref(null)
let username = ref('')

const townSlots = computed(() => {
  const slots = []
  const towns = townStore.towns
  for (let i = 0; i < 5; i++) {
    slots.push(towns[i] || null)
  }
  return slots
})

function handleSlotClick(index) {
  const slot = townSlots.value[index]
  if (slot) {
    loadTown(slot)
  } else {
    selectedSlotIndex.value = index
    showCreateModal.value = true
  }
}

async function loadTown(town) {
  try {
    await townStore.selectTown(town.uuid)
    await heroStore.setCurrentTownUuid(town.uuid)
    if (!town.id) {
      await router.push('/choose-hero')
    } else {
      await router.push('/main-page')
    }
  } catch (error) {
    console.error('Error loading town:', error)
  }
}

async function createTown() {
  if (!newTownName.value) {
    alert("Please enter a town name.")
    return
  }
  try {
    await townStore.createTown({name: newTownName.value})
    newTownName.value = ''
    showCreateModal.value = false
    await router.push('/choose-hero')
  } catch (error) {
    console.error('Error creating town:', error)
  }
}

function cancelCreation() {
  newTownName.value = ''
  showCreateModal.value = false
}

function formatDate(dateString) {
  if (!dateString) return 'Unknown'
  const options = {year: 'numeric', month: 'short', day: 'numeric'}
  return new Date(dateString).toLocaleDateString(undefined, options)
}

onMounted(() => {
  userStore.fetchCurrentUser()
  username = userStore.user.username
  if (userStore.user) {
    townStore.loadTowns(userStore.user.id)
  }
})
</script>

<template>
  <div class="town-manager-container">
    <div class="save-slots">
      <h2 class="sidebar-title">Your Town Saves {{ username }}</h2>
      <div class="slots-grid">
        <div v-for="(slot, index) in townSlots" :key="index" class="save-slot" @click="handleSlotClick(index)">
          <div v-if="slot" class="town-info">
            <h3 class="town-name">{{ slot.name }}</h3>
            <p class="town-date">Created: {{ formatDate(slot.created_at) }}</p>
            <p class="town-info-detail">Level {{ slot.level || '1' }}</p>
          </div>
          <div v-else class="empty-slot">
            <p>Empty Save Slot</p>
            <p class="create-prompt">Click to create a new town</p>
          </div>
        </div>
      </div>
    </div>
    <StartHeroSpawner/>
    <div v-if="showCreateModal" class="modal-overlay">
      <div class="modal-content">
        <h2>Create a New Town</h2>
        <input v-model="newTownName" type="text" placeholder="Enter town name" class="modal-input"/>
        <div class="modal-buttons">
          <button @click="createTown" class="modal-submit">Create</button>
          <button @click="cancelCreation" class="modal-cancel">Cancel</button>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
.town-manager-container {
  display: flex;
  justify-content: center;
  align-items: flex-start;
  width: 100%;
  height: 100vh;
  position: relative;
}

.save-slots {
  width: 30%;
  max-height: 100vh;
  padding: 20px;
  background: linear-gradient(135deg, #0d0d0d, #1a1a1a);
  border-right: 2px solid #00ffff;
  overflow-y: auto;
  box-shadow: 2px 0 15px rgba(0, 255, 255, 0.3);
}

.sidebar-title {
  font-family: 'Press Start 2P', cursive;
  text-align: center;
  margin-bottom: 20px;
  font-size: 1.5em;
  border-bottom: 2px solid #00ffff;
  padding-bottom: 10px;
  color: #f8facc;
}

.slots-grid {
  display: grid;
  grid-template-columns: 1fr;
  gap: 20px;
}

.save-slot {
  background: linear-gradient(45deg, #1a1a1a, #333);
  border: 2px solid #00ffff;
  border-radius: 10px;
  padding: 15px;
  cursor: pointer;
  transition: transform 0.3s ease, box-shadow 0.3s ease;
}

.save-slot:hover {
  transform: scale(1.03);
  box-shadow: 0 0 15px rgba(0, 255, 255, 0.6);
}

.town-info h3 {
  font-family: 'Press Start 2P', cursive;
  margin: 0;
  font-size: 1.2em;
  color: #f8facc;
}

.town-date,
.town-info-detail {
  font-family: 'Press Start 2P', cursive;
  font-size: 0.8em;
  margin: 5px 0;
  color: #f8facc;
}

.empty-slot {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  height: 100px;
  font-family: 'Press Start 2P', cursive;
  font-size: 1em;
  color: #f8facc;
  text-align: center;
  border: 2px dashed #00ffff;
  border-radius: 10px;
}

.create-prompt {
  font-size: 0.8em;
  margin-top: 5px;
  color: #00ffff;
}

.modal-overlay {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: rgba(0, 0, 0, 0.9);
  display: flex;
  align-items: center;
  justify-content: center;
  z-index: 100;
}

.modal-content {
  background: linear-gradient(45deg, #1a1a1a, #333);
  border: 2px solid #00ffff;
  border-radius: 10px;
  padding: 30px;
  width: 480px;
  text-align: center;
  box-shadow: 0 0 20px rgba(0, 255, 255, 0.8);
  color: #f8facc;
  font-family: 'Press Start 2P', cursive;
}

.modal-input {
  width: 100%;
  padding: 10px;
  margin: 20px 0;
  border: 2px solid #333;
  border-radius: 10px;
  font-family: 'Press Start 2P', cursive;
  font-size: 1em;
  background: #f8facc;
  color: #333;
}

.modal-buttons {
  display: flex;
  justify-content: space-between;
}

.modal-submit,
.modal-cancel {
  background: #333;
  color: #f8facc;
  border: 2px solid #00ffff;
  border-radius: 10px;
  padding: 10px;
  cursor: pointer;
  flex: 1;
  margin: 0 5px;
  font-family: 'Press Start 2P', cursive;
  transition: background-color 0.3s ease, transform 0.3s ease;
}

.modal-submit:hover,
.modal-cancel:hover {
  background: #1a1a1a;
  transform: scale(1.05);
}
</style>
