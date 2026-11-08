<template>
  <component :is="currentView" />
</template>

<script setup>
import { computed, onMounted } from 'vue';
import { useAuthStore } from './stores/auth';
import AuthView from './views/AuthView.vue';
import HomeView from './views/HomeView.vue';

const authStore = useAuthStore();

onMounted(() => {
  if (authStore.token) {
    authStore.fetchUser();
  }
});

const currentView = computed(() => {
  return authStore.token ? HomeView : AuthView;
});
</script>