<template>
  <div>
    <p>{{ todos }}</p>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'Ping',
  data() {
    return {
      todos: '',
    };
  },
  methods: {
    getMessage() {
      const path = 'http://localhost:8000';
      axios.get(path)
        .then((res) => {
          this.todos = res.data;
        })
        .catch((error) => {

          console.error(error);
        });
    },
  },
  created() {
    this.getMessage();
  },
};
</script>
