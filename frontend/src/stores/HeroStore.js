import { defineStore } from 'pinia';
import apiService from "@/api/apiService.js";
import { Hero } from "@/game/hero.js";
import { useTownStore} from "@/stores/TownStore.js";

const townStore = useTownStore();


export const useHeroStore = defineStore('heroStore', {
  state: () => ({
    heroes: [],
    selectedHero: null,
    HeroGroup1: [],
    HeroGroup2: [],
  }),
  getters: {
    heroById: (state) => (id) => state.heroes.find(hero => hero.id === id)
  },
  actions: {
    async loadInitialHeroData(){
      try {
        const response = await apiService.get('/api/initial_hero/hero_stats');
        this.heroes = response.data
      } catch (error) {
        console.error('Error loading initial hero data:', error);
      }
    },
    async loadHeroData(townUuid) {
      try {
        const response = await apiService.get(`/api/heroes/${townUuid}/`);
        this.HeroGroup1 = response.data.filter(hero => hero.heroGroup === 1).map(hero => new Hero(hero));
        this.HeroGroup2 = response.data.filter(hero => hero.heroGroup === 2).map(hero => new Hero(hero));
      } catch (error) {
        console.error('Error loading hero data:', error);
      }
    },
    async createHero(townUuid, heroData) {
      console.log(heroData)
      try {
        const response = await apiService.post(`/api/heroes/${townUuid}/`, heroData);
        return response.data;
      } catch (error) {
        console.error('Error creating hero:', error);
        throw error;
      }
    },
    selectHero(heroName) {
      const heroData = this.heroes.find(hero => hero.name === heroName);
      if (!heroData) {
        console.error('Hero data not found');
        return;
      }
      if (this.HeroGroup1.length < 5) {
        this.selectedHero = new Hero(heroData);
        this.selectedHero.heroGroup = 1;
      } else if (this.HeroGroup2.length < 5) {
        this.selectedHero = new Hero(heroData);
        this.selectedHero.heroGroup = 2;
      }
    },
    async confirmHeroSelection(groupNumber) {
      const townUuid = townStore.currentTown.uuid

      if (!this.selectedHero) {
        console.error("No hero selected to confirm.");
        return;
      }
      this.selectedHero.heroGroup = groupNumber;
      try {
        console.log(this.selectedHero)
        await this.createHero(townUuid, this.selectedHero);
        if (groupNumber === 1) {
          this.HeroGroup1.push(this.selectedHero);
        } else if (groupNumber === 2) {
          this.HeroGroup2.push(this.selectedHero);
        }
      } catch (error) {
        console.error('Error confirming hero selection:', error);
      }
      this.selectedHero = null;
    },
    clearHeroData() {
      localStorage.removeItem('HeroGroup1');
      localStorage.removeItem('HeroGroup2');
      this.HeroGroup1 = [];
      this.HeroGroup2 = [];
    },
  }
});
