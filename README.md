# danesjenovdan.si

Koda, ki poganja DJND domek.

## Development

- Main site:
  - Best way is to use docker compose and run `docker compose up` (see `compose.yaml`)
  - `djnd` is the main django project folder
  - `css-compile` is the main folder for compiling css with tailwind

- Website redirects:
  - `website-redirects` is a seperate project that handles custom redirects from other domains. Initially used for `agrument.danesjenovdan.si`, but can be extended for anything else via nginx config.

### Old versions

Old versions of the site are available in git under [tags](https://github.com/danesjenovdan/danesjenovdan.si/tags)

- v1 (php, retired in 2019)
- v2 (nuxt, retired in 2024)
- v3 (current)
