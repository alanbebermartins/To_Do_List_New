<script lang="ts">
import Vue from 'vue';
import { createTask } from '@/api'; 

export default Vue.extend({
  data() {
    return {
      form: {
        title: '',
        description: ''
      }
    };
  },
  methods: {
    salvar() {
      // Emitir evento para o componente pai
      this.$emit('salvar', this.form);
    },
    cancelar() {
      this.$emit('cancelar');
    },
    async salvarTarefa() {
      try {
        // Chamar a função createTask para criar a tarefa
        const data = await createTask(this.form.title, this.form.description);
        console.log('Tarefa criada com sucesso:', data);
        // Limpar formulário ou tomar outra ação necessária após salvar
        this.form.title = '';
        this.form.description = '';
      } catch (error) {
        console.error('Erro ao criar tarefa:', error.message);
        // Tratar erro, exibir mensagem de erro, etc.
      }
    }
  }
});
</script>


<template>
    <section>
        <form class="create-and-edit-tasks" @submit.prevent="salvarTarefa">
            <div class="form-group">
                <span for="input-field-task-title">Título da tarefa</span>
                <input v-model="form.title" type="text" class="form-control" maxlength="20" id="input-field-task-title">
            </div>
            <div class="form-group">
                <span for="input-field-task-description">Descrição da tarefa</span>
                <textarea v-model="form.description" class="form-control" rows="3" maxlength="100" id="input-field-task-description"></textarea>
            </div>
            <div class="d-flex align-items-center justify-content-around d-md-flex align-items-md-center justify-content-md-end">
                <div>
                    <button type="button" class="btn btn-sm btn-primary" @click="salvar">SALVAR</button>
                </div>
                <div>
                    <button type="button" class="btn btn-sm btn-danger" @click="cancelar">CANCELAR</button>
                </div>
            </div>
        </form>
    </section>
</template>

<style>
    .create-and-edit-tasks {
        max-width: 80%;
        margin: 30px auto;
    }
</style>