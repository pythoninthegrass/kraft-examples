# Wordpress with Nginx and MariaDB

[Wordpress](https://wordpress.com/) is a web content management system. It is often used to create blogs and websites. It needs a web server like [Nginx](https://nginx.org/) and a database to store user content.

## Deployment

This example uses a [`compose.yaml`](compose.yaml) file to define the Wordpress and MariaDB services. Nginx is run in the same instance as `php-fpm`, which is the backend for Wordpress.

To run it on Unikraft Cloud, first [install the `kraft` CLI tool](https://unikraft.org/docs/cli). Make sure you have an active account on Unikraft Cloud (UKC) and that you have authenticated your CLI with your UKC account.

```bash
export UKC_TOKEN=<your-unikraft-cloud-access-token>
export UKC_METRO=fra0
```

Then `cd` into [this](.) directory, and invoke:

```bash
kraft cloud compose up -d
```

The Wordpress server is exposed through Nginx. To get the public URL of the deployed application, run:

```bash
kraft cloud instance get wordpress-compose-wordpress
```

and look for the `fqdn` field in the output.

## Learn more

- [Wordpress's Documentation](https://wordpress.org/documentation/)
- [Nginx Documentation](https://nginx.org/en/docs/)
- [MariaDB Documentation](https://mariadb.com/docs/)
- [Unikraft Cloud's Documentation](https://unikraft.com/docs/introduction)
- [Building `Dockerfile` Images with `Buildkit`](https://unikraft.org/guides/building-dockerfile-images-with-buildkit)
