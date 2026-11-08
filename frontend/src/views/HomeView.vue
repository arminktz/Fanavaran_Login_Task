<template>
  <div class="min-h-screen bg-gray-50 flex flex-col" dir="rtl">
    <!-- Navbar -->
    <header class="bg-white border-b border-gray-100 shadow-xs">
      <div class="max-w-7xl mx-auto px-6 h-20 flex items-center justify-between">
        <div class="flex items-center gap-3">
          <div class="w-10 h-10 rounded-xl bg-blue-600 flex items-center justify-center text-white font-bold text-lg shadow-md shadow-blue-500/20">
            {{ userInitial }}
          </div>
          <div>
            <h1 class="font-bold text-gray-800 text-lg">داشبورد کاربری</h1>
            <p class="text-xs text-gray-400">سامانه مدیریت یکپارچه</p>
          </div>
        </div>
        
        <button 
          @click="handleLogout"
          class="flex items-center gap-2 px-4 py-2 bg-red-50 hover:bg-red-100 text-red-600 font-medium text-sm rounded-xl transition-all">
          <svg class="w-4 h-4" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" d="M17 16l4-4m0 0l-4-4m4 4H7m6 4v1a3 3 0 01-3 3H6a3 3 0 01-3-3V7a3 3 0 013-3h4a3 3 0 013 3v1"></path>
          </svg>
          خروج از حساب
        </button>
      </div>
    </header>

    <!-- Main Content -->
    <main class="flex-1 max-w-7xl w-full mx-auto p-6 md:p-10">
      <!-- Welcome Banner -->
      <div class="bg-gradient-to-r from-blue-600 to-indigo-700 rounded-3xl p-8 md:p-12 text-white shadow-xl shadow-blue-500/20 relative overflow-hidden mb-8">
        <div class="relative z-10">
          <span class="inline-block px-3.5 py-1.5 bg-white/10 backdrop-blur-md rounded-full text-xs font-medium mb-4">
            حساب کاربری فعال
          </span>
          <h2 class="text-3xl md:text-4xl font-extrabold mb-3">
            سلام، {{ authStore.user?.full_name || 'کاربر عزیز' }}! 👋
          </h2>
          <p class="text-blue-100 text-sm md:text-base max-w-xl leading-relaxed">
            از اینکه به سامانه ما برگشتید خوشحالیم. از طریق پنل خود می‌توانید به تمامی امکانات سیستم دسترسی داشته باشید.
          </p>
        </div>
        <!-- Decorative Circle -->
        <div class="absolute -left-10 -bottom-10 w-64 h-64 bg-white/10 rounded-full blur-2xl pointer-events-none"></div>
      </div>

      <!-- Info Cards Grid -->
      <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
        <div class="bg-white p-6 rounded-2xl border border-gray-100 shadow-sm flex items-center gap-4">
          <div class="w-12 h-12 rounded-xl bg-blue-50 text-blue-600 flex items-center justify-center font-bold text-xl">
            📧
          </div>
          <div>
            <p class="text-xs text-gray-400 font-medium">ایمیل ثبت‌شده</p>
            <p class="text-gray-800 font-bold mt-0.5">{{ authStore.user?.email }}</p>
          </div>
        </div>

        <div class="bg-white p-6 rounded-2xl border border-gray-100 shadow-sm flex items-center gap-4">
          <div class="w-12 h-12 rounded-xl bg-emerald-50 text-emerald-600 flex items-center justify-center font-bold text-xl">
            🛡️
          </div>
          <div>
            <p class="text-xs text-gray-400 font-medium">وضعیت حساب</p>
            <p class="text-emerald-600 font-bold mt-0.5">فعال و تایید شده</p>
          </div>
        </div>
      </div>
    </main>
  </div>
</template>

<script setup>
import { computed, onMounted } from 'vue';
import { useAuthStore } from '../stores/auth';

const authStore = useAuthStore();

onMounted(async () => {
  if (!authStore.user) {
    await authStore.fetchUser();
  }
});

const userInitial = computed(() => {
  const name = authStore.user?.full_name || authStore.user?.email || 'U';
  return name.charAt(0).toUpperCase();
});

const handleLogout = () => {
  authStore.logout();
};
</script>