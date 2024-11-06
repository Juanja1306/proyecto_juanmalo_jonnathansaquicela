<template>
  <div id="app">
    <h1>Frontend with Vue.js</h1>
    <button @click="fetchData">Get Backend Data</button>
    <p>{{ message }}</p>
  </div>
</template>

<script>
export default {
  data() {
    return {
      message: '',
    };
  },
  methods: {
    async fetchData() {
      const response = await fetch(`${process.env.VUE_APP_API_URL}/api/message`);
      const data = await response.json();
      this.message = data.message;
    },
  },
};
</script>

<style scoped>
#app {
  text-align: center;
}
</style>
