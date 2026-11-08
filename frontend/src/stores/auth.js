import { defineStore } from 'pinia';
import axios from 'axios';

const API_URL = 'http://localhost:8000/api/v1/auth';

export const useAuthStore = defineStore('auth', {
  state: () => ({
    token: localStorage.getItem('token') || null,
    user: null,
  }),
  actions: {
    async login(email, password) {
      const formData = new FormData();
      formData.append('username', email);
      formData.append('password', password);

      const res = await axios.post(`${API_URL}/login`, formData);
      this.token = res.data.access_token;
      localStorage.setItem('token', this.token);
      await this.fetchUser();
    },
    async register(email, password, fullName) {
      await axios.post(`${API_URL}/register`, {
        email,
        password,
        full_name: fullName,
      });
    },
    async fetchUser() {
      if (!this.token) return;
      try {
        const res = await axios.get(`${API_URL}/me`, {
          headers: { Authorization: `Bearer ${this.token}` }
        });
        this.user = res.data;
      } catch (err) {
        this.logout();
      }
    },
    logout() {
      this.token = null;
      this.user = null;
      localStorage.removeItem('token');
    }
  }
});