import { defineStore } from 'pinia';
import apiService from "@/api/apiService.js";

export const useUserStore = defineStore('userStore', {
  state: () => ({
    user: null,
  }),
  getters: {
    isAuthenticated(state) {
      return !!state.user;
    }
  },
  actions: {
    async signup({ email, username, password }) {
      try {
        const response = await apiService.post('/api/auth/signup', { email, username, password });
        return response.data;
      } catch (error) {
        console.error('Signup failed:', error);
        throw error;
      }
    },

    async login({ email, password }) {
      try {
        const response = await apiService.post('/api/auth/login', { email, password });
        this.user = response.data || null;
        return response.data;
      } catch (error) {
        console.error('Login failed:', error);
        throw error;
      }
    },

    async fetchCurrentUser() {
      try {
        const response = await apiService.get('/api/auth/current_user');
        this.user = response.data;
      } catch (error) {
        console.error('Failed to fetch current user:', error);
        this.user = null;
      }
    },

    async logout() {
      try {
        await apiService.post('/api/auth/logout');
      } catch (error) {
        console.error('Logout API call failed:', error);
      } finally {
        this.user = null;
      }
    }
  }
});
