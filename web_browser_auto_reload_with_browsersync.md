# Browsersync

Browsersync for auto reload assets files
Homepage: [https://browsersync.io/](https://browsersync.io/)

## Steps

```sh
npm install -g browser-sync
```

add tag to `index.html` to allow CSP

```html
<meta http-equiv="Content-Security-Policy" content="default-src *; style-src 'self' 'unsafe-inline'; script-src 'self' 'unsafe-inline' 'unsafe-eval'; img-src 'self' data:">
```
**NOTE: remove on production !!!**

```sh
browser-sync start --server 'bin' --files 'bin'
```
Very fast reload + debug :D

```sh
browser-sync start --reload-delay 0 --no-ui --no-inject-changes --logLevel debug --server 'bin' --files 'bin'
```
