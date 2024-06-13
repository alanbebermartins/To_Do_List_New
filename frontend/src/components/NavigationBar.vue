<script lang="ts">
import Vue from 'vue';

export default Vue.extend({
  methods: {
    showTaskList() {
      this.$emit('show-task-list');
    },
    showCreateEdit() {
      this.$emit('show-create-edit');
    }
  }
});
</script>

<template>
  <div class="row p-2">
    <div class="text-center col-sm-6 order-sm-1 d-sm-flex justify-content-sm-center mb-2 mb-sm-0">
      <a class="navigation-bar-options-item" @click="showTaskList">Lista de tarefas</a>
    </div>
    <div class="text-center col-sm-6 order-sm-2 d-sm-flex justify-content-sm-center">
      <a class="navigation-bar-options-item" @click="showCreateEdit">Criar/Editar tarefas</a>
    </div>
  </div>
</template>

<style scoped>
  .navigation-bar-options-item {
    cursor: pointer;
    font-size: 18px;
    font-weight: bold;
    color: white;
  }
</style>
