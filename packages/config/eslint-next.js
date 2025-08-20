module.exports = {
  root: false,
  env: {
    browser: true,
    es2021: true,
    node: true,
  },
  parser: '@typescript-eslint/parser',
  plugins: ['@typescript-eslint', 'react', 'react-hooks', 'jsx-a11y', 'prettier'],
  extends: [
    'eslint:recommended',
    'plugin:@typescript-eslint/recommended',
    'plugin:react/recommended',
    'plugin:react-hooks/recommended',
    'plugin:jsx-a11y/recommended',
    'plugin:prettier/recommended',
    'next/core-web-vitals',
  ],
  settings: {
    react: {
      version: 'detect',
    },
  },
  rules: {
    // example overrides; can be expanded later
    'react/react-in-jsx-scope': 'off',
  },
};
