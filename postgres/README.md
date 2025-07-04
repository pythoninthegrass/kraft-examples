# PostgreSQL

[PostgreSQL](https://www.postgresql.org/) is a powerful, open source object-relational database system.

To run PostgreSQL on Unikraft Cloud, first [install the `kraft` CLI tool](https://unikraft.org/docs/cli).
Then clone this examples repository and `cd` into this directory, and invoke:

```console
kraft cloud deploy --metro fra0 -M 1024 -e POSTGRES_PASSWORD=unikraft -p 5432:5432/tls .
```

Now you can query PostgreSQL using [`psql`](https://www.postgresql.org/docs/current/app-psql.html).
For that, use the following `psql` command:

```console
psql "postgresql://postgres:unikraft@<NAME>.<METRO>.kraft.host:5432/postgres?sslmode=require"
```

where `<NAME>.<METRO>.kraft.host` is the name of the instance created above.

Use SQL and `psql` commands for your work.
To stop the `psql` process, simply exit the command line interface.

## Using Volumes

You can use volumes for data persistence for you PostgreSQL instance.

For that you would first create a volume:

```console
kraft cloud volume create --name postgres --size 200
```

Then start the PostgreSQL instance and mount that volume:

```console
kraft cloud deploy --metro fra0 -M 1024 -e POSTGRES_PASSWORD=unikraft -e PGDATA=/volume/postgres -v postgres:/volume -p 5432:5432/tls .
```

## Learn more

- [PostgreSQL's Documentation](https://www.postgresql.org/docs/)
- [Unikraft Cloud's Documentation](https://unikraft.cloud/docs/)
- [Building `Dockerfile` Images with `Buildkit`](https://unikraft.org/guides/building-dockerfile-images-with-buildkit)
