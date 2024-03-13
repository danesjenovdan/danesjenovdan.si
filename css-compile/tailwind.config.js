/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./djnd/**/templates/**/*.html"],
  theme: {
    fontFamily: {
      mono: ["'Courier New'", "monospace"],
    },
    colors: {
      white: "#ffffff",
      "very-light": "#F6F9F8",
      light: "#eeeeee",
      dark: "#333333",
      // dark colors:
      "dark-green": "#6CA89F",
      "dark-red": "#DF786B",
      "dark-yellow": "#CFAD54",
      // light colors:
      mint: "#9DF2D3",
      "mint-light": "#EAFFF7",
      red: "#FFD1C7",
      green: "#D2F29D",
      blue: "#BAE2ED",
      yellow: "#FFEDAD",
      lavender: "#CCC7FF",
    },
    extend: {
      gridTemplateColumns: {
        fill230: "repeat(auto-fill, minmax(230px, 1fr))",
      },
      listStyleImage: {
        arrow: 'url("/static/img/noun-arrow-right-1434311.svg")',
      },
    },
  },
  plugins: [require("@tailwindcss/forms")],
};
