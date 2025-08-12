/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ['./djnd/**/templates/**/*.html'],
  theme: {
    screens: {
      '2xl-max': {'max': '1535px'},
      'xl-max': {'max': '1279px'},
      '2lg-max': {'max': '1113px'},
      'lg-max': {'max': '1023px'},
      'md-max': {'max': '767px'},
      'sm-max': {'max': '639px'},
      'xs-max': {'max': '479px'},
    },
    fontFamily: {
      mono: ["'Courier New'", 'monospace'],
      'mono-flags': ["'Courier New'", 'monospace', 'noto-color-emoji-flag-subset'],
    },
    fontSize: {
      'sm': ['0.875rem', '1rem'],
      'base': ['1rem', '1.5rem'],
      'smd': ['1.125rem', '1.5rem'],
      'md': ['1.25rem', '1.625rem'],
      '2md': ['1.3125rem', '1.875rem'],
      'lg': ['1.5rem', '2.25rem'],
      '2lg': ['1.625rem', '2.25rem'],
      '3lg': ['1.875rem', '2.125rem'],
      'xl': ['2rem', '2.625rem'],
      '2xl': ['2.25rem', '2.5rem'],
      '3xl': ['2.5rem', '1.625rem'],
      '4xl': ['3rem', '1.625rem'],
      '5xl': ['3.5rem', '4.1875rem'],
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
        fill240: 'repeat(auto-fill, minmax(240px, 1fr))',
        fill290: 'repeat(auto-fill, minmax(290px, 1fr))',
      },
      animation: {
        'arrow-hover': 'arrowHover 1s ease-in-out',
        'arrow-hover-down': 'arrowHoverDown 1s ease-in-out',
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
        arrowHoverDown: {
          '0%': { transform: 'translateY(0)' },
          '6%': { transform: 'translateY(-3px)' },
          '18%': { transform: 'translateY(2px)' },
          '31%': { transform: 'translateY(-1px)' },
          '43%': { transform: 'translateY(1px)' },
          '50%': { transform: 'translateY(0)' },
        },
      },
    },
  },
  safelist: [
    {
      pattern: /theme-color-/,
    },
    'forced-animated-bg-show',
    'forced-animated-bg-hide',
    'forced-box-scale',
  ],
  plugins: [require('@tailwindcss/forms')],
};
