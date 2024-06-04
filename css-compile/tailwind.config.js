/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./djnd/**/templates/**/*.html"],
  theme: {
    fontFamily: {
      mono: ["'Courier New'", "monospace"],
    },
    colors: {
      current: "currentColor",
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
      "red-light": "#FFF8F6",
      green: "#D2F29D",
      blue: "#BAE2ED",
      "blue-light": "#F5FDFF",
      yellow: "#FFEDAD",
      lavender: "#CCC7FF",
      "lavender-light": "#EEEDFF",
    },
    extend: {
      gridTemplateColumns: {
        fill230: "repeat(auto-fill, minmax(230px, 1fr))",
      },
      listStyleImage: {
        arrow: 'url("/static/img/noun-arrow-right-1434311.svg")',
      },
      animation: {
        "arrow-hover": "arrowHover 1s ease-in-out",
      },
      keyframes: {
        arrowHover: {
          "0%": { transform: "translateX(0)" },
          "6%": { transform: "translateX(-3px)" },
          "18%": { transform: "translateX(2px)" },
          "31%": { transform: "translateX(-1px)" },
          "43%": { transform: "translateX(1px)" },
          "50%": { transform: "translateX(0)" },
        },
      },
    },
  },
  safelist: [
    {
      pattern: /bg-(white|mint|red|green|blue|yellow|lavender)(-light)?$/,
    },
  ],
  plugins: [require("@tailwindcss/forms")],
};
