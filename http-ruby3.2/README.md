# Simple Ruby3.2 HTTP Server

This is a simple HTTP server written in the [Ruby](https://www.ruby-lang.org/) programming language.

To run this example on Unikraft Cloud, first [install the `kraft` CLI tool](https://unikraft.org/docs/cli).
Then clone this examples repository and `cd` into this directory, and invoke:

```console
kraft cloud deploy --metro fra -p 443:8080 -M 256 .
```

The command will deploy the `server.rb` source code file.

After deploying, you can query the service using the provided URL.

## Learn more

- [Ruby's Documentation](https://www.ruby-lang.org/en/documentation/)
- [Unikraft Cloud's Documentation](https://unikraft.cloud/docs/)
- [Building `Dockerfile` Images with `Buildkit`](https://unikraft.org/guides/building-dockerfile-images-with-buildkit)
