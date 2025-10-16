# Node18 Wings.io

[Node.js](https://nodejs.org) is a free, open-source, cross-platform JavaScript runtime environment.

To run Node.js on Unikraft Cloud, first [install the `kraft` CLI tool](https://unikraft.org/docs/cli).
Then clone this examples repository and `cd` into this directory, and invoke:

```console
kraft cloud deploy --metro fra -p 443:3000 -M 1024 .
```

The command will deploy an `wings.io` alternative called `https://github.com/Blendlight/wings.io-clone-io`.

After deploying, you can query the service using the provided URL.

## Learn more

- [Node.js's Documentation](https://nodejs.org/docs/latest/api/)
- [Unikraft Cloud's Documentation](https://unikraft.cloud/docs/)
- [Building `Dockerfile` Images with `Buildkit`](https://unikraft.org/guides/building-dockerfile-images-with-buildkit)

