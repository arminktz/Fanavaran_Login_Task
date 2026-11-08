<template>
  <div class="min-h-screen flex items-center justify-center bg-gray-50 p-4" dir="rtl">
    <div class="w-full max-w-md bg-white rounded-2xl shadow-xl p-8 border border-gray-100">
      
      <div class="text-center mb-6">
        <h2 class="text-2xl font-bold text-gray-800">سامانه احراز هویت</h2>
        <p class="text-sm text-gray-500 mt-1">لطفاً وارد حساب کاربری خود شوید یا ثبت‌نام کنید</p>
      </div>

      <!-- Tabs Header -->
      <div class="flex bg-gray-100 p-1 rounded-xl mb-6">
        <button 
          @click="isLogin = true; errorMsg = ''"
          :class="['w-1/2 py-2.5 text-sm font-medium rounded-lg transition-all', isLogin ? 'bg-white text-blue-600 shadow-sm' : 'text-gray-500 hover:text-gray-700']">
          ورود
        </button>
        <button 
          @click="isLogin = false; errorMsg = ''"
          :class="['w-1/2 py-2.5 text-sm font-medium rounded-lg transition-all', !isLogin ? 'bg-white text-blue-600 shadow-sm' : 'text-gray-500 hover:text-gray-700']">
          ثبت‌نام
        </button>
      </div>

      <!-- Alert Error -->
      <div v-if="errorMsg" class="bg-red-50 border border-red-200 text-red-600 p-3 rounded-xl text-sm mb-4">
        {{ errorMsg }}
      </div>

      <!-- Form -->
      <form @submit.prevent="handleSubmit" class="space-y-4">
        <div v-if="!isLogin">
          <label class="block text-sm font-medium text-gray-700 mb-1">نام کامل</label>
          <input 
            v-model="form.fullName" 
            type="text" 
            required 
            class="w-full px-4 py-2.5 bg-gray-50 border border-gray-200 rounded-xl focus:bg-white focus:ring-2 focus:ring-blue-500 focus:outline-none transition-all" 
            placeholder="مثال: علی محمدی" 
          />
        </div>

        <div>
          <label class="block text-sm font-medium text-gray-700 mb-1">ایمیل</label>
          <input 
            v-model="form.email" 
            type="email" 
            required 
            class="w-full px-4 py-2.5 bg-gray-50 border border-gray-200 rounded-xl focus:bg-white focus:ring-2 focus:ring-blue-500 focus:outline-none transition-all" 
            placeholder="name@example.com" 
          />
        </div>

        <div>
          <label class="block text-sm font-medium text-gray-700 mb-1">رمز عبور</label>
          <input 
            v-model="form.password" 
            type="password" 
            required 
            class="w-full px-4 py-2.5 bg-gray-50 border border-gray-200 rounded-xl focus:bg-white focus:ring-2 focus:ring-blue-500 focus:outline-none transition-all" 
            placeholder="••••••••" 
          />
        </div>

        <button 
          type="submit" 
          :disabled="loading"
          class="w-full bg-blue-600 hover:bg-blue-700 text-white font-medium py-3 rounded-xl transition-all shadow-lg shadow-blue-500/25 disabled:opacity-50">
          <span v-if="loading">در حال پردازش...</span>
          <span v-else>{{ isLogin ? 'ورود به حساب' : 'تکمیل ثبت‌نام' }}</span>
        </button>
      </form>

    </div>
  </div>
</template>

<script setup>
import { ref, reactive } from 'vue';
import { useAuthStore } from '../stores/auth';

const authStore = useAuthStore();

const isLogin = ref(true);
const loading = ref(false);
const errorMsg = ref('');

const form = reactive({
  email: '',
  password: '',
  fullName: ''
});

const handleSubmit = async () => {
  loading.value = true;
  errorMsg.value = '';

  try {
    if (isLogin.value) {
      await authStore.login(form.email, form.password);
      alert('ورود با موفقیت انجام شد! توکن ذخیره شد.');
    } else {
      await authStore.register(form.email, form.password, form.fullName);
      alert('ثبت‌نام با موفقیت انجام شد. حالا می‌توانید وارد شوید.');
      isLogin.value = true;
    }
  } catch (err) {
    errorMsg.value = err.response?.data?.detail || 'خطایی رخ داد. مجدداً تلاش کنید.';
  } finally {
    loading.value = false;
  }
};
</script>