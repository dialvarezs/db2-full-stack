import { camelCase, snakeCase } from 'change-case/keys'

import { Author, Book } from './interfaces'

const baseUrl = 'http://127.0.0.1:8000'

async function getBooks(): Promise<Book[]> {
  const response = await fetch(`${baseUrl}/books`)
  return camelCase(await response.json(), 3) as Book[]
}

async function postBook(book: Book) {
  const response = await fetch(`${baseUrl}/books`, {
    method: 'POST',
    body: JSON.stringify(snakeCase(book))
  })
  return response.json()
}

async function getAuthors(): Promise<Author[]> {
  const response = await fetch(`${baseUrl}/authors`)
  return camelCase(await response.json(), 3) as Author[]
}

async function postAuthor(author: Author) {
  const response = await fetch(`${baseUrl}/authors`, {
    method: 'POST',
    body: JSON.stringify(snakeCase(author))
  })
  return response.json()
}

export { getBooks, getAuthors, postBook, postAuthor }
