<script setup lang="ts">
import {
  IButton,
  IButtonGroup,
  IColumn,
  IContainer,
  IForm,
  IFormGroup,
  IFormLabel,
  IInput,
  INumberInput,
  IRow,
  ISelect,
  ITextarea
} from '@inkline/inkline'
import { computed, reactive } from 'vue'
import { useRouter } from 'vue-router'

import { getAuthors, postBook } from '../api'
import { Author, Book } from '../interfaces'

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
            <IFormLabel>Título</IFormLabel>
            <IInput v-model="book.title"></IInput>
          </IFormGroup>
          <IFormGroup>
            <IFormLabel>Descripción</IFormLabel>
            <ITextarea v-model="book.description"></ITextarea>
          </IFormGroup>
          <IFormGroup>
            <IFormLabel>Idioma</IFormLabel>
            <IInput v-model="book.language"></IInput>
          </IFormGroup>
          <IFormGroup>
            <IFormLabel>ISBN</IFormLabel>
            <IInput v-model="book.isbn"></IInput>
          </IFormGroup>
          <IFormGroup>
            <IFormLabel>Año</IFormLabel>
            <INumberInput v-model="book.year"></INumberInput>
          </IFormGroup>
          <IFormGroup>
            <IFormLabel>Autor</IFormLabel>
            <ISelect v-model="book.authorId" :options="authorOptions"></ISelect>
          </IFormGroup>
          <IFormGroup class="_margin-top:3!">
            <IButtonGroup block>
              <IButton color="primary" @click="saveBook">Guardar</IButton>
              <IButton color="gray" :to="{ name: 'Home' }">Cancelar</IButton>
            </IButtonGroup>
          </IFormGroup>
        </IForm>
      </IColumn>
    </IRow>
  </IContainer>
</template>
