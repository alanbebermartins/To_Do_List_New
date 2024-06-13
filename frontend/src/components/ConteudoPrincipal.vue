<script lang="ts">
import Vue from 'vue';
import CreateEdit from './CreateEdit.vue';
import ListTasks from './ListTasks.vue';
import NavigationBar from './NavigationBar.vue';

export default Vue.extend({
  components: {
    CreateEdit,
    ListTasks,
    NavigationBar
  },
  data() {
    return {
      showCreateEdit: false
    };
  },
  methods: {
    showCreateEditView() {
      this.showCreateEdit = true;
    },
    hideCreateEditView() {
      this.showCreateEdit = false;
    }
  }
});
</script>

<template>
  <div>
    <!-- Inclui o NavigationBar e ouve os eventos emitidos -->
    <NavigationBar 
      @show-task-list="hideCreateEditView" 
      @show-create-edit="showCreateEditView" 
    />

    <!-- Usa v-if e v-else para exibir os componentes com base no estado -->
    <ListTasks 
      v-if="!showCreateEdit" 
      @editar="showCreateEditView"
    />
    <CreateEdit v-else 
      @salvar="hideCreateEditView" 
      @cancelar="hideCreateEditView"
    />
  </div>
</template>
    