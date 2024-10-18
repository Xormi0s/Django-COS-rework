/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./templates/**/*.html", "./static/**/*.js"],
  theme: {
    extend: {
      colors: {
        "custom-gray": "#4e4e61", // Voeg hier je custom kleur toe
      },
    },
  },
  plugins: [],
};
