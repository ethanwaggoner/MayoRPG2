import { defineStore } from 'pinia';
import apiService from '@/api/apiService.js';

export const useTownStore = defineStore('townStore', {
    state: () => ({
        towns: [],
        currentTown: null,
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
            } catch (error) {
                console.error('Error loading towns:', error);
            }
        },
        async createTown(townData) {
            try {
                const response = await apiService.post('/api/towns/', townData);
                this.towns.push(response.data);
            } catch (error) {
                console.error('Error creating town:', error);
            }
        },
        async deleteTown(townUuid) {
            try {
                await apiService.delete(`/api/towns/${townUuid}/`);
                this.towns = this.towns.filter(town => town.uuid !== townUuid);
            } catch (error) {
                console.error('Error deleting town:', error);
            }
        },
        async selectTown(townUuid) {
            try {
                const response = await apiService.get(`/api/towns/${townUuid}/`);
                this.currentTown = response.data;
            } catch (error) {
                console.error('Error selecting town:', error);
            }
        },
    }
});
