module.exports = {
  'env': {
    'browser': true,
    'node': true,
    'es2021': true
  },
  'extends':
    ['eslint:recommended', 'plugin:vue/vue3-recommended', 'prettier'],
  'globals':
    {
      'BodyInit': 'readonly',
      'HeadersInit': 'readonly'
    }, 'parser': 'vue-eslint-parser',
  'parserOptions': {
    'parser': '@typescript-eslint/parser'
  },
  'plugins': ['vue', 'prettier', 'unused-imports'],
  'rules': {
    'vue/no-v-html': 'off',
    'vue/multi-word-component-names': 'off',
    'prettier/prettier': ['error'],
    'vue/html-indent': ['error', 2],
    '@typescript-eslint/no-unused-vars': 'off',
    'unused-imports/no-unused-imports': 'error',
    'unused-imports/no-unused-vars': [
      'warn',
      { 'vars': 'all', 'varsIgnorePattern': '^_', 'args': 'after-used', 'argsIgnorePattern': '^_' }
    ]
  }
}
