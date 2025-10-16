# Visual Studio Code server

[Visual Studio Code](https://code.visualstudio.com/) is a source-code editor developed by Microsoft. It includes support for debugging, syntax highlighting, intelligent code completion, snippets, code refactoring, and embedded Git.

The [Code Server](https://code.visualstudio.com/docs/remote/vscode-server) allows you to run Visual Studio Code on a remote server and access it through a web browser
or a local VS Code client.

## Deployment

To run this example on Unikraft Cloud, first [install the `kraft` CLI tool](https://unikraft.org/docs/cli). Make sure you have an active account on Unikraft Cloud (UKC) and that you have authenticated your CLI with your UKC account.

```bash
export UKC_TOKEN=<your-unikraft-cloud-access-token>
export UKC_METRO=fra
```

Then `cd` into [this](.) directory, and invoke:

```bash
kraft cloud volume create \
    --name code-workspace \
    --size 1Gi

kraft cloud deploy \
    --scale-to-zero on \
    --scale-to-zero-stateful \
    --scale-to-zero-cooldown 4s \
    -M 2048 \
    --name code-server \
    -p 443:8443 \
    -v code-workspace:/workspace \
    -e PGUID=0 \
    -e PGID=0 \
    -e PASSWORD=unikraft \
    -e SUDO_PASSWORD=unikraft \
    -e DEFAULT_WORKSPACE="/workspace" \
    .
```

Now, you can access the Code Server in the browser, at the provided URL.

## Volume

This deployment creates a volume for data persistence: `code-workspace`.
Upon deleting the instance (e.g., `kraft cloud instance rm code-server`), this volume will persist, allowing you to create another instance without losing data.
To remove the volume, you can use:

```bash
kraft cloud volume rm code-workspace
```

## Learn more

- [Visual Studio Code](https://code.visualstudio.com/)
- [Code Server](https://code.visualstudio.com/docs/remote/vscode-server)
- [Unikraft Cloud's Documentation](https://unikraft.cloud/docs/)
- [Building `Dockerfile` Images with `Buildkit`](https://unikraft.org/guides/building-dockerfile-images-with-buildkit)