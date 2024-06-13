<script lang="ts">
import Vue from 'vue';

export default Vue.extend({
  methods: {
    editarTarefa() {
      this.$emit('editar');
    }
  }
});
</script>

<template>
    <section>
        <div class="tasks-list-main-title text-enter">
            <span>Lista de tarefas existentes</span>
        </div>
        <div >
            <ul class="tasks-list">
                <li class="d-flex flex-column mb-4">
                    <div class="d-flex flex-column">
                        <span class="py-2">Reunião Inicial do Projeo</span>
                        <span class="py-2">Nessa reuinao será discutida como será desenvolvido o projeto, quem irá compor o projeto, tecnologias que serão utilizadas no projeto</span>
                    </div>
                    <div class="d-flex align-items-center justify-content-around d-md-flex align-items-md-center justify-content-md-end">
                        <div>
                            <button type="button" class="btn btn-sm btn-primary" id="button-to-edit" @click="editarTarefa">EDITAR</button>
                        </div>
                        <div>
                            <button type="button" class="btn btn-sm btn-danger" id="button-to-exlude">EXLUIR</button>
                        </div>
                    </div>
                </li>
                <li class="d-flex flex-column mb-4">
                    <div class="d-flex flex-column">
                        <span class="py-2">Montar Cronograma</span>
                        <span class="py-2">Montar o planejamento das tasks no jira, baseado no tamanho da equipe e tecnologias utlizadas</span>
                    </div>
                    <div class="d-flex align-items-center justify-content-around d-md-flex align-items-md-center justify-content-md-end">
                        <div>
                            <button type="button" class="btn btn-sm btn-primary" id="button-to-edit" @click="editarTarefa">EDITAR</button>
                        </div>
                        <div>
                            <button type="button" class="btn btn-sm btn-danger" id="button-to-exlude">EXLUIR</button>
                        </div>
                    </div>
                </li>
            </ul>
        </div>
    </section>
</template>

<style>
    .tasks-list-main-title {
        max-width: 80%;
        margin: 30px auto;
        font-size: 24px !important;
    }
    .tasks-list {
        max-width: 80%;
        margin: 30px auto;
        list-style-type: none;
    }
</style>