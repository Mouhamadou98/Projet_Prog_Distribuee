<template>
  <div id="app">
    <header>
      <div style="text-align: center; font-weight: bold; font-size: 30px;">
        Projet de Programmation Distribuée M1 AMSD <br>Auteurs : GNING Mouhamadou Lamine & SAMB Mouhamed
      </div>
      <router-link to="/"><button class="btn btn-success btn-sm">Students</button></router-link>
      <router-link to="/absences"><button class="btn btn-success btn-sm" style="margin: 10px ;">Absences</button></router-link>
    </header>
  </div>
  <RouterView />
</template>

<script setup>
import { RouterView } from 'vue-router'
</script>
<style>
/* Styles pour votre en-tête ici */
header {
  background-color: #f0f0f0;
  padding: 10px;
  /* text-align: center; */
}

</style>
