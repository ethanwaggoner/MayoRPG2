<script setup>
import {ref, reactive} from 'vue'
import {useUserStore} from "@/stores/UserStore.js";
import router from "@/router.js";

const isSubmitting = ref(false)
const userStore = useUserStore();

const formData = reactive({
  email: '',
  username: '',
  password: '',
  confirmPassword: ''
})

const errors = reactive({
  email: '',
  username: '',
  password: '',
  confirmPassword: ''
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

const validateUsername = () => {
  if (!formData.username) {
    errors.username = 'Username is required'
  } else if (formData.username.length < 3) {
    errors.username = 'Username must be at least 3 characters'
  } else if (formData.username.length > 20) {
    errors.username = 'Username must be less than 20 characters'
  } else {
    errors.username = ''
  }
}

const validatePassword = () => {
  if (!formData.password) {
    errors.password = 'Password is required'
  } else if (formData.password.length < 8) {
    errors.password = 'Password must be at least 8 characters'
  } else if (!/(?=.*[A-Z])/.test(formData.password)) {
    errors.password = 'Password must contain at least one uppercase letter'
  } else if (!/(?=.*[0-9])/.test(formData.password)) {
    errors.password = 'Password must contain at least one number'
  } else {
    errors.password = ''
  }
}

const validateConfirmPassword = () => {
  if (!formData.confirmPassword) {
    errors.confirmPassword = 'Please confirm your password'
  } else if (formData.confirmPassword !== formData.password) {
    errors.confirmPassword = 'Passwords do not match'
  } else {
    errors.confirmPassword = ''
  }
}

const validateForm = () => {
  validateEmail()
  validateUsername()
  validatePassword()
  validateConfirmPassword()

  return (
      !errors.email &&
      !errors.username &&
      !errors.password &&
      !errors.confirmPassword
  )
}

const handleSubmit = async () => {
  if (!validateForm()) return
  try {
    isSubmitting.value = true

    await userStore.signup({
      email: formData.email,
      username: formData.username,
      password: formData.password
    })

    await router.push('/login')
  } catch (error) {
    console.error('Signup error:', error)
  } finally {
    isSubmitting.value = false
  }
}
</script>

<template>
  <div class="signup-container">
    <div class="signup-box">
      <h1>Join the Adventure</h1>
      <p class="subtitle">Create your account today!</p>
      <form @submit.prevent="handleSubmit" class="signup-form">
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

        <div class="form-group" :class="{ 'error': errors.username }">
          <img src="../assets/items/tile085.png" alt="Username" class="input-icon">
          <input
              type="text"
              v-model="formData.username"
              placeholder="Username"
              @blur="validateUsername"
          >
          <span class="error-message">{{ errors.username }}</span>
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

        <div class="form-group" :class="{ 'error': errors.confirmPassword }">
          <img src="../assets/items/tile085.png" alt="Confirm Password" class="input-icon">
          <input
              type="password"
              v-model="formData.confirmPassword"
              placeholder="Confirm password"
              @blur="validateConfirmPassword"
          >
          <span class="error-message">{{ errors.confirmPassword }}</span>
        </div>

        <button type="submit" class="submit-btn" :disabled="isSubmitting">
          {{ isSubmitting ? 'Creating Account...' : 'Begin Your Journey' }}
        </button>
      </form>

      <p class="login-link">
        Already have an account? <a href="/login">Login here</a>
      </p>
    </div>
  </div>
</template>

<style>

.signup-container {
  min-height: 100vh;
  display: flex;
  justify-content: center;
  align-items: center;
  padding: 20px;
  background: rgba(18, 18, 18, 0.8);
  backdrop-filter: blur(5px);
}

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

.signup-form {
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

.login-link {
  text-align: center;
  margin-top: 24px;
  color: #b8b9cf;
}

.login-link a {
  color: #5c6bc0;
  text-decoration: none;
  font-weight: 500;
}

.login-link a:hover {
  text-decoration: underline;
}
</style>
