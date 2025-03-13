<template>
  <div>
    <h1>Hello World</h1>
    <button @click="testConnection">Tester la connexion Backend</button>
  </div>
</template>

<script setup lang="ts">
import axios from 'axios';

const testConnection = async () => {
  try {
    const res = await axios.get('/api/test');
    alert(res.data.message);
  } catch (error) {
    alert('Erreur de connexion backend');
  }
};
</script>
