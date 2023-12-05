<script setup lang="ts">
import { reactive } from 'vue';
import { getBooks } from '../api';
import { Book } from '../interfaces';

const books: Book[] = reactive([])

const loadBooks = async () => {
    Object.assign(books, await getBooks())
}

loadBooks()
</script>

<template>
    <IContainer class="_margin-top:2!">
        <IRow>
            <IColumn class="_display:flex! _justify-content:end!">
                <IButton color="primary" :to="{name: 'NewBook'}">
                    <template #icon>
                        <IIcon name="ink-plus" />
                    </template>
                    Nuevo libro
                </IButton>
            </IColumn>
        </IRow>
        <IRow class="_margin-top:1!">
            <IColumn v-for="book in books" :key="book.id" xs="6">
                <ICard>
                    <h2 class="_color:primary!">{{ book.title }}</h2>
                    <p>{{ book.description }}</p>
                    <p class="_color:gray!">{{ book.author?.name }}</p>
                </ICard>
            </IColumn>
        </IRow>
    </IContainer>
</template>