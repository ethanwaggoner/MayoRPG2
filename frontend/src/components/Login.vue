<script setup>
import { ref, reactive } from 'vue'
import { useUserStore } from "@/stores/UserStore.js";
import router from "@/router.js";

const isSubmitting = ref(false)
const userStore = useUserStore();

const formData = reactive({
  email: '',
  password: ''
})

const errors = reactive({
  email: '',
  password: ''
})

const validateEmail = () => {
  const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/
  if (!formData.email) {
    errors.email = 'Email is required'
  } else if (!emailRegex.test(formData.email)) {
    errors.email = 'Please enter a valid email'
  } else {
    errors.email = ''
  }
}

const validatePassword = () => {
  if (!formData.password) {
    errors.password = 'Password is required'
  } else {
    errors.password = ''
  }
}

const validateForm = () => {
  validateEmail()
  validatePassword()
  return !errors.email && !errors.password
}

const handleSubmit = async () => {
  if (!validateForm()) return
  try {
    isSubmitting.value = true

    await userStore.login({
      email: formData.email,
      password: formData.password
    })
    await router.push({ name: "NewTownName" })
  } catch (error) {
    console.error('Login error:', error)
  } finally {
    isSubmitting.value = false
  }
}
</script>

<template>
  <div class="login-container">
    <div class="login-box">
      <h1>Welcome Back</h1>
      <p class="subtitle">Please log in to your account</p>
      <form @submit.prevent="handleSubmit" class="login-form">
        <div class="form-group" :class="{ 'error': errors.email }">
          <img src="../assets/items/tile085.png" alt="Email" class="input-icon">
          <input
              type="email"
              v-model="formData.email"
              placeholder="Email"
              @blur="validateEmail"
          >
          <span class="error-message">{{ errors.email }}</span>
        </div>

        <div class="form-group" :class="{ 'error': errors.password }">
          <img src="../assets/items/tile085.png" alt="Password" class="input-icon">
          <input
              type="password"
              v-model="formData.password"
              placeholder="Password"
              @blur="validatePassword"
          >
          <span class="error-message">{{ errors.password }}</span>
        </div>

        <button type="submit" class="submit-btn" :disabled="isSubmitting">
          {{ isSubmitting ? 'Logging In...' : 'Login' }}
        </button>
      </form>

      <p class="signup-link">
        Don't have an account? <a href="/sign-up">Sign up here</a>
      </p>
    </div>
  </div>
</template>

<style>
.login-container,
.signup-container {
  min-height: 100vh;
  display: flex;
  justify-content: center;
  align-items: center;
  padding: 20px;
  background: rgba(18, 18, 18, 0.8);
  backdrop-filter: blur(5px);
}

.login-box,
.signup-box {
  background: rgba(18, 18, 18, 0.8);
  border-radius: 16px;
  color: #f8facc;
  font-family: 'Press Start 2P', cursive;
  padding: 40px;
  width: 100%;
  max-width: 480px;
  box-shadow: 0 8px 32px rgba(0, 0, 0, 0.1);
  border: 1px solid rgba(255, 255, 255, 0.1);
  scale: .8;
}

h1 {
  color: #fff;
  font-size: 2rem;
  margin: 0 0 8px;
  text-align: center;
  font-weight: 700;
}

.subtitle {
  color: #b8b9cf;
  text-align: center;
  margin-bottom: 32px;
}

.login-form {
  display: flex;
  flex-direction: column;
  gap: 20px;
}

.form-group {
  position: relative;
}

.input-icon {
  position: absolute;
  left: 12px;
  top: 50%;
  transform: translateY(-50%);
  width: 20px;
  height: 20px;
  opacity: 0.7;
}

input {
  width: 100%;
  padding: 12px 40px;
  border-radius: 8px;
  border: 1px solid rgba(255, 255, 255, 0.1);
  background-color: rgba(255, 255, 255, 0.05);
  color: #fff;
  font-size: .8rem;
  transition: border-color 0.2s, box-shadow 0.2s;
}

input::placeholder {
  color: #b8b9cf;
}

input:focus {
  outline: none;
  border-color: #5c6bc0;
  box-shadow: 0 0 0 2px rgba(92, 107, 192, 0.2);
}

.error input {
  border-color: #ff5252;
}

.error-message {
  color: #ff5252;
  font-size: 0.8rem;
  margin-top: 4px;
  display: block;
}

.submit-btn {
  background: linear-gradient(135deg, #5c6bc0 0%, #3f51b5 100%);
  color: #fff;
  padding: 14px;
  border-radius: 8px;
  border: none;
  font-size: .8rem;
  font-weight: 600;
  cursor: pointer;
  transition: transform 0.2s, box-shadow 0.2s;
}

.submit-btn:hover:not(:disabled) {
  transform: translateY(-2px);
  box-shadow: 0 4px 12px rgba(92, 107, 192, 0.2);
}

.submit-btn:disabled {
  opacity: 0.7;
  cursor: not-allowed;
}

.signup-link {
  text-align: center;
  margin-top: 24px;
  color: #b8b9cf;
}

.signup-link a {
  color: #5c6bc0;
  text-decoration: none;
  font-weight: 500;
}

.signup-link a:hover {
  text-decoration: underline;
}
</style>
