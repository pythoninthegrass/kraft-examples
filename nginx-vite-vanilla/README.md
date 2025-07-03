# Vite (vanilla) static build on Unikraft Cloud

This example demonstrates how to run a [Vite](https://vite.dev) project which
has been built for production on [Unikraft Cloud](https://unikraft.cloud).  The
deployment does not perform any server side rendering (non-SSR) and instead
serves the resulting artifacts statically (via `npm run build`) using
[`nginx`](../nginx). To use Vite in SSR mode or via the `dev` subcommand on a
NodeJS runtime, please see the [`node-vite-vanilla`](../node-vite-vanilla)
sibling project.


## Initialization

The project was instantiated via:

```
npm create vite@latest my-vue-app -- --template vanilla
```

The accompanying [`Dockerfile`](./Dockerfile) and [`Kraftfile`](./Kraftfile) are
necessary for deploying to Unikraft Cloud.


## Deployment

To deploy, `cd` into this directory and run:

```bash
kraft cloud deploy -p 443:8080 .
```

After deploying, you can query the service using the provided URL.


## Learn more

- [NGINX's Documentation](https://nginx.org/en/docs)
- [Vite's Documentation](https://vite.dev/guide/)
- [Unikraft Cloud's Documentation](https://unikraft.cloud/docs)
- [Building `Dockerfile` images with `Buildkit`](https://unikraft.org/guides/building-dockerfile-images-with-buildkit)


## See also

- [Vite (vanilla) node "dev" server on Unikraft Cloud](../node-vite-vanilla)
- [Vite (vanilla) SSR mode on Unikraft Cloud](../node-vite-ssr-vanilla)
