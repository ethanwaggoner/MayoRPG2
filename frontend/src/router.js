import { createWebHistory, createRouter }  from 'vue-router';
import {useUserStore} from "@/stores/UserStore.js";

const routes = [
    {
        path: '/',
        name: 'LandingPage',
        component: () => import('@/views/LandingPageView.vue')
    },
    {
        path: '/start',
        name: 'StartPage',
        component: () => import('@/views/StartPageView.vue')
    },
    {
        path: '/choose-hero',
        name: 'ChooseHero',
        component: () => import('@/views/NewChooseHeroView.vue'),
        meta: { requiresAuth: true }
    },
    {
        path: '/new-town-name',
        name: 'NewTownName',
        component: () => import('@/views/NewTownNameView.vue'),
        meta: { requiresAuth: true }
    },
    {
        path: '/choose-hero-class',
        name: 'ChooseHeroClass',
        component: () => import('@/views/NewChooseHeroClassView.vue'),
        meta: { requiresAuth: true }
    },
    {
        path: '/main-page',
        name: 'MainPage',
        component: () => import('@/views/MainPageView.vue'),
        meta: { requiresAuth: true }

    },
    {
        path: '/sign-up',
        name: 'SignUp',
        component: () => import('@/views/SignUpView.vue')
    },
    {
        path: '/login',
        name: 'Login',
        component: () => import('@/views/LoginView.vue')
    },
    {
        path: '/alchemist',
        name: 'Alchemist',
        component: () => import('@/views/AlchemistView.vue'),
        meta: { requiresAuth: true }
    },
    {
        path: '/news',
        name: 'News',
        component: () => import('@/views/NewsPageView.vue'),
    }
]

const router = createRouter({
    history: createWebHistory(),
    routes
});

router.beforeEach(async (to, from, next) => {
    if (to.meta.requiresAuth) {
        const userStore = useUserStore();

        if (!userStore.isAuthenticated) {
            try {
                await userStore.fetchCurrentUser();
            } catch (error) {
                console.error('Error fetching user:', error);
            }
        }
        if (!userStore.isAuthenticated) {
            return next({ name: 'Login' });
        } else {
        }
    }
    next();
});


export default router;