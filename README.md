# danesjenovdan.si

Koda, ki poganja DJND domek.

## Development

- Main site:
  - Best way is to use docker compose and run `docker compose up` (see `compose.yaml`)
  - `djnd` is the main django project folder
  - `css-compile` is the main folder for compiling css with tailwind

- Website redirects:
  - `website-redirects` is a seperate project that handles custom redirects from other domains. Initially used for `agrument.danesjenovdan.si`, but can be extended for anything else via nginx config.

## Deployment

- Deployment is setup to run automatically when pushed:
  - Production: to the `v3-k8s` branch
  - Staging: to the `v3-k8s-staging` branch

- Always merge (PRs are created automatically on push to `v3-dev`):
  - from `v3-dev` to `v3-k8s-staging`
  - from `v3-dev` to `v3-k8s`

- **DO NOT** merge from `v3-k8s-staging` to `v3-k8s` or any other way around

### Old versions

Old versions of the site are available in git under [tags](https://github.com/danesjenovdan/danesjenovdan.si/tags)

- v1 (php, retired in 2019)
- v2 (nuxt, retired in 2024)
- v3 (current)
