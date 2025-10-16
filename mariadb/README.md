# MariaDB

[MariaDB](https://mariadb.org/) is one of the most popular open source relational databases.

To run MariaDB on Unikraft Cloud, first [install the `kraft` CLI tool](https://unikraft.org/docs/cli).
Then clone this examples repository and `cd` into this directory, and invoke:

```console
kraft cloud deploy --metro fra -p 3306:3306/tls -M 1024 .
```

Get the results of the deployment by first forwarding the port:

```console
kraft cloud tunnel <instance_name>:3306
```

where `<instance_name>` is the name of the instance returned by the `kraft cloud deploy` command, typically `mariadb-<some_random_string_here>`.

Then, on another console, run a MariaDB client.
You can use either the `mysql` client:

```console
mysql -h 127.0.0.1 --ssl-mode=DISABLED -u root -punikraft mysql <<< "select count(*) from user"
```

Or you can use the `mariadb` client:

```console
mariadb -h 127.0.0.1 --ssl=OFF -u root -punikraft mysql <<< "select count(*) from user"
```

## Learn more

- [MariaDB's Documentation](https://mariadb.org/documentation/)
- [Unikraft Cloud's Documentation](https://unikraft.cloud/docs/)
- [Building `Dockerfile` Images with `Buildkit`](https://unikraft.org/guides/building-dockerfile-images-with-buildkit)
