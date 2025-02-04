import { defineStore } from 'pinia';
import apiService from '@/api/apiService.js';

export const useTownStore = defineStore('townStore', {
    state: () => ({
        towns: [],
        currentTown: JSON.parse(localStorage.getItem('currentTown')) || null,
    }),
    getters: {
        getTownByUuid: (state) => (uuid) => {
            return state.towns.find(town => town.uuid === uuid);
        },
        getCurrentTown: (state) => state.currentTown,
    },
    actions: {
        async loadTowns() {
          try {
            const response = await apiService.get('/api/towns/');
            this.towns = response.data;

            const storedTown = JSON.parse(localStorage.getItem('currentTown'));

            if (storedTown) {
              const foundTown = this.towns.find(town => town.uuid === storedTown.uuid);
              if (foundTown) {
                this.currentTown = foundTown;
              } else if (this.towns.length > 0) {
                this.currentTown = this.towns[0];
              }
            } else if (this.towns.length > 0) {
              this.currentTown = this.towns[0];
            }

            localStorage.setItem('currentTown', JSON.stringify(this.currentTown));
          } catch (error) {
            console.error('Error loading towns:', error);
          }
        },

        async createTown(townData) {
          try {
            const response = await apiService.post('/api/towns/', townData);
            this.towns.push(response.data);
            this.towns.sort((a, b) => new Date(b.created_at) - new Date(a.created_at));
            this.currentTown = response.data;
            localStorage.setItem('currentTown', JSON.stringify(this.currentTown));
          } catch (error) {
            console.error('Error creating town:', error);
          }
        },

       async deleteTown(townUuid) {
          try {
            await apiService.delete(`/api/towns/${townUuid}/`);
            this.towns = this.towns.filter(town => town.uuid !== townUuid);

            if (this.currentTown && this.currentTown.uuid === townUuid) {
              if (this.towns.length > 0) {
                this.currentTown = this.towns[0];
              } else {
                this.currentTown = null;
              }
              localStorage.setItem('currentTown', JSON.stringify(this.currentTown));
            }
          } catch (error) {
            console.error('Error deleting town:', error);
          }
        },
        async selectTown(townUuid) {
            try {
                const response = await apiService.get(`/api/towns/${townUuid}/`);
                this.currentTown = response.data;
                localStorage.setItem('currentTown', JSON.stringify(this.currentTown));
            } catch (error) {
                console.error('Error selecting town:', error);
            }
        },
    }
});
