# noVNC

[noVNC](https://novnc.com/info.html) is an open-source [VNC](https://en.wikipedia.org/wiki/VNC) client that runs in the browser,
allowing you to access remote desktops through a web interface, using your favorite modern web browser.

This sample deployment shows how to set up a VNC server on UKC, which enables you to access the VM remotely, with a graphical interface.
The VM is an Ubuntu 22.04 machine with Firefox and other apps preinstalled.

**Note**: This example is inspired from Anthropic's [Computer Use Demo](https://github.com/anthropics/anthropic-quickstarts/tree/main/computer-use-demo).

## Deployment

To run this example on Unikraft Cloud, first [install the `kraft` CLI tool](https://unikraft.org/docs/cli). Make sure you have an active account on Unikraft Cloud (UKC) and that you have authenticated your CLI with your UKC account.

```bash
export UKC_TOKEN=<your-unikraft-cloud-access-token>
export UKC_METRO=fra
```

Then `cd` into [this](.) directory, and invoke:

```bash
kraft cloud deploy \
    --scale-to-zero on \
    --scale-to-zero-stateful \
    --scale-to-zero-cooldown 4s \
    -M 4096 \
    -p 443:6080 \
    -n vnc-browser \
    .
```

Now, you can access the `vnc-browser` instance at the provided URL.

## Learn more

- [noVNC source code](https://github.com/novnc/noVNC)
- [Unikraft Cloud's Documentation](https://unikraft.cloud/docs/)
- [Building `Dockerfile` Images with `Buildkit`](https://unikraft.org/guides/building-dockerfile-images-with-buildkit)
