# Memcached

[Memcached](https://memcached.org) is an in-memory key-value store for small chunks of arbitrary data (strings, objects) from results of database calls, API calls, or page rendering.

To run Memcached on Unikraft Cloud, first [install the `kraft` CLI tool](https://unikraft.org/docs/cli).
Then clone this examples repository and `cd` into this directory, and invoke:

```console
kraft cloud deploy --metro fra -p 11211:11211/tls -M 256 .
```

Get the results of the deployment by first forwarding the port (save the returned PID):

```console
socat tcp-listen:11211,bind=127.0.0.1,fork,reuseaddr openssl:<NAME>.<METRO>.unikraft.app:11211 &
```

Then, run the following commands to test that it works (you should see output when incrementing):

```console
telnet 127.0.0.1 11211
set test 0 0 1
0
incr test 1
incr test 1
```

To exit telnet and stop the socat process, run:

```console
Ctrl + ]
Ctrl + C
kill -9 <PID>
```

## Learn more

- [Memcached's Documentation](https://github.com/memcached/memcached/wiki)
- [Unikraft Cloud's Documentation](https://unikraft.cloud/docs/)
- [Building `Dockerfile` Images with `Buildkit`](https://unikraft.org/guides/building-dockerfile-images-with-buildkit)
