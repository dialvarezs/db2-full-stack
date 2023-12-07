<script setup lang="ts">
import { reactive, computed } from 'vue'
import { Author, Book } from '../interfaces'
import { IRow } from '@inkline/inkline'
import { getAuthors, postBook } from '../api'
import { useRouter } from 'vue-router'

const router = useRouter()
const book: Book = reactive({
  title: '',
  description: '',
  language: '',
  isbn: '',
  year: null,
  authorId: null,
  categories: []
})
const authors: Author[] = reactive([])
const authorOptions = computed(() => {
  return authors.map((x) => ({ id: x.id, label: x.name }))
})

const loadAuthors = async () => {
  Object.assign(authors, await getAuthors())
}
const saveBook = async () => {
  book.year = parseInt(String(book.year))
  await postBook(book)
  await router.push({ name: 'Home' })
}

loadAuthors()
</script>

<template>
  <IContainer class="_margin-top:2!">
    <IRow center>
      <IColumn xs="6">
        <IForm>
          <IFormGroup>
            <FormLabel>Título</FormLabel>
            <IInput v-model="book.title"></IInput>
          </IFormGroup>
          <IFormGroup>
            <FormLabel>Descripción</FormLabel>
            <ITextarea v-model="book.description"></ITextarea>
          </IFormGroup>
          <IFormGroup>
            <FormLabel>Idioma</FormLabel>
            <IInput v-model="book.language"></IInput>
          </IFormGroup>
          <IFormGroup>
            <FormLabel>ISBN</FormLabel>
            <IInput v-model="book.isbn"></IInput>
          </IFormGroup>
          <IFormGroup>
            <FormLabel>Año</FormLabel>
            <INumberInput v-model="book.year"></INumberInput>
          </IFormGroup>
          <IFormGroup>
            <FormLabel>Autor</FormLabel>
            <ISelect v-model="book.authorId" :options="authorOptions"></ISelect>
          </IFormGroup>
          <IFormGroup>
            <IButtonGroup block>
              <IButton color="primary" @click="saveBook"> Guardar </IButton>
              <IButton color="gray" :to="{ name: 'Home' }"> Cancelar </IButton>
            </IButtonGroup>
          </IFormGroup>
        </IForm>
      </IColumn>
    </IRow>
  </IContainer>
</template>
