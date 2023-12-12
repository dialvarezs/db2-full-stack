<script setup lang="ts">
import { ILayout, ILayoutContent, ILayoutHeader } from '@inkline/inkline'

import Header from './components/Header.vue'
</script>

<template>
  <ILayout>
    <ILayoutHeader>
      <Header></Header>
    </ILayoutHeader>
    <ILayoutContent class="_padding-top:2!">
      <RouterView></RouterView>
    </ILayoutContent>
  </ILayout>
</template>

<style scoped></style>
