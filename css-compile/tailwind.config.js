/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ['./djnd/**/templates/**/*.html'],
  theme: {
    fontFamily: {
      mono: ["'Courier New'", 'monospace'],
    },
    fontSize: {
      'sm': ['14px', '16px'],
      'base': ['16px', '26px'],
      'smd': ['18px', '28px'],
      'md': ['20px', '26px'],
      'lg': ['24px', '36px'],
      'xl': ['32px', '42px'],
      '2xl': ['36px', '48px'],
      '3xl': ['40px', '26px'],
      '4xl': ['48px', '26px'],
      '5xl': ['56px', '67px'],
    },
    colors: {
      'current': 'currentColor',
      'white': '#ffffff',
      'very-light': '#F6F9F8',
      'light': '#eeeeee',
      'dark': '#333333',
      // dark colors:
      'dark-green': '#6CA89F',
      'dark-red': '#DF786B',
      'dark-yellow': '#CFAD54',
      // light colors:
      'mint': '#9DF2D3',
      'mint-light': '#EAFFF7',
      'red': '#FFD1C7',
      'red-light': '#FFF8F6',
      'green': '#D2F29D',
      'green-light': '#EBF4DB',
      'blue': '#BAE2ED',
      'blue-light': '#E6F0F3',
      'yellow': '#FFEDAD',
      'yellow-light': '#FFF7DB',
      'lavender': '#CCC7FF',
      'lavender-light': '#EEEDFF',
      // theme colors:
      'th-primary': 'var(--th-primary)',
      'th-primary-light': 'var(--th-primary-light)',
    },
    extend: {
      gridTemplateColumns: {
        fill230: 'repeat(auto-fill, minmax(230px, 1fr))',
      },
      listStyleImage: {
        arrow: 'url("/static/img/noun-arrow-right-1434311.svg")',
      },
      animation: {
        'arrow-hover': 'arrowHover 1s ease-in-out',
      },
      keyframes: {
        arrowHover: {
          '0%': { transform: 'translateX(0)' },
          '6%': { transform: 'translateX(-3px)' },
          '18%': { transform: 'translateX(2px)' },
          '31%': { transform: 'translateX(-1px)' },
          '43%': { transform: 'translateX(1px)' },
          '50%': { transform: 'translateX(0)' },
        },
      },
    },
  },
  safelist: [
    {
      pattern: /theme-color-/,
    },
  ],
  plugins: [require('@tailwindcss/forms')],
};
