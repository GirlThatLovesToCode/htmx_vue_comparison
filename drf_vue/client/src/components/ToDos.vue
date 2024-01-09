<template>
  <div class="container">
    <div v-for="(todo, index) in todos" :key="index">
      {{ todo.name }}
      <button>Done</button>
    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      todos: [],
    };
  },
  methods: {
    getTodos() {
      const path = 'http://localhost:8000/';
      axios.get(path)
          .then((res) => {
            this.todos = res.data;
          })
          .catch((error) => {
            console.error(error);
          });
    },
    newTodo(payload) {
      const path = 'http://localhost:8000/';
      axios.post(path, payload)
          .then(() => {
            this.getTodos();
          })
          .catch((error) => {
            console.log(error);
            this.getTodos();
          });
    },
  }
}
,
created()
{
  this.getTodos();
}
,
}
;
</script>