<script setup>
import { ref, computed, onMounted } from 'vue'
import router from '@/router.js'
import { useTownStore } from '@/stores/TownStore.js'
import { useUserStore } from '@/stores/UserStore.js'

const townStore = useTownStore()
const userStore = useUserStore()

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

async function handleSlotClick(index) {
  const slot = townSlots.value[index]
  if (slot) {
    await loadTown(slot)
  } else {
    selectedSlotIndex.value = index
    showCreateModal.value = true
  }
}

async function loadTown(town) {
  try {
    await townStore.selectTown(town.uuid)
    if (!town.id) {
      await router.push('/choose-hero')
    } else {
      await router.push('/main-page')
    }
  } catch (error) {
    console.error('Error loading town:', error)
  }
}

async function deleteTown(townUuid) {
  if (confirm('Are you sure you want to delete this town?')) {
    try {
      await townStore.deleteTown(townUuid)
    } catch (error) {
      console.error('Error deleting town:', error)
    }
  }
}

function createTown() {
  if (!newTownName.value) {
    alert("Please enter a town name.")
    return
  }
  try {
    townStore.createTown({name: newTownName.value})
    newTownName.value = ''
    showCreateModal.value = false
    router.push('/choose-hero')
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
  <div class="outer-wrapper">
    <div class="town-manager-container">
      <div class="save-slots">
        <h2 class="sidebar-title">Your Town Saves {{ username }}</h2>
        <div class="slots-grid">
          <div
              v-for="(slot, index) in townSlots"
              :key="index"
              class="save-slot"
              @click="slot && handleSlotClick(index)"
          >
            <div v-if="slot" class="slot-content">
              <div class="town-info">
                <h3 class="town-name">{{ slot.name }}</h3>
                <p class="town-date">Created: {{ formatDate(slot.created_at) }}</p>
                <div class="town-level-heroes">
                  <p class="town-info-detail">
                    Level {{ slot.level || 1 }}
                  </p>
                  <div class="hero-thumbs">
                    <div
                        v-for="hero in slot.heroes || []"
                        :key="hero.id"
                        class="hero-thumb"
                    >
                      <img
                          :src="hero.image"
                          :alt="hero.name"
                          class="hero-thumb-img"
                      />
                    </div>
                  </div>
                </div>
              </div>
              <button class="delete-button" @click.stop="deleteTown(slot.uuid)">
                Delete
              </button>
            </div>
            <div v-else class="empty-slot" @click="handleSlotClick(index)">
              <p>Empty Save Slot</p>
              <p class="create-prompt">Click to create a new town</p>
            </div>
          </div>
        </div>
      </div>
      <div v-if="showCreateModal" class="modal-overlay">
        <div class="modal-content">
          <h2>Create a New Town</h2>
          <input
              v-model="newTownName"
              type="text"
              placeholder="Enter town name"
              class="modal-input"
          />
          <div class="modal-buttons">
            <button @click="createTown" class="modal-submit">Create</button>
            <button @click="cancelCreation" class="modal-cancel">Cancel</button>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
.outer-wrapper {
  display: flex;
  align-items: center;
  justify-content: center;
  min-height: 100vh;
  background: none;
  margin: 0;
}

.town-manager-container {
  display: flex;
  flex-direction: column;
  background: rgba(36, 21, 11, 0.8);
  border: 2px solid #c2a368;
  border-radius: 10px;
  box-shadow: 0 0 20px rgba(194, 163, 104, 0.8);
  max-width: 700px;
  width: 90%;
  padding: 20px;
  margin: 20px;
}

.save-slots {
  width: 100%;
  max-height: 90vh;
  overflow-y: auto;
  overflow-x: visible;
}

.sidebar-title {
  font-family: 'Press Start 2P', cursive;
  text-align: center;
  margin-bottom: 20px;
  font-size: 1.5em;
  border-bottom: 2px solid #c2a368;
  padding-bottom: 10px;
  color: #dac9a6;
  text-shadow: 1px 1px 2px #000;
}

.slots-grid {
  display: grid;
  grid-template-columns: 1fr;
  gap: 20px;
  overflow: visible;
}

.save-slot {
  background: rgba(57, 38, 25, 0.85);
  border: 2px solid #c2a368;
  border-radius: 10px;
  padding: 15px;
  cursor: pointer;
  transition: transform 0.3s ease, box-shadow 0.3s ease, background-color 0.3s ease;
  z-index: 100;
}

.save-slot:hover {
  position: relative;
  background: rgba(79, 56, 39, 0.85);
  box-shadow: 0 0 15px rgba(194, 163, 104, 0.6);
  z-index: 200;
}

.slot-content {
  display: flex;
  align-items: center;
  justify-content: space-between;
}

.town-info {
  display: flex;
  flex-direction: column;
}

.town-name {
  font-family: 'Press Start 2P', cursive;
  margin: 0;
  font-size: 1.2em;
  color: #dac9a6;
  text-shadow: 1px 1px 2px #000;
}

.town-date,
.town-info-detail {
  font-family: 'Press Start 2P', cursive;
  font-size: 0.8em;
  margin: 5px 0;
  color: #dac9a6;
  text-shadow: 1px 1px 2px #000;
}

.town-level-heroes {
  display: flex;
  align-items: center;
  gap: 4px;
  margin-top: 5px;
}

.hero-thumbs {
  display: flex;
  gap: 8px;
}

.hero-thumb {
  padding: 2px;
  border: 2px solid #c2a368;
  border-radius: 4px;
  background: rgba(79, 56, 39, 0.85);
  box-shadow: 0 0 6px rgba(194, 163, 104, 0.3);
  transition: transform 0.3s ease, box-shadow 0.3s ease;
}

.hero-thumb:hover {
  transform: scale(1.1);
  box-shadow: 0 0 12px rgba(194, 163, 104, 0.6);
}

.hero-thumb-img {
  width: 32px;
  height: 32px;
  object-fit: cover;
  border-radius: 2px;
  display: block;
  pointer-events: none;
}

.delete-button {
  background: #aa3333;
  color: #fff;
  border: none;
  border-radius: 5px;
  padding: 5px 10px;
  font-family: 'Press Start 2P', cursive;
  cursor: pointer;
  transition: background 0.3s ease;
  margin-left: 10px;
}

.delete-button:hover {
  background: #ff5555;
}

.empty-slot {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  height: 100px;
  font-family: 'Press Start 2P', cursive;
  font-size: 1em;
  color: #dac9a6;
  text-align: center;
  border: 2px dashed #c2a368;
  border-radius: 10px;
  text-shadow: 1px 1px 2px #000;
}

.create-prompt {
  font-size: 0.8em;
  margin-top: 5px;
  color: #c2a368;
  text-shadow: 1px 1px 2px #000;
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
  background: rgba(36, 21, 11, 0.8);
  border: 2px solid #c2a368;
  border-radius: 10px;
  padding: 30px;
  width: 480px;
  text-align: center;
  box-shadow: 0 0 20px rgba(194, 163, 104, 0.8);
  color: #dac9a6;
  font-family: 'Press Start 2P', cursive;
  text-shadow: 1px 1px 2px #000;
}

.modal-input {
  width: 100%;
  padding: 10px;
  margin: 20px 0;
  border: 2px solid #333;
  border-radius: 10px;
  font-family: 'Press Start 2P', cursive;
  font-size: 1em;
  background: #dac9a6;
  color: #333;
}

.modal-buttons {
  display: flex;
  justify-content: space-between;
}

.modal-submit,
.modal-cancel {
  background: #333;
  color: #dac9a6;
  border: 2px solid #c2a368;
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
  background: rgba(36, 21, 11, 0.9);
  transform: scale(1.05);
}
</style>
