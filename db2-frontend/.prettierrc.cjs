module.exports = {
  'printWidth': 100,
  'semi': false,
  'singleQuote': true,
  'tabWidth': 2,
  'trailingComma': 'none',
  'vueIndentScriptAndStyle': false,
  'htmlWhitespaceSensitivity': 'ignore',
  'importOrder': [
    '^@/[^components](.*)$',
    '^@/components/(.*)$',
    '^[./]'
  ],
  'importOrderSeparation': true,
  'importOrderSortSpecifiers': true,
  'plugins': ['@trivago/prettier-plugin-sort-imports']
}
