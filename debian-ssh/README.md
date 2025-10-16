# Debian SSH Connection

This is a Debian SSH server deployed on Unikraft Cloud, as a debug interface.

To run this example on Unikraft Cloud, first [install the `kraft` CLI tool](https://unikraft.org/docs/cli).
Then clone this examples repository and `cd` into this directory, and invoke:

```console
kraft cloud deploy --metro fra -M 1Gi -e PUBKEY="...." .
```

To connect to the debug console (via SSH), run the command below:

```console
kraft cloud tunnel 2222:<instance-name>:2222
```

Then connect to the instance via SSH using:

```console
ssh -l root localhost -p 2222
```

## Learn more

- [Unikraft Cloud's Documentation](https://unikraft.cloud/docs/)
- [Building `Dockerfile` Images with `Buildkit`](https://unikraft.org/guides/building-dockerfile-images-with-buildkit)
