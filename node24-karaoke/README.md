# Node 24 AllKaraoke

[Allkaraoke](https://github.com/Asvarox/allkaraoke) offers an ultrastar deluxe-like online platform for karaoke.

To run Allkaraoke on Unikraft Cloud, first [install the `kraft` CLI tool](https://unikraft.org/docs/cli).
Then clone this examples repository and `cd` into this directory, and invoke:

```bash
kraft cloud deploy -p 443:8080 -M 2Gi .
```

The command will build the files in the current directory.

After deploying, you can query the service using the provided URL.

## Learn more

- [Allkaraoke official deployment](https://allkaraoke.party/)
- [Unikraft Cloud's Documentation](https://unikraft.cloud/docs/)
- [Building `Dockerfile` Images with `Buildkit`](https://unikraft.org/guides/building-dockerfile-images-with-buildkit)
