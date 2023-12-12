export interface Book {
  id?: number
  isbn: string
  title: string
  description: string
  year: number | null
  language: string
  authorId: number | null
  author?: Author
  categories?: Category[] | number[]
}

export interface Author {
  id?: number
  name: string
  bibliography: string | null
  dateOfBirth: string | null
}

export interface Category {
  id?: number
  name?: string
}
