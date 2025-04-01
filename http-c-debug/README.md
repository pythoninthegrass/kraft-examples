# Simple C HTTP Server Base Compat and Debugging

This is a simple HTTP server written in the C programming language.

To run this example on Unikraft Cloud, first [install the `kraft` CLI tool](https://unikraft.org/docs/cli).
Then clone this examples repository and `cd` into this directory, and invoke:

```console
kraft cloud deploy --metro fra0 -p 443:8080/http+tls -p 2222:2222/tls -e PUBKEY="...." .
```

The command will build and deploy the `http_server.c` source code file in debugging mode.

After deploying, you can query the service using the provided URL.

To connect to the debug console (via SSH), run the command below:

```console
kraft cloud tunnel 2222:<instance-name>:2222
```

Then connect to the instance via SSH using:

```console
ssh -l root localhost -p 2222
```

For extensive debug information with `strace`, add the `USE_STRACE=1` environment variable to the deploy command:

```console
kraft cloud deploy --metro fra0 -p 443:8080/http+tls -p 2222:2222/tls -e PUBKEY="...." -e USE_STRACE=1 .
```

## Learn more

- [Unikraft Cloud's Documentation](https://unikraft.cloud/docs/)
- [Building `Dockerfile` Images with `Buildkit`](https://unikraft.org/guides/building-dockerfile-images-with-buildkit)
