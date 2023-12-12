<script setup lang="ts">
import { IColumn, IContainer, IRow } from '@inkline/inkline'
import { Ref, ref } from 'vue'
import { useRoute } from 'vue-router'

import { getBook } from '@/api'
import { Book } from '@/interfaces.ts'

const route = useRoute()
const book: Ref<Book | null> = ref(null)

const loadBook = async () => {
  book.value = await getBook(route.params.id as string)
}

loadBook()
</script>

<template>
  <IContainer>

    {{ book }}
  </IContainer>
</template>

<style scoped></style>
