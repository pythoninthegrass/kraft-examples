# Very Secure FTP Daemon

[Very Secure FTP Daemon (vsftpd)](https://security.appspot.com/vsftpd.html) is a secure and fast FTP server for Unix-like systems. It is designed to be secure and efficient, with a focus on performance and ease of use.
It allows you to run a secure FTP server on a remote machine and access it through a web browser or a local FTP client.

## Deployment

To run this example on Unikraft Cloud, first [install the `kraft` CLI tool](https://unikraft.org/docs/cli). Make sure you have an active account on Unikraft Cloud (UKC) and that you have authenticated your CLI with your UKC account.

```bash
export UKC_TOKEN=<your-unikraft-cloud-access-token>
export UKC_METRO=fra0
```

Then `cd` into [this](.) directory, and invoke:

```bash
kraft cloud volume create \
    --name vsftpd-workspace \
    --size 1Gi

kraft cloud deploy \
    --scale-to-zero on \
    --scale-to-zero-stateful \
    --scale-to-zero-cooldown 3s \
    --name vsftpd \
    -M 1024Mi \
    -p 20:20/tls \
    -p 21:21/tls \
    -p 222:22/tls \
    -p 990:990/tls \
    -p 10100:10100/tls \
    -v "vsftpd-workspace":/home/ftpuser \
    .
```

Now, you can access the `vsftpd` instance at the provided URL. You can test using an FTP client like `lftp`:

```bash
$ lftp -u ftpuser,ftpuserpass ftps://<URL>:21
lftp ftpuser@damp-grass-awnbbv20.fra0.kraft.host:~> ls
```

## Volume

This deployment creates a volume for the user's data persistence: `vsftpd-workspace`.
Upon deleting the instance (e.g., `kraft cloud instance rm vsftpd`), this volume will persist, allowing you to create another instance without losing data.
To remove the volume, you can use:

```bash
kraft cloud volume rm vsftpd-workspace
```

## Learn more

- [vsftpd documentation](https://security.appspot.com/vsftpd/vsftpd_conf.html)
- [Unikraft Cloud's Documentation](https://unikraft.cloud/docs/)
- [Building `Dockerfile` Images with `Buildkit`](https://unikraft.org/guides/building-dockerfile-images-with-buildkit)